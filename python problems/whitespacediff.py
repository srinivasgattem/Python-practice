import string
sentence="hey, geeks !, how are you"
for i in sentence:
    if i in string.whitespace:
        print("printable value is:"+i)