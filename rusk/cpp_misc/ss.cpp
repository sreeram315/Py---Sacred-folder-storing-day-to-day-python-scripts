#include <bits/stdc++.h>
#include "/Users/sreerammaram/Desktop/CC/genfuncs.h"
using namespace std;


string highestValuePalindrome(string s, int n, int k) {
    unordered_set<int>needs;
    for(int i = 0; i < (n/2); i++){
        if(s[i] != s[n-1-i])
            needs.insert(i);
        if((n%2==1) && i == (n/2) && (s[i] != '9'))
            needs.insert(i);
    }
    if(needs.size() > k)
        return "-1";

    // cout << endl;
    // printf("NEEDS: \t");
    // print(needs);
    int extras = k-needs.size();
    // printf("\nextras = %lu\n", k-needs.size());
    int i = 0;
    while(extras && i<(n/2)){
        if(s[i] == '9' && s[n-i-1] == '9'){
            i++; continue;
        }
        if(needs.find(i) != needs.end()){
            if(s[i] != '9' && s[n-i-1] != '9')
                extras -= 1;
            // printf("Erasing i = %d\n", i);
            needs.erase(i);
        }
        // else if((s[i] == '9' && s[n-i-1] != '9') || (s[i] != '9' && s[n-i-1] == '9')){
        //     printf("SErasing i = %d\n", i);
        //     needs.erase(i);
        //     extras -= 1;
        // }
        else if(extras > 1)
            extras -= 2;
        else
            break;
        s[i] = s[n-i-1] = '9';
        i += 1;
    }
    // cout << endl;
    // cout << s << endl;
    // printf("NEEDS: \t");
    // print(needs);
    // printf("\nextras = %d\n", extras);
    // cout << endl << endl;

    for(auto& x: needs){
        s[x] = s[n-x-1] = max(s[x], s[n-x-1]);
    }

    if(extras && (n%2)==1){
        s[n/2] = '9';
    }


    return s;
}


int main(){
    cout << endl << highestValuePalindrome("912471", 6, 0) << " " << 0;
    cout << endl << highestValuePalindrome("912471", 6, 1) << " " << 1;;
    cout << endl << highestValuePalindrome("912471", 6, 2) << " " << 2;;
    cout << endl << highestValuePalindrome("912471", 6, 3) << " " << 3;;
    cout << endl << highestValuePalindrome("912471", 6, 4) << " " << 4;;
    cout << endl << highestValuePalindrome("912471", 6, 5) << " " << 5;;
    cout << endl << highestValuePalindrome("912471", 6, 6) << " " << 6;;
    cout << endl << highestValuePalindrome("912471", 6, 7) << " " << 7;;
    cout << endl << highestValuePalindrome("912471", 6, 1298419284) << endl;

    cout << endl << endl;
    return 0;
}

