file = open(r"day1_data.txt", "r")

def report(data):
    for i in range(len(data)):
        sum1 = i
        for j in range(len(data)):
            sum2 = j
