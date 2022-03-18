# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.stdin = open("i.txt")
# Enter your code here. Read input from STDIN. Print output to STDOUT
class String:
    def __init__(self, string): 
        self.string = string
    
    def display(self):
        print(self.string)

    def less_than(self, str2):
        str1 = str(self.string)
        return str1 < str2

def sort_them(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i].string > arr[j].string : arr[i], arr[j] = arr[j], arr[i]
    return arr
        
def sorted_insert(arr, string):
    ind = 0
    while(arr[ind].string < string): ind += 1
    arr.append('')
    for i in range(len(arr)-1, ind, -1): arr[i] =arr[i-1]
    arr[ind] = String(string)
    return arr

def delete_string(arr, string):
    for i in range(len(arr)):
        if str(arr[i].string) == str(string):
            ind = i
            break
    del arr[ind]
    return arr


def max_length_string(arr):
    l = -1; ans = ''
    for x in arr:
        if(len(x.string) > l):
            ans = x.string
            l = len(x.string) 
    return ans

if __name__ == '__main__':
    arr = []; n = int(input());
    for _ in range(n):
        arr.append(String(input()))
    arr = sort_them(arr)
    for x in arr:
        x.display()
    print('')
    input()
    arr = sorted_insert(arr, input())
    for x in arr: x.display()
    print(''); input()
    string = input()
    arr = delete_string(arr, string)
    for x in arr: x.display()
    print('')
    for x in arr: print(x.string, len(x.string))
    print('')
    ans = max_length_string(arr)
    print(ans)