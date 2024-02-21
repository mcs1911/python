#fname = input('Enter the file name: ')

fhandle = open('mbox-short.txt')
for line in fhandle:
    print(line.upper())