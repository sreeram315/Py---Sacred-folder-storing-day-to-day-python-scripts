# proprietary to BEERA // DO NOT COPY
if __name__ == '__main__':
    names, scores, dic = [], [], {}
    second_best = None
    for _ in range(int(input())):
        name = input()
        score = input()
        dic[name] = score
        scores.append(float(score))
    scores.sort()
    for i in range(1, len(scores)):
        if scores[i] != scores[0]:
            second_best = scores[i]
            break
    if second_best == None: second_best = [scores[0]]
    print('second best == ',second_best)
    print(dic)
    for key, value in dic.items():
    	print('comparing {} and {}'.format(value, second_best))
    	if float(value) == float(second_best): print(key)
        
        