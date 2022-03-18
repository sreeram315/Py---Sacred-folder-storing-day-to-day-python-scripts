

#include<iostream>

int main(){
	int length, last_num;
	std::cin>>length;
	int line_count = 0, print_count = 0;
	for(int i = 0; i < length; i++){
		line_count++;
		if(line_count%2==0){
			last_num = line_count + print_count;
			// std::cout<<"LAST IS :"<<last_num<<"\n";
			for(int j = 0; j< line_count; j++){
				std::cout<<last_num--;
				print_count++;
				if(j+1<line_count)
					std::cout<<"*";
				
			}
			std::cout<<"\n";
			continue;
		}
		for(int j=0; j< line_count; j++){
			std::cout<<++print_count;
			if(j+1<line_count)
				std::cout<<"*";
		}
		std::cout<<"\n";
	}

	
}

if(count==0 && done[a[i]]==0){
	print(a[i]);
	done[a[i]] = 1;
}