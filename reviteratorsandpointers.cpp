#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
	// Iterate through a vector using iterators.
	// Then copy the vector into an array and iterate though it using pointers
	// Compare results

	const int n = 5;
	
	vector< int > x;
	for( int xi = 0 ; xi < n ; xi++ )
		x.push_back( xi );
	vector< int >::iterator i;
	vector< int >::reverse_iterator j;
	cout << "Forward iteration using iterators" << endl;
	for( i = x.begin() ; i != x.end() ; i++ )
		cout << *i << " ";
	cout << endl;
	cout << "Reverse iteration using iterators" << endl;
	for( j = x.rbegin() ; j != x.rend() ; j++ )
		cout << *j << " ";
	cout << endl;

	int *y = new int[n];
	memcpy( y, &x[0], n * sizeof(int) );

	int *p, *q;
	cout << "Forward iteration using pointers" << endl;
	for( p = y ; p < y + n ; p++ )
		cout << *p << " ";
	cout << endl;
	cout << "Reverse iteration using pointers" << endl;
	for( q = y + n - 1 ; y != NULL && q >= y ; q-- )
		cout << *q << " ";
	cout << endl;

	return 0;
}
