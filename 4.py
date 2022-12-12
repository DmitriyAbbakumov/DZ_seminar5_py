# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open ('Python/Seminar5/DZ/rleinput.txt', 'r') as data:
    string=data.readline()

def rle(text):
    encoding=''
    i = 0
    while i < len(text):
        count = 1
 
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + text[i]
        i = i + 1
    return encoding
 
# s = 'ABBCCCD'
d=rle(string)
print(rle(string))

def decoding_rle(s:str):
    count = ''
    str_decode = ''
    for char in s:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode
s1=decoding_rle(d)
print(decoding_rle(d))

with open('Python/Seminar5/DZ/rleoutput.txt', 'w') as file:
    file.write(s1)