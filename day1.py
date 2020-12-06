file = open(r"day1_data2.txt", "r")
data = file.read()
words = data.split()
#print(words)
def report(data):
    for i in range(len(words)):
        sum1 = int(words[i])
        for j in range(len(words)):
            sum2 = int(words[j])
            value = sum1 + sum2
            #print(value)
            #print(sum1)
            #print(int(sum1) * int(sum2))
            if value == 2020:
                solution = sum1 * sum2
                print("%i + %i" % (sum1, sum2))
                #print(solution)

print('Number of words in text file :', len(words))
report(file)
