import os


print(f"\nparent start, pid: {os.getpid()}\n")

i = os.fork()

if(i == 0):
	print(f"\nchild start ,pid: {os.getpid()}\n")
	print("child end\n\n")

else:
	print("Parent end\n\n")

print("PROGRAM END\n\n")
