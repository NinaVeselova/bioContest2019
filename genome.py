Trans = {'A': 'GCT', 'R': 'CGT', 'N': 'AAT', 'D': 'GAT', 'C': 'TGT', 'Q': 'CAA', 'E': 'GAA', 'G': 'GGT', 'H': 'CAT',
         'I': 'ATT', 'L': 'TTA', 'K': 'AAA', 'M': 'ATG', 'F': 'TTT', 'P': 'CCT', 'S': 'TCT','T': 'ACT', 'W': 'TGG',
         'Y': 'TAT', 'V': 'GTT', '$': 'TAA'}
f = open('for_genome.txt')
text = f.read()
text = text.split('\n')
text = text[1:]
text.sort(key = len)
print(text)
res = []
for i in range(len(text) - 1):
    d = 0
    for j in range(i + 1,len(text)):
        if text[j].find(text[i]) != -1:
            d = 1
            break
    if d == 0:
        res.append(text[i])
res.append(text[-1])
str1 = ''
for i in range(len(res)):
    str1 = str1 + res[i]
DNA = ''
for i in str1:
    DNA = DNA + Trans[i]
print(str1)
f = open('for_genome.txt')
t1 = f.read()
t1 = t1.split('\n')
t1 = t1[1:]
answer = []
for i in t1:
    k = str1.find(i) * 3 + 1
    answer.append(k)
my_file = open('gen6.txt','w')
my_file.write(DNA + '\n')
for i in answer:
    my_file.write(str(i) + ' +\n')
