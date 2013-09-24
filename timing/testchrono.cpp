#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main()
{
	typedef high_resolution_clock Clock;

	time_point<Clock, microseconds> t1;
	time_point<Clock, microseconds> t2;

	t1 = time_point_cast<microseconds>( Clock::now() );
	cout << "test" << endl;
	t2 = time_point_cast<microseconds>( Clock::now() );

	microseconds time_span = duration_cast<microseconds>(t2 - t1);

	cout << time_span.count() << "us" << endl;

	return 0;
}
