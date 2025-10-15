// #include "ppp.hpp"
#include <iostream>

using namespace std;

int main()
{
	constexpr double usd_to_jpy = 152.6877096;
	constexpr double usd_to_nok = 9.987529027;
	constexpr double usd_to_gbp = 0.7457641696;
	double amount = 0;
	double amount_curr = 0;
	char unit_in, unit_out;
	cout << "Please enter an amount followed by its unit (y, k, p, u) and then the desired unit\n";
	cin >> amount >> unit_in >> unit_out;
	if ( unit_in == 'y' ){
		amount_curr = amount / usd_to_jpy;
		if ( unit_out == 'k' )
			cout << amount << " JPY = " << amount_curr * usd_to_nok << " NOK\n";
		else if ( unit_out == 'p' )
			cout << amount << " JPY = " << amount_curr * usd_to_gbp << " GBP\n";
		else if ( unit_out == 'u' )
			cout << amount << " JPY = " << amount_curr << " USD\n";
	}
	else if ( unit_in == 'k' ){
		amount_curr = amount / usd_to_nok;
		if ( unit_out == 'y' )
			cout << amount << " NOK = " << amount_curr * usd_to_nok << " JPY\n";
		else if ( unit_out == 'p' )
			cout << amount << " NOK = " << amount_curr * usd_to_gbp << " GBP\n";
		else if ( unit_out == 'u' )
			cout << amount << " NOK = " << amount_curr << " USD\n";
	}

	else if ( unit_in == 'p' ){
		amount_curr = amount / usd_to_gbp;
		if ( unit_out == 'k' )
			cout << amount << " GBP = " << amount_curr * usd_to_nok << " NOK\n";
		else if ( unit_out == 'y' )
			cout << amount << " GBP = " << amount_curr * usd_to_jpy << " JPY\n";
		else if ( unit_out == 'u' )
			cout << amount << " GBP = " << amount_curr << " USD\n";
	}
	else if ( unit_in == 'u' ){
		amount_curr = amount;
		if ( unit_out == 'k' )
			cout << amount << " USD = " << amount_curr * usd_to_nok << " NOK\n";
		else if ( unit_out == 'p' )
			cout << amount << " USD = " << amount_curr * usd_to_gbp << " GBP\n";
		else if ( unit_out == 'y' )
			cout << amount << " USD = " << amount_curr * usd_to_jpy << " JPY\n";
	}
	else
		cout << "IDK what's that!";

}
