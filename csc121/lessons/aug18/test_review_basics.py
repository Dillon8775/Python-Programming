import review_basics as rb

help(rb)
print(rb.__doc__)

print("=== TEST REVIEW BASICS ===")

if (rb.isValidIdentifier("Amy")):
    print("Amy is a keyword")
else:
    print("Amy is not a keyword")