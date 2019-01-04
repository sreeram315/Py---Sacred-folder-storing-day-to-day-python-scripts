# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	word, kk, dic, answer, i = input(), int(input()), {}, '', 0
	for letter in word:
		try: 	dic[letter] += 1
		except: dic[letter] =  1
	letters = [letter for letter in word]
	letters.sort(reverse = True)

	for letter in letters:
		if dic[letter] >= kk and letter in word[i:]:
			ltimes 	= dic[letter]
			for _ in range(dic[letter]):
				answer 		+= letter
			while (ltimes > 0):
				if word[i] == letter: ltimes -= 1
				dic[word[i]] -= 1
				i += 1
				if i >= len(word):
					print(answer)
					exit()
	print(answer)


