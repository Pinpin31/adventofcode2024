import re
total = 0

with open("day3.input") as file:
    vals = file.read()
print(len(vals))
vals = re.sub(r"don't\(\).*?do(?!n't)\(\)", '', vals)
print(len(vals))
x = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
result = re.findall(x,vals)
for x,y in result:
    total +=int(y)*int(x)
print(total)
