
# -*- coding: cp1251 -*-
#1

#def fahrenheit_translation (сelsius):
    
#    return  (x*1.8+32 for x in сelsius)

#сelsius_list = [39.2, 36.5, 37.3, 37.8]

#fahrenheit_list = map(lambda x: x*1.8+32,сelsius_list)
#print(list(fahrenheit_list))

#fahrenheit_list = (x*1.8+32 for x in сelsius_list)
#print(list(fahrenheit_list))

#fahrenheit_list = fahrenheit_translation(сelsius_list)
#print(list(fahrenheit_list))

#2
#def len_str(str_list):

#    return (len(x) for x in str_list)

#str_list = ['Tina', 'Raj', 'Tom']

#len_str_list = len_str(str_list)
#print(list(len_str_list))

#len_str_list =map(lambda x: len(x), str_list)
#print(list(len_str_list))

#3
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = (sentence.count('капитан') for sentence in sentences)

print(sum(cap_count))

#4
#X = [2, 3, 4]
#Y = [10, 11, 12]

#degree = map(lambda x,y: x**y, X,Y)
#print(list(degree))

#degree = (x**y for x,y in zip(X,Y))
#print(list(degree))

#5
#def f(n):
#    for x in range(n+1):
#        if x==0:
#            yield -10
#        elif x%3==0:
#            yield x/5+93
#        else:
#            yield 45

#def f1(n):
#    for x in range(n+1):
#        if x==0:
#            yield -10
#        elif x%3==0:
#            yield 45
#        elif x%5==0:
#            yield x/5+93
#        else:
#            yield x/2

#print(list(f1(15)))
#print(list(f(7)))

#6
#def largest_histogram(dano):
#    n = 0
#    answer  = len(dano)
#    if len(dano)>1:
#        for i in dano[:-1]:
#                count = 1
#                n+=1
#                if i>1:
#                    for j in dano[n:]:
#                        if j>=i:
#                            count+=1
#                        else: break
#                    if answer < i * count:
#                        answer = i * count
#        n = -1
#        for i in dano[:-len(dano):-1]:
#                count = 1
#                n-=1
#                if i>1:
#                    for j in dano[n::-1]:
#                        if j>=i:
#                            count+=1
#                        else: break
#                    if answer < i * count:
#                        answer = i * count
#    else:
#        answer = dano[0]
#    return answer 
#
#print(largest_histogram([1, 2, 3, 3, 3, 2]))
#dano = [1,2,3,3,4]
#for j in dano[-3::-1]:
#    print(j)