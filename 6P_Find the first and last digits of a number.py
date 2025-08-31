num = int(input("Enter a number: "))
last = num % 10

while num >= 10:
    num //= 10
first = num

print("First digit:", first)
print("Last digit:", last)
