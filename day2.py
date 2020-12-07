import re


file = open(r'day2_data2.txt', 'r')
#data = file.readlines()
passwords = re.findall(r'(\d+)-(\d+)\s(\w)', file.read())
valid = 0

for tuple in passwords:
    print(tuple[0], tuple[1], tuple[2])

    #if passwords[tuple]
    
    

#print(file.read())
#print(passwords)
