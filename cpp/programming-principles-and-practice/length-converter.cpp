#include "ppp.hpp"
using namespace std;

int main()
{
	// const double delta = 1.0/100;
	bool state = true;
	double a = 0, sum = 0, num = 0;
	double min = 0, max = 0;
	char unit;
	vector <double> all_values;
	while(state){
		char state_in;
		cout << "do you want to start the program? (if yes, press anything except | )\n";
		cin >> state_in;
		if ( state_in == '|' )
			break;
		cout << "enter a number with a unit, c = cm, i = in, f = ft, m = m\n";
		cin >> a >> unit;
		double converted_a = 0;
		switch(unit){
			case 'c':
				converted_a = a;
				break;
			case 'm':
				converted_a = a * 100;
				break;
			case 'f':
				converted_a = a * 2.54 * 12;
				break;
			case 'i':
				converted_a = a * 2.54;
				break;
			default:
				cout << "IDK!\n";
				break;
		}
		sum += converted_a;
		num += 1;
		all_values.push_back(converted_a);
		if( converted_a <= min){
			cout << "the smallest so far = " << converted_a << "cm\n";
			min = converted_a;
		}
		else{
			if ( max <= converted_a ){
				cout << "the largest so far = " << converted_a << "cm\n";
				max = converted_a;
			}
		}
	}
	cout << "no. of items = " << num << ", sum of items = " << sum << "cm\n";
	ranges::sort(all_values);
	for ( double v : all_values )
		cout << v << "cm, ";
	cout << '\n';
}
