#include <stdio.h>
#include <stdlib.h>

int main()
{
	int t = 19;
	int i;
	for(i = 0; i < 10; i++) {
		printf("%d\n", rand_r(&t));
	}
	return 0;
}
