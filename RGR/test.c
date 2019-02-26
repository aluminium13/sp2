
#include <stdio.h>

int main(void){
	int b = 0;
	int a[4] = {0,0,0,0};
	int n = 0;
	__asm
	{

		mov edx, 3
		push edx

		pop edx
		mov n, edx

		mov edx, n
		push edx

		pop edx
		mov [a + 4 * 2], edx ; write element by index to array

		mov eax, [a + 4 * 2] ; get element by index from array
		push eax

		pop edx
		mov [a + 4 * 3], edx ; write element by index to array

		mov eax, [a + 4 * 3] ; get element by index from array
		push eax

		pop edx
		mov b, edx
	}

	printf("n=%d\n", n);
	getchar();
}
