text = 'AAAAABBRRRR'
count=1
new_str=[]
text2=''
text3=''
for i in range(len(text)-1):
    if text[i]==text[i+1]:
        count+=1
        text2=str(count)+text[i]
    else:
        text2= str(count)+text[i]
        count = 1
        text3+=text2
text3+=text2
print(text3)