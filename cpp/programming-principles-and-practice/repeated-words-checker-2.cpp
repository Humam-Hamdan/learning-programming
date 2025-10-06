#include "ppp.hpp"
using namespace std;

int main()
{
	int no_words = 0;
	string prev;
	string curr;
	while ( cin >> curr ){
		++no_words;
		if ( prev == curr )
			cout <<  "word number " << no_words << " repeated: " << curr << '\n';
		prev = curr;
	}
}
