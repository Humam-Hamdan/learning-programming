#include "ppp.hpp"
using namespace std;

int main()
{
	string input;
	cout << "Enter a string\n";
	cin >> input;
	for ( int i = 0; i < input.size(); i++ ){
		char c = char(input[i]);
		cout << c << '\t' << int(c) << '\n';
	}
}
