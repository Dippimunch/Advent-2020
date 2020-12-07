import re


file = open(r'day2_data2.txt', 'r')
#data = file.readlines()
passwords = re.findall(r'(\d+)-(\d+)\s(\w):\s(\w+)', file.read())
valid = 0


for i in range(len(passwords)):
    print(passwords[i])
    valid_check = passwords[i][3].count(passwords[i][2])

    print(valid_check)

    if valid_check >= int(passwords[i][0]) & valid_check <= int(passwords[i][1]):
        valid += 1
    

"""for tuple in passwords:
    print(tuple[0], tuple[1], tuple[2], tuple[3])
    print(passwords[0])
    #if passwords[tuple]"""
    
    
print('# of valid passwords: ', valid)
#print(file.read())
#print(passwords)
