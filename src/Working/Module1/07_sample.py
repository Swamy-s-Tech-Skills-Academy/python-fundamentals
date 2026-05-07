Examining the Print Function in Depth
print()
age = 29
sentence = "My years old is"
print(sentence age)
  File "<ipython-input-52-e28092760f3c>", line 1
    print(sentence age)
                   ^
SyntaxError: invalid syntax
print(sentence, age)
My years old is 29
print(sentence, age, sep = "-")
print(sentence, age, sep = "-")
My years old is-29
My years old is-29
print(sentence, age, sep = "-", end = "")
print(sentence, age, sep = "-")
My years old is-29My years old is-29