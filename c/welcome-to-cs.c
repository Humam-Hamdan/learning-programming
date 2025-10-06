/*

this code if from this reddit post:

[here](https://www.reddit.com/r/programminghorror/comments/1kmmq3z/cisverysimpleandeasytolearn/).
*/

#include <stdio.h>

int main(){
	int arr[3] = {1, 42, 69};
	int what = *(&((0x40-64)[&(&(3[arr]))[-2]])-(-1));

	printf("%d\n", what);

	return 0;
}

/*

Solution:

First note that if a is a pointer and n is an integer then "a[n] == n[a] == *(a + n)" and that &* cancels out.

So start with :

&(&(3[arr]))[-2]     ,  Note: &(3[arr]) = arr + 3

&(arr + 3)[-2] = &*(arr + 3 - 2) = arr + 1

Next:

(0x40-64)[arr + 1] = 0[arr + 1] = *(arr + 1)

Finally put the rest in:

*(&(*(arr+1))-(-1)) = *(&*(arr +1) + 1) = *(arr + 2) = 69

*/
