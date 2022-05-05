#1
from datetime import datetime

y = int(input("Enter year born (4-digit): "))
m = int(input("Enter month born (1-12): "))
d = int(input("Enter day born (1-31): "))

date_born = datetime(year = y, month = m, day = d)
print("Number of days you lived:", (datetime.today() - date_born).days)

#2
snt = input("Enter a sentece: ").lower()
counts = snt.count("a") + snt.count("e") + snt.count("o") + snt.count("i") + snt.count("u")
print("Your sentence contains", counts, "vowels.")

#3
name_list =[]
result = 0

while True:
    name = input("Enter a name (q to quit): ").lower
    if name == "q":
        break
    else:
        name_list.append(name)
        a_count = name.count("a")
        result = result + a_count

print("Number of names and letter 'a': ", len(name_list), ",", result)


#4
num_list = []

while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    else:
        num_list.append(num)

num_list.sort()
max_num = num_list[-1]
print("The largest number entered was", max_num)