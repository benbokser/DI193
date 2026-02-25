with open("words.txt", "r") as f:
    content = f.read()


# content is ONE big string - split it into words
words = content.split()

print(words)
