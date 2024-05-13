def translate(sentence):
    letter = ""
    for n in sentence:
        if n in "AEIOUaeiou":
            letter +="g"
        else:
            letter +=n
    return letter
sentence = input("Enter the sentence or word : ")
print(translate(sentence))