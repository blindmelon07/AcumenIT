#string functions
sentence = "The quick brown FOX jumps over the lazy DOG"
breakpoint()
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
# print(sentence.swapcase())
# print(sentence.capitalize())
print(sentence.replace("fox".upper(), "cat".upper()))
sentence = sentence.replace("dog".lower(), "elephant")
sentence = sentence.replace("dog".upper(), "elephant")
print(sentence)