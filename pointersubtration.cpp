#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	double *a = new double[10];
	int *b = new int;
	int *c;
	printf("%p %p\n", &a[10], &a[9]);
	//printf("%p\n", &a[10] - &a[9]);
	printf("%ld\n", (long) ( &a[10] - &a[9] ));

	c = b + (&a[10] - &a[9]);
	printf("%p\n", b);
	printf("%p\n", c);

	return 0;
}
