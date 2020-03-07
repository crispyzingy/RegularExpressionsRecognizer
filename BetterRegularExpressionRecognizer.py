# Better Regular Expressions recognizer
import re

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999"

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phoneNumRegex.findall(message))
