#include "ppp.hpp"
using namespace std;

int main()
{
	string input;
	string bad = "damn";
	bool state = true;
	while ( state ){
		cin >> input;
		if ( input == "q" )
			break;
		if ( input == bad )
			input = "BEEP";
		cout << input << ' ';

	}
	cout << '\n';
}
