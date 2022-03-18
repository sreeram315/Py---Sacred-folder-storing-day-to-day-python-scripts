#include<stdio.h>



int main(){
	int a = 0;
	long long is_parent = fork( );
	if(is_parent) {
		a = a+5;
		printf("%d %p \n", a, &a);
	}
	else {
		a = a - 5;
		printf("%d %p \n", a, &a);
	}
	if (!is_parent){
	printf("%d\n", a);
}
}