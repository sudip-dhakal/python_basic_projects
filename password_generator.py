import random
word="364782#^$*&#^$&*(#)abcdefghijklmn"
length_of_word=len(word)
print(length_of_word)
password=""
for i in range(12):
    password=password+random.choice(word)
print(password)