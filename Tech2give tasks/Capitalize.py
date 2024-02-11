''' Question 4: Capitalize Words
 Write a program that accepts a string as input, capitalizes the first letter of each word in the string,
 and then returns the result string. Examples: "hi"=> returns "Hi" "i love programming"=> returns "I Love
 Programming"'''


def capitalization(input_str):
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


result1 = capitalization("hi")
result2 = capitalization("i love programming")

print(result1)
print(result2)
