#include "ppp.hpp"
using namespace std;

int main()
{
	vector <double> temps = {};
	for (double temp; cin >> temp; )
		temps.push_back(temp);

	double sum = 0;
	for (double x : temps)
		sum += x;
	cout << "avg = " << sum/temps.size() << '\n';

	ranges::sort(temps);
	cout << "median = " << temps[temps.size()/2] << '\n';
}
