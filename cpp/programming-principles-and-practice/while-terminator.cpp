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
		int a, b;
		cin >> a >> b;
		cout << "a = " << a << " , b = " << b << '\n';
	}
}
