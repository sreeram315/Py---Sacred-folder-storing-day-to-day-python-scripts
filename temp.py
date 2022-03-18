''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    arr = [1, 1]
    i = 2
    K = int(input())
    divi = 1
    flag = True
    for i in range(2, K+2, 2):
        temp = arr[i-1] + arr[i-2]
        # print(f'==. {temp}')
        arr.append(int(temp))
        # print(f'++ {arr[i]}')
        temp = arr[i]/divi
        # print(f'--{temp}')
        arr.append(int(temp))
        if flag: divi +=1
        flag = not flag
    for i in range(K):
        print(arr[i], end = ' ')


 # Write code here 
N = int(input())
main()

