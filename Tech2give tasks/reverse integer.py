''' Question 5: Reverse Integer Write a program that takes an integer as input and returns an
integer with reversed digit ordering. Examples: For input 500, the program should return 5.
For input -56, the program should return -65. For input -90, the program should return -9.
For input 91, the program should return 19 '''


def integer_reverse(num):
    sign = -1 if num < 0 else 1
    num_string = str(abs(num))
    reversed_string = num_string[::-1]
    reversed_number = int(reversed_string) * sign
    return reversed_number


result1 = integer_reverse(500)
result2 = integer_reverse(-56)
result3 = integer_reverse(-90)
result4 = integer_reverse(91)

print(result1)
print(result2)
print(result3)
print(result4)
