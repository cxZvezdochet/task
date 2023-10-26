import re
s = input()
print(re.findall('\S+@\S+', s))