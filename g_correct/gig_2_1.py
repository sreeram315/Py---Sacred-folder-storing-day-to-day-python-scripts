# proprietary to BEERA // DO NOT COPY
word = str(input())
k = int(input())
dic = {}
answer = ''
point = 0
debug = False

for letter in word:
	try: dic[letter] += 1
	except: dic[letter] = 1

letters = [letter for letter in word]

letters.sort()
letters.reverse()

if debug: print(dic,'\n',letters)

for letter in letters:
	if debug: print('main loop for ',letter)
	if dic[letter] >= k:
		for i in range(dic[letter]):
				answer += letter
		count = 0
		for i in range(point, len(word)):
			if count < dic[letter]:
				if word[i] == letter: count += 1
				if debug: print('removing',word[i])
				dic[word[point]] -= 1
				point += 1
				if point >= len(word):
					print(answer)
					exit()


