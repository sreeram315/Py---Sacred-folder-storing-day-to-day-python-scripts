// # proprietary to BEERA // DO NOT COPY
#include<iostream>
#include<cmath>



int main(){
	long long n = 0, ultimate_sum = 0, modulo = pow(10,7)+9;
	std::cin >> n;
	long long cost[n], cost_main[n], cost_sum[n];
	for(int i = 0; i < n; i++)
		std::cin >> cost[i];

	cost_main[0] = cost[0];
	for(long long i = 1; i < n; i++)
		cost_main[i] = cost[i] + cost_main[i-1];
	
	for( long long j = 0; j < n; j++){
		if (j > 0){
			for( long long k = j; k < n; k++){
				cost_sum[k] = cost_main[k] - cost_main[j-1];
			}
		}
		else{
			for(long long k = 0; k < n; k++){
				cost_sum[k] = cost_main[k];
			}
		}
		for(long long k = j; k < n; k++){
			ultimate_sum += cost_sum[k] * cost[k];
		}
	}
	
	std:: cout << ultimate_sum % modulo;
}
