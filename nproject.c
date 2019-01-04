#include<stdio.h>
int main()
{
	int a,rst,y,count;
	count=0;
	rst=0;
	int i=0;
	scanf("%d",&a);
	
	if(rst==1)
		printf("0");
	else
	{
		for(i=2;i<a;i++)
		{
			if(a%i==0)
				count++;
		}


	}

	
	if(count>0)
		printf("not prime number ");
	else
		printf("prime number");
}