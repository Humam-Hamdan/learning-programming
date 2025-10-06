
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

void inplaceSwap(int* a, int* b){
	*a = *a ^ *b;
	*b = *a ^ *b;
	*a = *a ^ *b;
	return;
}

int main(){
	int a = 8;
	int b = 10;
	printf("Before: %d , %d\n",a, b);
	inplaceSwap(&a, &b);
	printf("After: %d , %d\n", a, b);
}
