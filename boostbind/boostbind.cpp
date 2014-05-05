#include <iostream>
#include <boost/bind.hpp>

class Incrementor {
	public:
		int x;

		Incrementor();
		~Incrementor();
		void increment(int y = 1);
};

Incrementor::Incrementor()
{
	std::cout << "Constructor" << std::endl;
	x = 10;
}

Incrementor::~Incrementor()
{
	std::cout << "Destructor: " << x << std::endl;
}

void Incrementor::increment(int y)
{
	x += y;
}

void funcbyvalue(Incrementor inc)
{
	inc.increment();
}

void funcbyref(Incrementor &inc)
{
	inc.increment();
}

int main()
{
	Incrementor inc;

	std::cout << "By value:" << std::endl;
	boost::bind(funcbyvalue, inc)();

	std::cout << "By reference:" << std::endl;
	boost::bind(funcbyref, boost::ref(inc))();
	// Gets destroyed automatically

	return 0;
}

