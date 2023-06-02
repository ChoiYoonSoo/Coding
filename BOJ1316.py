n = int(input())
cnt = 0

for i in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if word[index] in new_word:
                error = error+1
    if error == 0:
        cnt = cnt+1
print(cnt)
        
    