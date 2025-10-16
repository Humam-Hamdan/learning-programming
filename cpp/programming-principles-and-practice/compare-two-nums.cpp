#include "ppp.hpp"
using namespace std;

int main()
{
	bool state = true;
	while(state){
		char state;
		cout << "do you want to start the program? (if yes, press anything except | )\n";
		cin >> state;
		if ( state == '|' )
			break;
		double a, b;
		cin >> a >> b;
		const double delta = 1.0/100;
		if( a < b){
			cout << "the smaller value is = " << a << " ,and the larger is = " << b << '\n';
			if( (b - a) < delta )
				cout << "they are almost equal\n";
		}
		else{
			if ( b < a ){
			cout << "the smaller value is = " << b << " ,and the larger is = " << a << '\n';
				if( (a - b) < delta )
					cout << "they are almost equal\n";
			}
			else
				cout << "they are the same value = " << a << '\n';
		}

	}
}
