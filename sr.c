#include<stdio.h>
int main()
{
	int a,y;
	a=0;
	while(1)
	{
	y=a;
	a++;
	if(a==15)
	a=0;
	printf("%d",y);

	}
}