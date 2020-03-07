import re

batRegex = re.compile(r"Bat(wo)?man")  # wo is optional, it can appear 0 or 1 time
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # must match
mo = phoneRegex.search("My phone number is 415-555-1234. Call me tomorrow.")
print(mo.group())
mo = phoneRegex.search("My phone number is 555-1234. Call me tomorrow.")
print(mo == None)

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")  # optional
mo = phoneRegex.search("My phone number is 415-555-1234. Call me tomorrow.")
print(mo.group())
mo = phoneRegex.search("My phone number is 555-1234. Call me tomorrow.")
print(mo.group())

batRegex = re.compile(r"Bat(wo)*man")  # wo is optional, it can appear 0 or more times
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwowowowoman")
print(mo.group())

batRegex = re.compile(r"Bat(wo)+man")  # wo is not optional, must appear 1 or more times
mo = batRegex.search("The Adventures of Batman")
print(mo == None)
mo = batRegex.search("The Adventures of Batwowowowoman")
print(mo.group())

haRegex = re.compile(r"(Ha){3}")  # {} exactly that many times
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

haRegex = re.compile(r"(Ha){3,5}")  # {} min 3, max 5 times
mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())

haRegex = re.compile(
    r"(Ha){,5}"
)  # {} slices can be used here, {,5} means 0 to 5. {3,} means 3 or more

digitRegex = re.compile(r"(\d){3,5}")  # greedymatch: longest string possible
mo = digitRegex.search("1234567890")
print(mo.group())

digitRegex = re.compile(r"(\d){3,5}?")  # non-greedymatch: shortest string possible
mo = digitRegex.search("1234567890")
print(mo.group())
