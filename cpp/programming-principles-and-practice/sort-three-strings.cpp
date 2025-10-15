#include "ppp.hpp"
using namespace std;

int main()
{
	string x1, x2, x3;
	cout << "enter the strings: \n";
	cin >> x1 >> x2 >> x3;
	if ( x1 == x2 && x2 == x3 )
		cout << x1 << ' ' << x2 << ' ' << x3;
	if (x1 < x2) {
		if (x1 < x3) {
			if (x2 < x3) {
				cout << x1 << ' ' <<  x2 << ' ' << x3;
			}
			else
				cout << x1 << ' ' <<  x3 << ' ' << x2;
		}
		else
			cout << x3 << ' ' <<  x1 << ' ' << x2;
	}
	else {
		if (x1 < x3) 
			cout << x2 << ' ' << x1 << ' ' << x3;
		
		else
			if (x2 < x3)
				cout << x2 << ' ' << x3 << ' ' << x1;
			else
				cout << x3 << ' ' << x2 << ' ' << x1;
		
	}
	cout << '\n';
}
