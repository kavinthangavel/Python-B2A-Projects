def translate(sentence):
    letter = ""
    for n in sentence:
        if n.lower() in "aeiou":
            if n.isupper():
                letter +="G"
            else:
                letter +="g"
        else:
            letter +=n
    return letter
sentence = input("Enter the sentence or word : ")
print(translate(sentence))