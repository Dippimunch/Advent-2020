import re


file = open(r'day2_data.txt', 'r')
passwords = re.findall(r'(\d+)-(\d+)\s(\w):\s(\w+)', file.read())
valid = 0

for i in range(len(passwords)):
    valid_check = passwords[i][3].count(passwords[i][2])

    if valid_check >= int(passwords[i][0]) and valid_check <= int(passwords[i][1]):
        valid += 1

print('# of valid passwords: ', valid)
