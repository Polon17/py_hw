#Написать калькулятор для вычисления дискриминанта. На вход подаются коэффициенты квадратного уравнения, выход - значение дискриминанта.

print("Введите значение коэффициентов квадратного уравнения вида a(x^2)+bx+c=0:")
a=int(input())
b=int(input())
c=int(input())
D1=(-b+((b*b-4*a*c)**0.5))/(2*a)
D2=(-b-((b*b-4*a*c)**0.5))/(2*a)
print(D1)
print(D2)

#По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

print("Введите целое число")
N=int(input())
i=1
print("Квадраты натуральных чисел не превосходящие данное:")
while i**2<=N:
    print(i**2)
    i+=1

#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

print("Введите целое число не меньше 2")
n = int(input())
i = 2
while n % i != 0:
    i += 1
print("Наименьший натуральный делитель равен",i)

#Последовательность Фибоначчи определяется так: f_0 = 0,  f_1 = 1,  f_n = f_{n−1} + f_{n−2}. По данному числу n определите n-е число Фибоначчи f_n.

print("Введите номер члена последовательности Фибоначчи")
n=int(input())
if n==0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n+1):
        a, b=b, a+b
    print("Данный член последовательности равен",b)

#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

print("Введите последовательность чисел через пробел")
a=input().split()
print("Элементы данной последовательности с четными индексами:")
for i in range(0, len(a), 2):
    print(a[i])

#Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы

print("Введите последовательность чисел через пробел")
s=input()
a=[int(s) for s in s.split()]
print("Четные элементы данной последовательности:")
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')

#Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.

print("Введите последовательность чисел через пробел")
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print("Соседние элементы одного знака:",a[i - 1], a[i])
        break
    
#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.

print("Введите последовательность натуральных чисел, последний элемент которой равен 0")
pre=int(input())
ans=0
while pre!=0:
    next=int(input())
    if next!=0 and pre<next:
        ans+=1
    pre=next
print("Количество элементов больших предыдущего равно",ans)

#Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

print("Введите последовательность чисел через пробел")
a=[int(i) for i in input().split()]
resh=0
for i in range(1, len(a) - 1):
    if a[i-1]<a[i]>a[i+1]:
        resh+=1
print("Количество элементов, больших двух соседних, помимо крайних, равно",resh)

#Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200. Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.

print("Введите невозрастающую последовательность натуральных чисел, не превышающих 200, через пробел")
a=[int(i) for i in input().split()]
print("Введите рост Пети, не превыщающий 200")
x=int(input())
nom=0
while nom<len(a) and a[nom]>=x:
    nom+=1
print("Номер Пети в строю по росту равен",nom+1)

#Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

print("Введите через пробел упорядоченный по неубыванию список")
b=[int(i) for i in input().split()]
raz=1
for i in range(0, len(b)-1):
    if b[i]!=b[i+1]:
        raz+=1
print("Количество различных элементов в данном списке равно",raz)
    
#Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

inmax=0
print("Введите список чисел через пробел")
c=[int(i) for i in input().split()]
for i in range(1, len(c)):
    if c[i]>c[inmax]:
        inmax=i
print("Наибольшее число из списка равно",c[inmax])
print("Индекс наибольшего (первого из наибольших, если их несколько) равен", inmax)

#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

naib=0
num_naib=0
el=-1
print("Введите последовательность натуральных элементов, окончавающуюся 0")
while el!=0:
    el=int(input())
    if el>naib:
        naib, num_naib=el, 1
    elif el==naib:
        num_naib+=1       
print("Количество элементов равных наибольшему равно",num_naib)

#Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

prev=-1
currep=0
maxrep=0
print("Введите последовательность натуральных чисел, последний элемент которой 0")
elem=int(input())
while elem!=0:
    if prev==elem:
        currep+=1
    else:
        prev=elem
        maxrep=max(maxrep, currep)
        currep=1
    elem=int(input())
maxrep=max(maxrep, currep)
print("Максимальное количестворавных подряд идущих элементов равно",maxrep)

#Даны два списка с числами, получить третий путем поэлементного сложения первых двух.

from itertools import zip_longest
print("Введите первый список через пробел")
u=[int(i) for i in input().split()]
print("Введите второй список через пробел")
e=[int(i) for i in input().split()]
q=[x+y for x, y in zip_longest(u, e, fillvalue=0)]
print(q) 

#Даные два вектора (списка), вычислить скалярное произведение

print("Введите координаты двух пространственных векторов")
d=[int(i) for i in input().split()]
r=[int(i) for i in input().split()]
f=d[0]*r[0]+d[1]*r[1]+d[2]*r[2]
print("Скалярное произведение данных векторов равно", f)