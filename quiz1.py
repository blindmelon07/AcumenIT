

sentence = "The quick brown FOX jumps over the lazy DOG"
vowels = "aeiou"
for vowel in vowels:
    sentence = sentence.replace(vowel, "")
print(sentence)

sentence = (sentence.replace("a", "")
     .replace("e", "")
        .replace("i", "")
            .replace("o", "")
                .replace("u", ""))
print(sentence)