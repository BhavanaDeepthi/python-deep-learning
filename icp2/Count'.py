fname = input("Enter the name of the file:")
infile = open(fname, 'r')
words = 0
l = 0
characters = 0
line = infile.readline()
while line != "":
    for i in line:
        if i.isalpha():
           l=l+1
        else:
           pass

    characters = len(line)
    words = len(line.split())

    print(str(line) + " -->" + " words: " + str(words) + " letters: " + str(l) + " characters: " + str(characters))

    line = infile.readline()


