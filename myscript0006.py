import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
msg = 'My phone no. is 415-273-4555.'
mo = phoneNumRegex.search(msg)
print('First mobile number group: ' + mo.group(1))
print('Second mobile number group: ' + mo.group(2))
print('Third mobile number group: ' + mo.group(0) + '\n\n')

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
msg = 'My phone no. is (415)-273-4555.'
mo = phoneNumRegex.search(msg)
print('First mobile number group: ' + mo.group(1))
print('Second mobile number group: ' + mo.group(2))
print('Third mobile number group: ' + mo.group(0))
