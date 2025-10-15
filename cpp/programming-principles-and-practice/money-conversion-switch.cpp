#include "ppp.hpp"
using namespace std;

int main()
{
	constexpr double usd_to_jpy = 152.6877096;
	constexpr double usd_to_nok = 9.987529027;
	constexpr double usd_to_gbp = 0.7457641696;
	constexpr double udf_to_chf = 0.8002924228;
	double amount = 0;
	double amount_curr = 0;
	char unit_in, unit_out;
	cout << "Please enter an amount followed by its unit (jpy, nok, gbp, usd, chf) and then the desired unit\n";
	cin >> amount >> unit_in >> unit_out;
	switch(unit_in){
		case 'jpy':
			amount_curr = amount / usd_to_jpy;
			switch(unit_out){
				case 'nok':
					cout << amount << " JPY = " << amount_curr * usd_to_nok << " NOK\n";
					break;
				case 'gbp':
					cout << amount << " JPY = " << amount_curr * usd_to_gbp << " GBP\n";
					break;
				case 'usd':
					cout << amount << " JPY = " << amount_curr << " USD\n";
					break;
				default : cout << "IDK!\n"; 
			}
			break;
		case 'nok':
			amount_curr = amount / usd_to_nok;
			switch(unit_out){ 
				case 'jpy':
					cout << amount << " NOK = " << amount_curr * usd_to_nok << " JPY\n";
					break;
				case 'gbp':
					cout << amount << " NOK = " << amount_curr * usd_to_gbp << " GBP\n";
					break;
				case 'usd':
					cout << amount << " NOK = " << amount_curr << " USD\n";
					break;
				default :
					cout << "IDK!\n"; 
					break;
			}
			break;
		case 'gbp':
			switch(unit_out){ 
				amount_curr = amount / usd_to_gbp;
				case 'nok':
					cout << amount << " GBP = " << amount_curr * usd_to_nok << " NOK\n";
					break;
				case 'jpy':
					cout << amount << " GBP = " << amount_curr * usd_to_jpy << " JPY\n";
					break;
				case 'usd':
					cout << amount << " GBP = " << amount_curr << " USD\n";
					break;
				default :
					cout << "IDK!\n"; 
					break;
			}
			break;
		case 'usd':
			switch(unit_out){ 
				amount_curr = amount;
				case 'nok':
					cout << amount << " USD = " << amount_curr * usd_to_nok << " NOK\n";
					break;
				case 'gbp':
					cout << amount << " USD = " << amount_curr * usd_to_gbp << " GBP\n";
					break;
				case 'jpy':
					cout << amount << " USD = " << amount_curr * usd_to_jpy << " JPY\n";
					break;
				default :
					cout << "IDK!\n"; 
					break;
			}
			break;
		default:
			cout << "IDK what's that!";
			break;
	}




}
