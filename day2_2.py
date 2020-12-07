import re


file = open(r'day2_data.txt', 'r')
passwords = re.findall(r'(\d+)-(\d+)\s(\w):\s(\w+)', file.read())
valid = 0

for i in range(len(passwords)):
    if bool(passwords[i][3][int(passwords[i][0])-1] == passwords[i][2]) ^ bool(passwords[i][3][int(passwords[i][1])-1] == passwords[i][2]):
        valid += 1

print('# of valid passwords: ', valid)
