# Напишите программу, удаляющую из 
# текста все слова содержащие "абв".


with open ('Python/Seminar5/DZ/my_text.txt', 'r', encoding='utf-8') as my_text:
    string=my_text.readline()
print(' '.join(list(filter(lambda x: not'абв' in x, string.split()))))