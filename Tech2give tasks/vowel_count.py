''' Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence. eg. "Hello world" =>returns 3'''

def count_vowels(sentence):
    vowels = "aeiou"
    vowel_count = sum(1 for char in sentence if char in vowels)
    return vowel_count


result = count_vowels("Hello world")
print(str(result).lower())
