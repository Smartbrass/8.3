m = int(input('Грузоподъемность:'))
n = int(input('Сколько рыбаков?:'))
a = []
b = []
for i in range(n):
    a.append(int(input('Вес рыбака?:')))
# Сортируем список, чтобы алгоритм работал точнее
a.sort()
a.reverse()
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print(len(b))
     