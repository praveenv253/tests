#include <cuda.h>
#include <cuda_runtime.h>
#include <iostream>

using namespace std;

struct Test {
	int x;
	int y;
};

__global__ void testfunc(Test t, int *z)
{
	*z = t.x + t.y;
}

int main()
{
	Test t;
	t.x = 10;
	t.y = 20;
	
	int *z;
	cudaMalloc((void **)&z, sizeof(int));
	testfunc<<<1, 1>>>(t, z);

	int hz;
	cudaMemcpy(&hz, z, sizeof(int), cudaMemcpyDeviceToHost);
	cout<<hz<<endl;

	return 0;
}
