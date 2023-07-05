#list

# can be changed, removed, added
name_list = ['Ahmad', 'Waqar', 'Mahin', 'ALi', 'Abdullah']

name_list.append('Basil')
name_list.remove('Waqar')

name_list[0] = 'Ali'

#print(list(reversed(name_list)))

#Tuple

name_tuple = ('Ahmad', 'Waqar', 'Mahin', 'ALi', 'Abdullah')

#can't be canged, removed, or added

#print(name_tuple)

#set

#can be added, removed, and location is random
name_set = {'Ahmad', 'Waqar', 'Mahin', 'ALi', 'Abdullah'}

name_set.add('Basil')

#print(name_set)

#dictionary

name_dictionary = {'first': 'Ahmad', 'second': 'Waqar', 'third': 'Mahin'}
name_dictionary['forth'] = 'Basil'
name_dictionary['first'] = 'Ali'

#print(name_dictionary)


# for loop
'''
for name in ['Ahmad', 'Waqar', 'Mahin', 'ALi', 'Abdullah']:
    print(name)


for i in range(10):
    print(i)

name_range = list(range(10))

print(name_range)
'''
#while loop

num = 0

while num <= 10:
    num += 1

# conditional statements
'''
if num < 10:
    print('Hello world')

elif num > 10:
    print('Elif World')

else:
    print('Else world')
'''
'''
#functions

#      Parameter
def name(name):
    if name == 'Mahin':
        return 'Muhammad Mahin'
    else:
        return name

name = name('Ahmad')

print(name)
'''
'''
name = 0
print(type(name))

name = str(0)
print(type(name))

num = int(input('What is you number?: '))

print(num + 2)
'''

num = [1, 2, 3]
print(len(num))
for i, value in enumerate(num):
    print(i)
    print(value)