#include <sys/time.h>
#include <iostream>

using namespace std;

int main()
{
	itimerval *timer;
	getitimer(ITIMER_VIRTUAL, timer);

	int a = 0;
	for(int i = 0; i < 1e7; i++) {
		a += i;
	}

	setitimer(ITIMER_VIRTUAL, timer, NULL);
	cout << timer.it_interval.tv_usec << endl;
	cout << a << endl;

	return 0;
}
