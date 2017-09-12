poem = "Do not go gentle into that good night"

print("if there is not 10 elements in list, let's fix that")

# split the stuff
stuff = poem.split()

ten_list = ['rage', 'rage', 'say', 'overwhelm', 'assume']

# add elements of ten_list to stuff unttil 10
while len(stuff) !=10:
    next = ten_list.pop()
    print(f"adding {next}")
    stuff.append(next)

print(f"{ten_list}")

print(f"{stuff}")
print(stuff[-1])
