def count():
    f = input("Enter file name:")
    numberOfWords = 0
    file = open(f, 'r')
    for line in file:
        words = line.split()
        numberOfWords += len(words)
    print("number of words: ", numberOfWords)
count()