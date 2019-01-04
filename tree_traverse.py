# proprietary to BEERA // DO NOT COPY
# python3


import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    self.result1, self.result2, self.result3 = [], [], []
     


  def in_order(self, N):
    if self.left[N] == -1 and self.right[N] == -1:
      self.result1.append(self.key[N])
      return
    if self.left[N] != -1: self.in_order(self.left[N])
    self.result1.append(self.key[N])
    if self.right[N] != -1: self.in_order(self.right[N])
    return self.result1


  def pre_order(self, N):
    self.result2.append(self.key[N])
    if self.left[N] != -1: self.pre_order(self.left[N])
    if self.right[N] != -1: self.pre_order(self.right[N])
    return self.result2

  def post_order(self, N):
    if self.left[N] != -1: self.post_order(self.left[N])
    if self.right[N] != -1: self.post_order(self.right[N])
    self.result3.append(self.key[N])
    return self.result3
    
   

def main():
  T     =   TreeOrders()
  T.read()
  arr   = T.in_order(0)
  for i in arr: print(i, end=' ')
  print('')
  arr   = T.pre_order(0)
  for i in arr: print(i, end=' ')
  print('')
  arr   = T.post_order(0)
  for i in arr: print(i, end=' ')
threading.Thread(target=main).start()




















