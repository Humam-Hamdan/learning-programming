#include "ppp.hpp"
using namespace std;

int main()
{
	string prev;
	string curr;
	while ( cin >> curr ){
		if ( prev == curr )
			cout << "repeated word: " << curr << '\n';
		prev = curr;
	}
}
