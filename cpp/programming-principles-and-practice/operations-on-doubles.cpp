#include "ppp.hpp"
using namespace std;

int main() {
	double val1, val2;
	cout << "Enter val1 and val2: \n";
	cin >> val1 >> val2;
	cout << '\n';
	if (val1 > val2)
		cout << "val1 is bigger";
	else 
		if (val2 > val1)
			cout << "val2 is bigger";
		else
			cout << "val1 = val2l";
	cout << '\n';
	cout << "val1 + val2 = " << val1 + val2;
	cout << '\n';
	cout << "val1 - val2 = " << val1 - val2;
	cout << '\n';
	cout << "val1 * val2 = " << val1 * val2;
	cout << '\n';
	cout << "val1 / val2 = " << val1 / val2;
	cout << '\n';
}
