from sys import argv

# argv pass to argv
script, filename = argv

print(f"the filename is called {filename}")

#open the .txt file
poem = open(filename)

# print the readed file
print(poem.readline())
print(poem.readline())

# move to position 0
poem.seek(0)

# read one line of the file
print('-'*40)
print(poem.read())

# move to position 0
poem.seek(0)

# truncate the poem
target = open(filename, 'w+')
print(target.readline())
target.truncate()
target.write('Do no go gentle into good night')
