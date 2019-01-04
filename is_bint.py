#python3
# proprietary to BEERA // DO NOT COPY

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size



# def main():
#   nodes = int(sys.stdin.readline().strip())
#   tree = []
#   for i in range(nodes):
#     tree.append(list(map(int, sys.stdin.readline().strip().split())))
#   if IsBinarySearchTree(tree):
#     print("CORRECT")
#   else:
#     print("INCORRECT")




class IsBinaryTree():
  def read(self):
    self.n = int(sys.stdin.readline())
    if self.n == 0:
      print('CORRECT')
      exit()
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def no_left(self, N):
    if self.left[N] == -1: return True
  def no_right(self, N):
    if self.right[N] == -1: return True
  def no_children(self, N):
    if self.left[N] == -1 and self.right[N] == -1: return True

  def post_order(self, N,kee, logic = ''):
    self.result = []
    # if self.right[N] != -1 and self.left[N] != -1: print(f'N = {self.key[N]}; lc = {self.key[self.left[N]]}, rc = {self.key[self.right[N]]}')
    if self.left[N] != -1:
      if not self.post_order(self.left[N], kee, logic = logic): return False
    if self.right[N] != -1:
      if not self.post_order(self.right[N], kee, logic = logic): return False
    if logic == 'less' and self.key[N] > kee: return False
    if logic == 'more' and self.key[N] < kee: return False
    return True

  # def left_okay(self, N):
  #    if no_children(N):
  #     return True

  def all_of_N_are_less_than_kee(self, N, kee):
    self.result = []
    result = self.post_order(N, kee, logic = 'less')
    # print(self.key[N] ,result)
    return result

  def all_of_N_are_more_than_kee(self, N, kee):
    self.result = []
    result = self.post_order(N, kee, logic = 'more')
    # print(self.key[N], result)
    return result

  # def all_children(index, kee, logic):
  #   if self.left[N] == -1: l = True
  #   if self.right[N] == -1: r = True
  #   if l and r: return True
  #   if self.left[N] != -1: l = self.all_children(self.left[N], kee, logic=logic)
  #   if self.right[N] != -1: r = self.all_children(self.right[N], kee, logic=logic)



  def is_binary_tree(self, N):
    if self.no_children(N):
      return True                     
    l = (not self.no_left(N)) and self.all_of_N_are_less_than_kee(self.left[N], self.key[N]) and self.is_binary_tree(self.left[N])
    r = (not self.no_right(N)) and self.all_of_N_are_more_than_kee(self.right[N], self.key[N]) and self.is_binary_tree(self.right[N])
    if self.no_left(N): l = True
    if self.no_right(N): r = True
    return (l and r)





def main():
  T = IsBinaryTree()
  T.read()
  if T.is_binary_tree(0): print('CORRECT')
  else: print('INCORRECT')

threading.Thread(target=main).start()

















