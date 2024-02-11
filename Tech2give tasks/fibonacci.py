''' Question 2: Fibonacci Sequence
 Write a program to generate the Fibonacci sequence up to 100. '''

a = 0
b = 1
while a <= 100:
    print(a)
    a = b
    b = a + b
