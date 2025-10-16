#include "ppp.hpp"
using namespace std;

int main()
{
	vector <double> temps;
	for( double temp; cin >> temp; ){
		temps.push_back(temp);
	}

	double sum = 0;
	for( double x: temps)
		sum += x;
	cout << "avg = " << sum / temps.size() << '\n';

	ranges::sort(temps);
	if( temps.size() % 2 == 0 ){
		double mid = floor(temps.size() / 2);
		cout << "median = " << (temps[mid] + temps[mid - 1]) / 2 << '\n';
	}
	else
		cout << "median = " << temps[temps.size() / 2] << '\n';

}
