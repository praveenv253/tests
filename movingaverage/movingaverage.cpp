#include <iostream>
#include <fstream>
#include <complex>

using namespace std;

int main()
{
	int n = 1e6;
	int w = 32;
	complex<float> *x = new complex<float>[n];

	fstream f("data.bin", fstream::in | fstream::binary);
	f.read((char *) x, sizeof(complex<float>) * n);
	f.close();

	int i, j;
	complex<float> *true_avg = new complex<float>[n-w+1];
	for(i = 0; i < n - w + 1; i++) {
		true_avg[i] = 0;
		for(j = i; j < i+w; j++) {
			true_avg[i] += x[j];
		}
		true_avg[i] /= float(w);
	}

	f.open("true_avg.bin", fstream::out | fstream::binary);
	f.write((char *) true_avg, sizeof(complex<float>) * (n-w+1));
	f.close();

	complex<float> mov_avg = 0;
	complex<float> *avg = new complex<float>[n-w+1];
	for(i = 0; i < n - w + 1; i++) {
		if(i == 0) {
			for(j = 0; j < w; j++) {
				mov_avg += x[i] / float(w);
			}
		} else {
			mov_avg += x[i+w-1] / float(w) - x[i-1] / float(w);
		}
		avg[i] = mov_avg;
	}

	f.open("mov_avg.bin", fstream::out | fstream::binary);
	f.write((char *) avg, sizeof(complex<float>) * (n-w+1));
	f.close();

	return 0;
}
