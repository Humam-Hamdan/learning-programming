#include "ppp.hpp"
using namespace std;

int main()
{
	int x = -1;
	cout << "enter the number: ";
	cin >> x;
	if ( x % 2 == 0 )
		cout << "the value " << x << " is even\n";
	else
		cout << "the value " << x << " is odd\n";
}
