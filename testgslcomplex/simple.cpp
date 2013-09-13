#include <iostream>
#include <gsl/gsl_complex_math.h>
#include <complex>
#include <ctime>
#include <cstdlib>

int main()
{
	// Array size for testing performance
	const int N = 1e7;

	clock_t clk_start;
	clock_t clk_end;

	// First generate a gsl and an std::complex array of random complexes.
	//srand((unsigned)time(0));
	double real1, imag1, real2, imag2;
	gsl_complex *g1, *g2, *g3;
	g1 = new gsl_complex[N];
	g2 = new gsl_complex[N];
	g3 = new gsl_complex[N];
	std::complex<double> *c1, *c2, *c3;
	c1 = new std::complex<double>[N];
	c2 = new std::complex<double>[N];
	c3 = new std::complex<double>[N];

	int i;
	for(i = 0; i < N; i++) {
		real1 = 10 * (double) rand() / (double) RAND_MAX;
		imag1 = 10 * (double) rand() / (double) RAND_MAX;
		real2 = 10 * (double) rand() / (double) RAND_MAX;
		imag2 = 10 * (double) rand() / (double) RAND_MAX;
		
		GSL_SET_COMPLEX(&g1[i], real1, imag1);
		c1[N] = std::complex<double>(real1, imag1);
		GSL_SET_COMPLEX(&g2[i], real2, imag2);
		c2[N] = std::complex<double>(real2, imag2);
	}

	clk_start = clock();
	for(i = 0; i < N; i++) {
		g3[i] = gsl_complex_add(g1[i], g2[i]);
	}
	clk_end = clock();

	std::cout << "GSL: " << (double)(clk_end - clk_start) / CLOCKS_PER_SEC
			  << std::endl;

	clk_start = clock();
	for(i = 0; i < N; i++) {
		c3[i] = c1[i] + c2[i];
	}
	clk_end = clock();

	std::cout << "std::complex: "
			  << (double)(clk_end - clk_start) / CLOCKS_PER_SEC << std::endl;

	return 0;
}

