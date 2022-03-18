# proprietary to BEERA // DO NOT COPY
# Uses python3
import sys



def gold_bars(W, wt):
	n = len(wt)
	ans=[[0 for m in range(n+1)]for l in range(W+1)]
	for i in range(1,n+1):
		for w in range(1,W+1):
			ans[w][i] = ans[w][i-1]
			if wt[i-1] <= w :
				val = ans[w-wt[i-1]][i-1] + wt[i-1]
				if ans[w][i] < val:
					ans[w][i] = val
	return ans[W][i]



if __name__ == '__main__':

	W ,n = map(int,input().split())
	wt = list(map(int, input().split()))
	wt.sort()
	print(gold_bars(W, wt))