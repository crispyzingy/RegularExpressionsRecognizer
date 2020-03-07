import re

beginsWithHelloRegex = re.compile(r"^Hello")  # ^: must start with Hello
mo = beginsWithHelloRegex.search("Hello there!")
print(mo.group())
mo = beginsWithHelloRegex.search('He said "Hello!"')
print(mo == None)
endsWithWorldRegex = re.compile(r"world!$")  # $: must end with world!
mo = endsWithWorldRegex.search("Hello world!")
print(mo.group())

allDigitsRegex = re.compile(
    r"^\d+$"
)  # must start and end with a digit, can contain more than one digit
mo = allDigitsRegex.search("2545353534343")
print(mo.group())

atRegex = re.compile(r".at")  # . can be any character(except newline), but ends with at
print(atRegex.findall("The cat in the hat sat on the flat mat."))

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
print(nameRegex.findall("First Name: Arbaaz Last Name: Khan"))

# greedy vs non-greedy
serve = "<To serve humans> for dinner.>"
nongreedy = re.compile(r"<(.*?)>")  # '?', so least possible
print(nongreedy.findall(serve))

greedy = re.compile(r"<(.*)>")  # no '?', so max possible
print(greedy.findall(serve))

prime = "Serve the public trust.\nProtect the innocent.\nUpload the law."
print(prime)

dotStar = re.compile(r".*")  # till newline appears
mo = dotStar.search(prime)
print(mo.group())

dotStar = re.compile(r".*", re.DOTALL)  # searches all, greedymatch
mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r"[aeiou]")
print(vowelRegex.findall("Arbaaz loves Food"))

vowelRegex = re.compile(r"[aeiou]", re.I)  # IGNORECASE
print(vowelRegex.findall("Arbaaz loves Food"))
