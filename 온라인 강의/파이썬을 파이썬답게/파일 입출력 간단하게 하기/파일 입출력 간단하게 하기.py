with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))