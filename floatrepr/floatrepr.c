#include <stdio.h>

int main()
{
	float i = 0.0f;
	float *pi = &i;
	unsigned int j;
	printf("      s eeeeeeee ffffffffffffffffffffff\n");
	for(; i < 10.0f; i += 0.1f) {
		printf("%.2f: ", i);
		for(j = 31; j != 0; j--) {
			printf("%d", ((*(int *)(pi))>>j) & 1);
			if(j == 31 || j == 23)
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}
