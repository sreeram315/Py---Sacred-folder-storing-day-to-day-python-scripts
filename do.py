
Ts  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Hs  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Rs  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Es  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Ls  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Vs  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ns  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ws  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ys  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
num1=0; num2=0; num3=0

for T in Ts:
	for H in Hs:
		if len(set([T, H])) != 2: continue
		for R in Rs:
			if len(set([T, H, R])) != 3: continue
			for E in Es:
				if len(set([T, H, R, E])) != 4: continue
				for L in Ls:
					if len(set([T, H, R, E, L])) != 5: continue
					for V in Vs:
						if len(set([T, H, R, E, L, V])) != 6: continue
						for N in Ns:
							if len(set([T, H, R, E, L, V, N])) != 7: continue
							for W in Ws:
								if len(set([T, H, R, E, L, V, N, W])) != 8: continue
								for Y in Ys:
									if len(set([T, H, R, E, L, V, N, W, Y])) != 9: continue
									count += 1
									if count > 10000:
										print(f"{T} {H} {R} {E} {L} {V} {N} {W} {Y}")
										count = 0
									num1 = int(f'{str(T)}{str(H)}{str(R)}{str(E)}{str(E)}')
									num2 = int(f'{str(E)}{str(L)}{str(E)}{str(V)}{str(E)}{str(N)}')
									num3 = int(f'{str(T)}{str(W)}{str(E)}{str(N)}{str(T)}{str(Y)}')
									if (3*num1) + num2 == num3 and len(set([T, H, R, E, L, V, N, W, Y])) == 9:
										print("GOOT")
										print(f"{T} {H} {R} {E} {L} {V} {N} {W} {Y}")
										print(num1, num2, num3)
										exit()








