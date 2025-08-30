d = (3,[5,6,7],(4,5,6),[5,6,7,(6,7,8)],9,10)
d = (3,[5,6,7],(4,5,6),[5,6,7,(6,7,8)],9,10)

# Access 6 from the list [5,6,7]
print(d[1][1])      

# Access 6 from the tuple (4,5,6)
print(d[2][2])

# Access 6 from the nested list inside list
print(d[3][3][0])
