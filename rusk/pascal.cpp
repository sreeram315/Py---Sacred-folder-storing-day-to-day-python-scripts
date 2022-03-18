#include <iostream>

int main()
{
    int rows = 5, num = 1;
    for(int i = 0; i < rows; i++)
    {
        for(int spacing = 1; spacing <= rows - i; spacing++)
            std::cout <<" ";
        for(int j = 0; j <= i; j++)
        {
            if (i == 0 || j == 0) num = 1;
            else num = num*(i-j+1)/j;

            std::cout << num << " ";
        }
        std::cout << "\n";
    }
}