// # proprietary to BEERA // DO NOT COPY

#include<stdio.h>

int main(){
	int y, clk, rst = 1, ps, ns;

	while(1){
		if (rst){
			y = 0;
			ps = 0;
			ns = 0;
			rst = 0;
		}


		else{

			switch(ps){
				case 0:
					ns = 1;
					break;
				case 1:
					ns = 2;
					break;
				case 2:
					ns = 3;
					break;
				case 3:
					ns = 4;
					break;
				case 4:
					ns = 5;
					break;
				case 5:
					ns = 6;
					break;
				case 6:
					ns = 7;
					break;
				case 7:
					ns = 8;
					break;
				case 8:
					ns = 9;
					break;
				case 9:
					ns = 10;
					break;
				case 10:
					ns = 11;
					break;
				case 11:
					ns = 12;
					break;
				case 12:
					ns = 13;
					break;
				case 13:
					ns = 14;
					break;
				case 14:
					ns = 15;
					break;
				case 15:
					ns = 0;
					break;
				default:
					printf("something wrong");

			}

			ps = ns;
			y = ps;

			printf("%d ",y);
		}
		
	}
}
