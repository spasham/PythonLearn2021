#find vowels and consonants in your name
name = input('enter your name: ')
vowels = ['a','e','i','o','u']

for char in name:
    if char in vowels:
        print(char, '- is vowel')
    else:
        print(char, '- is a consonant')
print ('Thank You..')