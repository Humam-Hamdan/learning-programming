#include "ppp.hpp"
using namespace std;

int main()
{
	string num;
	cout << "enter the number in spelling: \n";
	cin >> num;
	if ( num == "zero" )
		cout << num << " is " << 0 << '\n';
	
	else{
		if ( num == "one" )
			cout << num << " is " << 1 << '\n';
		else{
			if ( num == "two" )
				cout << num << " is " << 2 << '\n';
			else{
				if ( num == "three" )
					cout << num << " is " << 3 << '\n';
				else{
					if ( num == "four" )
						cout << num << " is " << 4 << '\n';
					else
						cout << "not a number i know!\n";
				}
			}
		}
	}
}
