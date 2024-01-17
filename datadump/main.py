with open('dump.json', 'rb') as f:
    data = f.read()

# Change the encoding of the data
data_str = data.decode('utf-16')

# Save the data back to a file
with open('dump.json', 'w', encoding='utf-8') as f:
    f.write(data_str)


