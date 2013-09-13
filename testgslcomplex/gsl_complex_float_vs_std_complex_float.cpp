#include <iostream>
#include <gsl/gsl_complex_math.h>
#include <complex>
#include <ctime>
#include <cstdlib>
#include <ratio>
#include <chrono>

// Array size for testing performance
const int N = 4500;
// Number of times to run test
const int num_iter = 1e5;

using namespace std;
using namespace std::chrono;

/* NOTE: The functions gsl_complex_float_add and gsl_complex_float_mul have
 * been written exactly the same way as gsl_complex_add and gsl_complex_mul,
 * with the only difference being in the data type.
 */
gsl_complex_float gsl_complex_float_add(gsl_complex_float a,
										gsl_complex_float b)
{
	float ar = GSL_REAL (a), ai = GSL_IMAG (a);
	float br = GSL_REAL (b), bi = GSL_IMAG (b);

	gsl_complex_float z;
	GSL_SET_COMPLEX(&z, ar + br, ai + bi);
	return z;
}

gsl_complex_float gsl_complex_float_mul(gsl_complex_float a,
										gsl_complex_float b)
{
	float ar = GSL_REAL (a), ai = GSL_IMAG (a);
	float br = GSL_REAL (b), bi = GSL_IMAG (b);

	gsl_complex_float z;
	GSL_SET_COMPLEX(&z, ar * br - ai * bi, ar * bi + ai * br);
	return z;
}

int main()
{
	high_resolution_clock::time_point time_start;
	high_resolution_clock::time_point time_end;
	microseconds tot_time;
	float avg_time;

	// First generate a gsl and an std::complex array of random complexes.
	//srand((unsigned)time(0));
	float real1, imag1, real2, imag2;
	gsl_complex_float *g1, *g2, *g3;
	g1 = new gsl_complex_float[N];
	g2 = new gsl_complex_float[N];
	g3 = new gsl_complex_float[N];
	std::complex<float> *c1, *c2, *c3;
	c1 = new std::complex<float>[N];
	c2 = new std::complex<float>[N];
	c3 = new std::complex<float>[N];

	int i;
	for(i = 0; i < N; i++) {
		real1 = 10 * (float) rand() / (float) RAND_MAX;
		imag1 = 10 * (float) rand() / (float) RAND_MAX;
		real2 = 10 * (float) rand() / (float) RAND_MAX;
		imag2 = 10 * (float) rand() / (float) RAND_MAX;
		
		//if(i == 0)
		//    std::cout << real1 << " + j" << imag1 << std::endl;
		GSL_SET_COMPLEX(&g1[i], real1, imag1);
		c1[N] = std::complex<float>(real1, imag1);
		GSL_SET_COMPLEX(&g2[i], real2, imag2);
		c2[N] = std::complex<float>(real2, imag2);
	}

	int count;
	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			g3[i] = gsl_complex_float_add(g1[i], g2[i]);
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = float(tot_time.count()) / num_iter;

	std::cout << "GSL addition: " << avg_time << "us" << std::endl;

	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			c3[i] = c1[i] + c2[i];
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = float(tot_time.count()) / num_iter;

	std::cout << "std::complex addition: " << avg_time << "us" << std::endl;

	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			g3[i] = gsl_complex_float_mul(g1[i], g2[i]);
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = float(tot_time.count()) / num_iter;

	std::cout << "GSL multiplication: " << avg_time << "us" << std::endl;

	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			c3[i] = c1[i] * c2[i];
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = float(tot_time.count()) / num_iter;

	std::cout << "std::complex multiplication: " << avg_time << "us" << std::endl;

	return 0;
}

