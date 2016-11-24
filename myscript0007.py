import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4|)')
msg = 'My phone number is: 415-358-3945'
mo = phoneNumRegex.search(msg.group(1))
print(mo)
