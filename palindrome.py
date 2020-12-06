#just a comment
def palindrome(s):
    s = ("".join([st for st in s if st in "abcdefgjklmnpqrstuvwxzy"])) #remove the special characters
    if len(s) <= 1:
        return True
    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            return False
    return True


if palindrome("Able was i,ere i saw elba".lower()):
    print(True)
else:
    print(False)
