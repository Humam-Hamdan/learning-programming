#include "ppp.hpp"
using namespace std;

int main() {
	int val1, val2;
	cout << "Enter val1 and val2: \n";
	cin >> val1 >> val2;
	if (val1 > val2)
	cout << "val1 is bigger\n";
	else if (val2 > val1)
	cout << "val2 is bigger\n";
	else
	cout << "val1 = val2l";
	cout << "\nval1 + val2 = " << val1 + val2;
	cout << "\nval1 - val2 = " << val1 - val2;
	cout << "\nval1 * val2 = " << val1 * val2;
	cout << "\nval1 / val2 = " << val1 / val2;
	cout << "\nval1 % val2 = " << val1 % val2;
	cout << '\n';
}
