


#include<iostream>

int main(){
	int line_count = 0, num = 0;
	std::cin>>num;
	num = num-1;
	for(int i=0; i<= num; i++){
		line_count++;
		for(int j = 0; j < line_count; j++){
			std::cout<<line_count;
			if(j+1<line_count)
				std::cout<<"*";
		}
		std::cout<<"\n";
	}

	for(int i=0; i<= num; i++){
		for(int j = line_count; j > 0; j--){
			std::cout<<line_count;
			if(j-1>0)
				std::cout<<"*";
		}
		std::cout<<"\n";
		line_count--;
	}

}