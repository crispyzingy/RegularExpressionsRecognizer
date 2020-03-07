import re

namesRegex = re.compile(r"Agent \w+")
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))
print(
    namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
)  # substitute

namesRegex = re.compile(r"Agent (\w)\w*")  # returns only the group
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))
print(
    namesRegex.sub(
        r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob."
    )
)  # substitute


# verbose mode
re.compile(
    r"""
(\d\d\d-) | # area code (without parens, with dash)
(\(\d\d\d\))# -or- area code (with parens, no dash)
\d\d\d # first 3 digits
-      # second dash
\d\d\d\d #last 4 digits
""",
    re.VERBOSE,
)
