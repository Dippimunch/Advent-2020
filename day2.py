import re


file = open(r'day2_data2.txt', 'r')
#data = file.readlines()
passwords = re.findall(r'(\d+)-(\d+)\s(\w)', file.read())

#print(file.read())
print(passwords)
