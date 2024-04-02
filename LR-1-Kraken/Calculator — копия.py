print("Stable Version")
from num2words import *
des = ['плюс', 'минус', 'умножить', 'разделить', 'на', 'остаток']
ch = []

for i in range(99*99+1):
    ch.append(num2words(i, lang='ru'))

vvod = input().split()
if 'на' in vvod:
    vvod.remove('на')
if 'от' in vvod:
    vvod.remove('от')
if 'деления' in vvod:
    vvod.remove('деления')
if 'одна' in vvod:
    vvod = [vv.replace('одна', 'один') for vv in vvod]
if 'две' in vvod:
    vvod = [vv.replace('две', 'два') for vv in vvod]
    

k1 = []
p1 = []

for i in vvod:
    if i not in des:
         k1.append(i)
    else:
        deist = i
        k2 = ' '.join(map(str, k1))
        k1 = []
        p1.append(k2)
        
k2 = ' '.join(map(str, k1))
p1.append(k2)


def smesh(j):
    t1 = []
    r1 = []
    j = j.split()
    for i in j:
        if i != 'и':
            t1.append(i)
        else:
            t2 = ' '.join(map(str, t1))
            t1 = []
            r1.append(t2)
    t2 = ' '.join(map(str, t1))
    r1.append(t2)
    return r1


g1 = smesh(p1[0])
if len(g1) > 1:
    g2 = g1[1]
    g1 = g1[0]
else:
    g1 = g1[0]
    g2 = 0
    
g3 = smesh(p1[1])
if len(g3) > 1:
    g4 = g3[1]
    g3 = g3[0]
else:
    g3 = g3[0]
    g4 = 0

    
def p_t(l):
    if l != 0:
        l = l.split()
        if (l[-1] == 'десятых') or (l[-1] == 'десятая'):
            l.remove(l[-1])
            l = ' '.join(map(str, l))
            l = (ch.index(str(l)))/10
        elif (l[-1] == 'сотых') or (l[-1] == 'сотая'):
            l.remove(l[-1])
            l = ' '.join(map(str, l))
            l = (ch.index(str(l)))/100
        elif (l[-1] == 'тысячная') or (l[-1] == 'тысячных'):
            l.remove(l[-1])
            l = ' '.join(map(str, l))
            l = (ch.index(str(l)))/1000
    
    return l


num1 = ch.index(str(g1)) + (p_t(g2))
num2 = ch.index(str(g3)) + (p_t(g4))


def drob(num1,num2):
    d = (round((num1/num2)%1,3))
    d1 = d % 1
    d1 =  d1 * 1000
    if d1 != 0:
        if d1 % 100 == 0:
            d1 = d1/100
            pr = d1 - 1
            d1 = ' и ' + ch[round(d1)]
            if 'один' in d1:
                d1 = d1.replace('один', 'одна', 1)
            if 'два' in d1:
                d1 = d1.replace('два', 'две', 1)
            if pr % 10 == 0:
                d1 += ' десятая'
            else:
                d1 += ' десятых'
        elif d1 % 10 == 0:
            d1 = d1/10
            pr = d1 - 1
            d1 = ' и ' + ch[round(d1)]
            if 'один' in d1:
                d1 = d1.replace('один', 'одна', 1)
            if 'два' in d1:
                d1 = d1.replace('два', 'две', 1)
            if pr % 10 == 0:
                d1 += ' сотая'
            else:
                d1 += ' сотых'
        else:
            pr = d1 - 1
            d1 = ' и ' + ch[round(d1)]
            if 'один' in d1:
                d1 = d1.replace('один', 'одна', 1)
            if 'два' in d1:
                d1 = d1.replace('два', 'две', 1)
            if pr % 10 == 0:
                d1 += ' тысячная'
            else:
                d1 += ' тысячных'
    else:
        d1 = ''
    return d1


if deist == 'плюс':
    itog = ch[round((num1 + num2)//1)] + drob(num1 + num2, 1)
    
elif deist == 'минус':
    if (num1 - num2)>=0:
        itog = ch[round((num1 - num2)//1)] + drob(num1 - num2, 1)
    else:
        itog = 'минус '+ ch[round((num2 - num1)//1)] + drob(num2 - num1, 1)
        
elif deist == 'умножить':
    itog = ch[round((num1 * num2)//1)] + drob(num1 * num2, 1)

elif deist == 'разделить':
    if k2 != 'ноль':
        if num1 % num2 != 0:
            itog = ch[round(num1//num2)] + drob(num1,num2)
        else:
            itog = ch[num1/num2]
    else:
        print('Ошибка. Деление на ноль')
        itog = 'Error'

elif deist == 'остаток':
    if k2 != 'ноль':
        if num1 % num2 != 0:
            itog = ch[num1%num2]
    else:
        print('Ошибка. Деление на ноль')
        itog = 'Error'

print(itog)