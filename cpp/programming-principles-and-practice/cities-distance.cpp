#include "ppp.hpp"
using namespace std;

int main()
{
	vector <double> distance;
	double min = 1, max = 0, sum = 0;
	for ( double dist; cin >> dist;  ){
		distance.push_back(dist);
		sum += dist;
	}
	for( int i = 1; i < distance.size(); i++){
		double delta = abs(distance[i] - distance[i-1]);
		if( delta < min )
			min = delta;
		else if ( delta > max)
			max = delta;
	}
	cout << "min distance = " << min << " , max distance = " << max << " , sum distance = " << sum << '\n';
}
