# Python has functions for creating, reading, updating, and deleting files.
myFile = open ('myfile.txt', 'w')

# Get some info
print('Name', myFile.name)
print('Closed', myFile.closed)
print('Mode', myFile.mode)

# Write to file
myFile.write('Wir')