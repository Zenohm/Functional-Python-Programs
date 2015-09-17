ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
names = open('C:/Python34/p022_names.txt', 'r').read()
names = names.split(',')
names = [name.strip('"') for name in names]
names.sort()

def name_score(name):
    name = list(name)
    summation = sum([ALPHA.index(letter)+1 for letter in name])
    place = names.index(''.join(name))+1
    return summation * place

total_sum = 0
for n in names:
    total_sum += name_score(n)

total_sum

