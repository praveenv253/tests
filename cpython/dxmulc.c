#include <dxmulc.h>

double *dxmul(int *sup, double *vals, double *D, int k, int m, int n)
{
	/* Internal variables */
	int i, j;

	/* Output pointer */
	double *output;

	/* Do a memory allocation for output */
	output = (double *) malloc(m*sizeof(double));

	/* Remember that data is assumed to be row major */

	for(i = 0; i < m; i++)
	{
		output[i] = 0;
		for (j = 0; j < k; j++)
		{
			output[i] = output[i] + D[i*n + sup[j]]*vals[j];
		}
	}

	/* Done */
	return output;
}
