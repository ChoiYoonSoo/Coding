n = int(input())
i = 0
cnt = 0
user = {}
while(i < n):
    chat = input()
    
    if chat == 'ENTER':
        for key,value in user.items():
            if value == 1:
                cnt += 1
        user = {}
    else:
        if chat not in user:
           user[chat] = 1 
    i += 1
for key,value in user.items():
    if value == 1:
        cnt += 1
        
print(cnt)