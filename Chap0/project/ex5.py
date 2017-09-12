from sys import argv

script, input_file = argv

# def a function print whole file
def print_all_file(input_file):
    print(input_file.read())

# def a function rewind file
def rewind_file(input_file):
    input_file.seek(0)

# def a function print one line of file
def print_count_line(line_count, input_file):
    print(f"the line_count is {line_count}")
    print(input_file.readline())

# open the file
current_file = open(input_file)

# print whole file
print_all_file(current_file)

# rewind file
rewind_file(current_file)

# initialization line_count
line_count = 1
#print one line of file
print_count_line(line_count, current_file)

line_count += 1
print_count_line(line_count, current_file)

line_count += 1
print_count_line(line_count, current_file)
