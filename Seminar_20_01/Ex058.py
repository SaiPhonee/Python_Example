def delete(text):
    str = text.split(' ')
    new_str=[]
    temp = 'абв'
    for i in range(len(str)):
        if not temp in str[i]:
            new_str.append(str[i])
    return new_str

text1 = '1аббв 2абв 3апдвь 4валти 5ваабвлдпт 6авьба 7абвав'
text2=' '.join(delete(text1))
print(text2)
