#include "ppp.hpp"
using namespace std;

int main()
{
	double mile = -1;
	cout << "Input the amount of miles: ";
	cin >> mile;
	double km = mile * 1.609;
	cout << mile << "miles correspond to about " << km << "kilometers";
}
