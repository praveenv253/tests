#ifndef A_H
#define A_H

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

#endif
