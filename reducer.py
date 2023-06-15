import sys
word_dict={}
for line in sys.stdin:
    word, count = line.split('\t',1)
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

for word, count in word_dict.items():
    print(f'{word}\t{count}')