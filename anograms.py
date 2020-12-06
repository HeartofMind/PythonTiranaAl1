
def anograms(string1, string2):
    if (sorted(string1) == sorted(string2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


anograms('cuna','nacu')