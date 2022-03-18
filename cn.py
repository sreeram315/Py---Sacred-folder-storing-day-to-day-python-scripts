import os

files = os.listdir(".")
# print(files)
num = 1
for filename in os.listdir("."):
	if not filename.startswith(".") and not filename.startswith("cn"):
		ext = filename.split('.')[1]
		os.rename( filename,  str(num) + '.' + f'{ext}')
		num += 1

# for subdir, dirs, files in os.walk("."):
# 	if subdir == '.': continue
# 	os.chdir(os.getcwd() + subdir[1:])
# 	print(os.getcwd())
# 	for filename in os.listdir("."):
# 		if filename.startswith("Seinfeld"):
# 			ext = filename.split('.')[1]
# 			os.rename( str(num) + '.' + f'{ext}')
# 			num += 1
# 	os.chdir('..')
#     # for file in files:
#     #     print(os.path.join(subdir, file))