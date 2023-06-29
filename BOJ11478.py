word = input()
count = set()
for i in range(len(word)):
    for j in range(0,len(word)):
        count.add(word[j:j+i])
        
print(len(count))