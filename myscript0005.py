import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-345-1238.')
print('Phone number found: ' + mo.group())
