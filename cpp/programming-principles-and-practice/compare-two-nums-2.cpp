#include "ppp.hpp"
using namespace std;

int main()
{
	// const double delta = 1.0/100;
	bool state = true;
	double a;
	double min = 0, max = 0;
	while(state){
		char state_in;
		cout << "do you want to start the program? (if yes, press anything except | )\n";
		cin >> state_in;
		if ( state_in == '|' )
			break;
		cin >> a;
		if( a <= min){
			cout << "the smallest so far = " << a << '\n';
			min = a;
		}
		else{
			if ( max <= a ){
				cout << "the largest so far = " << a << '\n';
				max = a;
			}
		}
	}
}
