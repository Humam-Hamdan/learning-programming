#include "ppp.hpp"
using namespace std;

int main()
{
	double x1 = -1;
	double x2 = -1;
	string operation;
	cout << "enter the operation then the numbers: \n";
	cin >> operation >> x1 >> x2;

	if ( operation == "+" || operation == "plus" ){
		cout << x1 << " plus " << x2 << " = " << x1 + x2 << '\n';
	}
	else{
		if ( operation == "-" || operation == "minus" ){
			cout << x1 <<  " minus " << x2 << " = " << x1 - x2 << '\n';
		}
		else {
			if ( operation == "*" || operation == "mul" ){
				cout << x1 <<  " mul " << x2 << " = " << x1 * x2 << '\n';
				}
			else{
				if (operation == "/" || operation == "div") {
					cout << x1 << " div " << x2 << " = " << x1 / x2 << '\n';
					}
				}
		}
	}
}
