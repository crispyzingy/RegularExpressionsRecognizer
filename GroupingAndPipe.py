import re

# Grouping RE
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("Call me 415-555-1011 tomorrow")
print(mo.group(1))
print(mo.group(2))
phoneNumRegex = re.compile(r"\(\d\d\d\)-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("Call me (415)-555-1011 tomorrow")
print(mo.group())

# Pipe character
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())

