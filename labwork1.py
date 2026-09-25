import numpy
import math
import os
def p1():    
    PI = 3.14
    a = float(input())
    print(PI*(a**2))
def p2():
    a = float(input())
    print(a * (9 / 5) + 32)
def p3():
    a = int(input("Enter a number? "))
    if(a <= 1): 
        print(f"{a} is a NOT prime number") 
        return
    for i in range(2,a):
        if(a % i) == 0:
            print(f"{a} is a NOT prime number")
            return
    print(f"{a} is a prime number")
def p4():
    x = int(input("Enter a number? "))
    t = 1
    l = int(math.sqrt(x))
    for i in range(2, l):
        if(x % i == 0):
            t = t + i + x / i
    if(t == x): print(f"{x} is a perfect number")
    else: print(f"{x} is a NOT perfect number")
def p5():
    n = input("What is your favourite color? ")
    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
    if n in colors:
        print(f"Your color is at index {colors.index(n)}")
    else: 
        print("Sorry, I could not find your color")
def p6():
    a = range(7)
    b = range(1,11,3)
    c = range(5,0,-1)
    d = range(6,-3,-2)
    for i in a:
        print(i,end=" ")
    print()
    for i in b:
        print(i,end=" ")
    print()
    for i in c:
        print(i,end=" ")
    print()
    for i in d:
        print(i,end=" ")
def p7():
    s = str(input())
    a = s.replace("$", "")
    print(a)
def p8():
    l = list(map(int, input().split()))
    for i in l:
        if(i % 2 != 0):
            l.remove(i)
            print(f"{i} is removed")
    print(l)
def p9():
    n = int(input())
    if(n < 0):
        print("Invalid input")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(fact)
def p10():
    a = int(input())
    l = list()
    for i in range(2, int(math.sqrt(a)) + 1):
            if(a % i == 0):
                l.append(i)
                l.append(a // i)
    print(sorted(list(set(l))))
def p11():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(d) 
def p12():
    m = int(input())
    n = int(input())
    for i in range(n):
        for j in range(m):
            if(i == 0 or i == n-1 or j == 0 or j == m-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
p12()
