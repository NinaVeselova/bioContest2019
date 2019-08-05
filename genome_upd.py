Trans = {'A': 'GC*', 'R': '*G*', 'N': 'AA*', 'D': 'GA*', 'C': 'TG*', 'Q': 'CA*', 'E': 'GA*', 'G': 'GG*', 'H': 'CA*',
         'I': 'AT*', 'L': '*T*', 'K': 'AA*', 'M': 'ATG', 'F': 'TT*', 'P': 'CC*', 'S': '***','T': 'AC*', 'W': 'TGG',
         'Y': 'TA*', 'V': 'GT*', '$': 'T**'}
f = open('for_genome_upd.txt')
t = f.read()
t = t.split('\n')
t = t[1:]
t.sort(key = len)
print(t)
res = []
for i in range(len(t) - 1):
    d = 0
    for j in range(i + 1,len(t)):
        if t[j].find(t[i]) != -1:
            d = 1
            break
    if d == 0:
        res.append(t[i])
res.append(t[-1])
print(res)
mask = []
for i in res:
    c = ''
    for j in i:
        c = c + Trans[j]
    mask.append(c)
print(mask)
my_file = open('upd.txt','w')
for i in mask:
    my_file.write(i + '\n')

