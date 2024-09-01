n = int(input())
word = []

for _ in range(n):
    word.append(input())

set_word = list(set(word))
sor_word = sorted(set_word, key= lambda x: (len(x), x))
print(*sor_word,sep='\n')