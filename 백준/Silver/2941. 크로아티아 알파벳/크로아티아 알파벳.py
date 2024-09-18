cro = ['dz=','z=','c=','c-','d-','lj','nj','s=']
ans = 0
word = input()
for i in cro:
    if i in word:
        ans += word.count(i)
        word = word.replace(i,' ')
print(ans+ len(word.replace(' ','')))  