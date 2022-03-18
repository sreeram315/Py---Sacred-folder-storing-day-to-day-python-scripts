#include<bits/stdc++.h>
using namespace std;

int main() {
    int r = 3;int c = 3;
    int a[3][3] = { {1,2,3},
                    {4,5,6},
                    {7,8,9}
                };
    int row1=0, col1=0, row2=r-1, col2=c-1;
    int i;

    while(row1<=row2 && col1<=col2){

        if(row1<=row2){
            for(i=col1;i<=col2;i++)
                cout<<a[row1][i]<<" ";
            row1++;
        }
        if(col1<=col2){
            for(i=row1;i<=row2;i++)
                cout<<a[i][col2]<<" ";
            col2--;
        }
        if(row1<=row2){
            for(i=col2;i>=col1;i--)
                cout<<a[row2][i]<<" ";
            row2--;
        }
        if(col1<=col2){
            for(i=row2;i>=row1;i--)
                cout<<a[i][col1]<<" ";
            col1++;
        }

    }
    return 0;
}