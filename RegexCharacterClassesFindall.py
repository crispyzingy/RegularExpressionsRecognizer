import re

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(
    phoneRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
)  # findall the matches

lyrics = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"

xmasRegex = re.compile(r"\d+\s\w+")  # character classes
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(
    r"[aeiouAEIOU]"
)  # this is better than r'(a|e|i|o|u)', put caps and smalls both
print(vowelRegex.findall("Robocop eats baby food"))

doubleVowelRegex = re.compile(r"[aeiou]{2}")  # finds exactly 2 vowels in sequence
print(doubleVowelRegex.findall("Robocop eats baby food"))

rangesRegex = re.compile(r"[a-fA-F]")  # ranges: a to f & A to F

consonantsRegex = re.compile(
    r"[^aeiouAEIOU]"
)  # negativeCharacterClass, finds the remaining
print(consonantsRegex.findall("Robocop eats baby food"))
