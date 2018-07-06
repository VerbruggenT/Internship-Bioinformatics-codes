f = open("C:\Python27\Doc\HGNC list.txt")

genes ={}

for line in f:
	if not 'HGNC ID	Approved Symbol	Approved Name	Previous Symbols	Synonyms	Ensembl ID(supplied by Ensembl)'in line:
		S = line.split('\t')
		genes[S[0]]=[]
		genes[S[0]].append(S[1])
		genes[S[0]].append(S[2])
		if not S[5][:-1] == '':
			genes[S[0]].append(S[5][:-1])
		for item in S[3].split(', '):
			if not item == '':
				genes[S[0]].append(S[3])
		for item in S[4].split(', '):
			if not item == '':
				genes[S[0]].append(S[4])


