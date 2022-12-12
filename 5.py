# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]    
 
found=[]
for index in lst[::-1]:        
    for index_1 in found[:]:
        if index < index_1[0]:
            found.append([index]+index_1)
    found.append([index])
found.sort()
 
for index in range (len(found[:][:])):
    if len(found[index][:]) == 1:
        del found[index][:]
lst_1 = (list((filter(None, found))))
 
for index in range (len(lst_1[:][:])):
    print (lst_1[index][:])