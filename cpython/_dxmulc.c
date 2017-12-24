#include <Python.h>
#include <numpy/arrayobject.h>
#include <dxmulc.h>

/* Define the docstring */
static char module_docstring[] =
	"Module used for wrapping C functions for python interface.";

static char dxmulc_docstring[] =
	("Computes multiplication of a matrix with a sparse vector written in"
	 "(index, value) format");

/* Now declare our python object */
static PyObject *dxmulc_dxmulc(PyObject *self, PyObject *args);

/* Define members of this module */
static PyMethodDef module_methods[] = {
	{"dxmulc", dxmulc_dxmulc, METH_VARARGS, dxmulc_docstring},
	{NULL, NULL, 0, NULL}
};

/* Initialize the module */
PyMODINIT_FUNC init_dxmulc(void)
{
	PyObject *m = Py_InitModule3("_dxmulc", module_methods, module_docstring);

	/* See if the output is null */
	if (m == NULL)
		return;

	/* Load numpy functionality */
	import_array();
}

/* Now start our main routine */
static PyObject *dxmulc_dxmulc(PyObject *self, PyObject *args)
{
	/* We have three objects as inputs and one as output*/
	PyObject *D_obj, *sup_obj, *vals_obj, *ret_obj;

	/* Data pointers */
	double *D, *vals, *output;
	int *sup;

	/* Matrix sizes */
	int m, n, k;
	npy_intp dims[2];

	/* Numpy arrays */
	PyObject *D_array, *sup_array, *vals_array;

	/* Step 1 -- parse input */
	if (!PyArg_ParseTuple(args, "OOO", &D_obj, &sup_obj, &vals_obj))
		return NULL;

	/* Extract the numpy arrays */
	D_array = PyArray_FROM_OTF(D_obj, NPY_DOUBLE, NPY_IN_ARRAY);
	sup_array = PyArray_FROM_OTF(sup_obj, NPY_INT, NPY_IN_ARRAY);
	vals_array = PyArray_FROM_OTF(vals_obj, NPY_DOUBLE, NPY_IN_ARRAY);

	/* Check that the objects were successfully translated into arrays */
	if (D_array == NULL || sup_array == NULL || vals_array == NULL)
	{
		Py_XDECREF(D_array);
		Py_XDECREF(sup_array);
		Py_XDECREF(vals_array);
		return NULL;
	}

	/* Awesome. Now get the dimension of the matrices */
	m = (int)PyArray_DIM(D_array, 0);
	n = (int)PyArray_DIM(D_array, 1);
	k = (int)PyArray_DIM(sup_array, 0);

	/* Get data pointers */
	D = (double *)PyArray_DATA(D_array);
	sup = (int *)PyArray_DATA(sup_array);
	vals = (double *)PyArray_DATA(vals_array);

	/* Okay that is done as well. Call the main function */
	output = dxmul(sup, vals, D, k, m, n);
	dims[0] = m;
	dims[1] = 1;

	/* Clean up */
	Py_DECREF(D_array);
	Py_DECREF(sup_array);
	Py_DECREF(vals_array);

	/* Build output */
	ret_obj = PyArray_SimpleNewFromData(2, dims, NPY_DOUBLE, output);

	/* Return */
	return ret_obj;
}
