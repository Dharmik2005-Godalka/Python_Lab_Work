# First, read binary data from source file
with open('a.tif', 'rb') as f:   
    binary_data = f.read()

# Then, write binary data to a new file
with open('c.tif', 'wb') as f:   
    f.write(binary_data)
