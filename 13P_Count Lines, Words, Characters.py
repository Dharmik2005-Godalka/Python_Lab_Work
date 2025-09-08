with open("ict.txt", 'r') as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
chars = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)
