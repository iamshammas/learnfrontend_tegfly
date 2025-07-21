# name = input('Enter your name:')

# low = name.lower()
# cap = name.upper()
# spl = name.split()

# print(low,cap,spl)

# CALCULATOR

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def div(a,b):
#     print(a/b) 
# def mult(a,b):
#     print(a*b)

# a = int(input('Enter two numbers:'))
# b = int(input())

# choice = input('Enter calculation to be done: ')

# if choice =='+':
#     add(a,b)
# elif choice == '-':
#     sub(a,b)
# elif choice == '/':
#     div(a,b)
# elif choice == '*':
#     mult(a,b)
# else:
#     print('Wrong choice')

# LISTS

# movies = ['Yodha','Monkey Pen','Pokkiriraja','My Boss']

# print(movies)

# movies.append('Cheetah')
# movies.pop()
# movies.pop()

# print(movies)

# DICTIORIES

# person = {'name':'shammas','age':23,'place':'Kannur','Height':5.7}

# print(person)

#CHALLANGE

name = input('Enter your name: ')
age = int(input('Enter your age: '))
lang = input('Which language are u currently learning?')

data = {'name' : name, 'age':age, 'lang' : lang}
print(data)
print(f"Welcome {name}! At {age}, Learning {lang} is a great choice.")