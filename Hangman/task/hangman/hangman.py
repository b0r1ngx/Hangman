import random

print('H A N G M A N')
# create a tuple from file.txt
words = ('python', 'java', 'kotlin', 'javascript')
word = words[random.randint(0, len(words)-1)]
print(word)
offer = input()
print('Guess the word: > ' + word)
if offer == word:
    print("You survived!")
else:
    print("You are hanged!")