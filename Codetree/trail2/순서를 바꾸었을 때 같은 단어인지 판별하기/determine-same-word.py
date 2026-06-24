word1 = input()
word2 = input()

# Please write your code here.
list_word1 = sorted(list(word1))
list_word2 = sorted(list(word2))

flag = True
for i in range(len(list_word1)):
    if len(list_word1) != len(list_word2):
        flag=False
        break
    if list_word1[i] != list_word2[i]:        
        flag = False

if flag:
    print('Yes')
else:
    print('No')