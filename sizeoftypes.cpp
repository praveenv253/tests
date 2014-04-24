#include <iostream>
#include <wchar.h>
#include <complex.h>

using namespace std;

int main()
{
	cout << "sizeof(char): " << sizeof(char) << endl;
	cout << "sizeof(short int): " << sizeof(short int) << endl;
	cout << "sizeof(int): " << sizeof(int) << endl;
	cout << "sizeof(long long): " << sizeof(long long) << endl;
	cout << "sizeof(float): " << sizeof(float) << endl;
	cout << "sizeof(double): " << sizeof(double) << endl;
	cout << "sizeof(long double): " << sizeof(long double) << endl;
	cout << "sizeof(void *): " << sizeof(void *) << endl;
	cout << "sizeof(char *): " << sizeof(char *) << endl;
	cout << "sizeof(int *): " << sizeof(int *) << endl;
	cout << "sizeof(float *): " << sizeof(float *) << endl;
	cout << "sizeof(double *): " << sizeof(double *) << endl;
	cout << "sizeof(wchar): " << sizeof(wchar_t) << endl;
	cout << "sizeof(double complex): " << sizeof(double complex) << endl;
	return 0;
}
