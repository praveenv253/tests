#include <cstdio>
#include <iostream>
#include <poll.h>

using namespace std;

int main()
{
	pollfd p;
	p.fd = 0;
	p.events = POLLIN;
	int i = 0;
	while(1) {
		// Poll for 1s.
		int ready = poll(&p, 1, 1000);
		if(ready > 0 && (p.revents & POLLIN)) {
			break;
		} else {
			cout << ++i << endl;
		}
	}
	return 0;
}

