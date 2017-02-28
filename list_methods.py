#!/usr/bin/python3

list = ['a', 25, 'alpha', '55']
list.append('beta')
print (list)
list.extend([55, 600])
print(list)
list.insert(0, 5)
list.insert((len(list)-2), 10)
print(list)
list.remove(5)
print(list)
a = list.pop()
print(a)
print(list)
b = list.pop(len(list)-2)
print(b)
print(list)
print(list.index('alpha'))

print(list.count('alpha'))
num_list = [10, 20, 30, 78]
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
list2 = num_list.copy()
print(list2)

squares = list(map(lambda x: x**2, range(10)))
