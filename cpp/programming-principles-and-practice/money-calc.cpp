#include "ppp.hpp"
using namespace std;

int main()
{
	int penny = 0, nickel = 0 , dime = 0, quarter = 0, half_dollar = 0, dollar = 0;

	cout << "Enter your pennies (1 cent), nickles (5 cents), dimes (10 cents), quarters (25 cents), half dollars (50 cents), and dollars one after the other, if you don't have for a specific type then write a simple 0\n";
	cin >> penny >> nickel >> dime >> quarter >> half_dollar >> dollar;
	cout << "you have " << penny << " pennies.\n" ;
	cout << "you have " << nickel << " nickels.\n" ;
	cout << "you have " << dime << " dimes.\n" ;
	cout << "you have " <<  half_dollar << " half dollars.\n" ;
	cout << "you have " <<  dollar << " dollar.\n" ;
	cout << "you have " << penny + ( 5 * nickel ) + ( 10 * dime ) + ( 25 * quarter ) + ( 50 * half_dollar ) + ( 100 * dollar ) << " cents in total.\n" ;
}
