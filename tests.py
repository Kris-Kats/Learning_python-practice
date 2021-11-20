#name = input('Как тебя зовут? ')
#print('Привет,', name)
#print()
#num = input('Введи число ')
#print('Ты ввела число: ', num)

name1 = 'Тимур'
name2 = name1
print(name2)
print(name1)

name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name1 = 'Timur'
name2 = 'Gvido'
name1, name2 = name2, name1
print('Имя:', name1, 'Фамилия:', name2)

# print('Java')
# print('Ruby')
# print('Scala')
print('Python', end='+')  # print('C++')
# print('GO')
print('C#', end='=')  # print('C')
print('awesome')
# finish

#num1 = input()
#num2 = input()
#print(num1 + num2)

#num1 = int(input())
#num2 = int(input())
#print(num1 + num2)

s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100
print(s)

x = 3 
y = 4 
z = x + y 
z = z + 1 
x = y 
y = 5
x = z + y + 7
print(x)

a = 4
print(a, 'a')

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))


print(23 // 7)
print(20 // 5)
print(2 // 5)
print(123 // 10)
print(-123 // 10)
print()
print(23 % 7)
print(20 % 5)
print(2 % 5)
print(123 % 10)
print()
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)
print()
a = 82 // 3 ** 2 % 7
print(a)

b1, q, n = int(input()), int(input()), int(input())
print(b1*q**(n-1))

n = int(input())
print(n//100)