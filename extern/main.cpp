#include <iostream>
//#include "A.h"

using namespace std;

class A {
	private:
		int x;
	public:
		A() {
			x = 10;
		}
		A(int a) {
			x = a;
		}
		void inc();
		void print();
};

int main()
{
	A a;
	a.print();
	a.inc();
	a.print();
}
