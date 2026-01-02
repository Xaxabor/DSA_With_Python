"""
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
EXAMPLE 
pale , pi e - > tru e 
pales , pal e - > tru e 
pale , bal e - > tru e 
pale , bak e - > fals e
"""

def one_away(first: str, second: str) -> bool:

    a = len(first)
    b = len(second)
    if abs(a - b) > 1:
        return False
    isEq= False
    chanceLeft = True
    if a == b:
        isEq = True
    if a < b:
        first, second = second, first
        a, b = b, a
    j = 0
    i = 0
    while(i<b):
        if first[j] != second[i]:
            if not chanceLeft:
                return False
            else:
                chanceLeft = False
                if not isEq:
                    j+=1
                else:
                    j+=1
                    i+=1
        else:
            j += 1
            i += 1

    return True



if __name__ == "__main__":
    print(one_away("pale", "ple"))  # True
    print(one_away("pales", "pale"))  # True
    print(one_away("pale", "bale"))  # True
    print(one_away("pale", "bake"))  # False
    print(one_away("pale", "pse"))  # False
    print(one_away("pale", "paless"))  # False