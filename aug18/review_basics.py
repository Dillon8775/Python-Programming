"""
review_basics.py: review basics of Python
by D. Strickland
08/18/2026
"""

import keyword as theKeywordList

__author__ = "Dillon Strickland" # Author
__email__ = "stricklandd0778@forsythtech.edu" #E-mail

# Print number of keywords in Python
print(f"There are {len(theKeywordList.kwlist)} keywords defined in this version of Python.")

# Returns: if a string is a valid identifier/str
def isValidIdentifier(identifier_name:str):
    # test if a given word is a keyword
    if theKeywordList.iskeyword(identifier_name):
        # print(f"[ERROR] {identifier_name} is a keyword.")
        return True
    else:
        # print(f"[SUCCESS] {identifier_name} is not a keyword.")
        return False

# Print documentation comment
print(__doc__)

print("Hello, and goodbye!", end=" woah")