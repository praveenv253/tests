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

int main()
{
	high_resolution_clock::time_point time_start;
	high_resolution_clock::time_point time_end;
	microseconds tot_time;
	double avg_time;

	// First generate a gsl and an std::complex array of random complexes.
	//srand((unsigned)time(0));
	int real1, imag1, real2, imag2;
	gsl_complex *g1, *g2, *g3;
	g1 = new gsl_complex[N];
	g2 = new gsl_complex[N];
	g3 = new gsl_complex[N];
	std::complex<int> *c1, *c2, *c3;
	c1 = new std::complex<int>[N];
	c2 = new std::complex<int>[N];
	c3 = new std::complex<int>[N];

	int i;
	for(i = 0; i < N; i++) {
		real1 = rand();
		imag1 = rand();
		real2 = rand();
		imag2 = rand();
		
		GSL_SET_COMPLEX(&g1[i], real1, imag1);
		c1[N] = std::complex<int>(real1, imag1);
		GSL_SET_COMPLEX(&g2[i], real2, imag2);
		c2[N] = std::complex<int>(real2, imag2);
	}

	int count;
	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			c3[i] = c1[i] + c2[i];
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = double(tot_time.count()) / num_iter;

	cout << "std::complex addition: " << avg_time << "us" << endl;

	tot_time = microseconds(0);
	for(count = 0; count < num_iter; count++) {
		time_start = high_resolution_clock::now();
		for(i = 0; i < N; i++) {
			c3[i] = c1[i] * c2[i];
		}
		time_end = high_resolution_clock::now();
		tot_time += duration_cast<microseconds>(time_end - time_start);
	}
	avg_time = double(tot_time.count()) / num_iter;

	cout << "std::complex multiplication: " << avg_time << "us" << endl;

	return 0;
}

