def check_string_is_permutation(s1, s2):
    """
    Check if one string is a permutation of another.
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
    other

    Args:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    bool: True if s1 is a permutation of s2, False otherwise.
    """

    if len(s1) != len(s2):
        return False

    mp = {}
    
    for char in s1:
        if char in mp:
            mp[char] +=1
        else:
            mp[char] = 1
            
    print(mp)
    
    for char in s2:
        if char in mp:
            mp[char] -=1
            if mp[char] == 0:
                mp.pop(char)
        else:
            return False
    
    if len(mp)==0:
        return True


# Example usage:

if __name__ == "__main__":
    str1 = "aalohaa"
    str2 = "ahaloaa"
    
    result = check_string_is_permutation(str1, str2)
    print(f'Is "{str1}" a permutation of "{str2}"? {result}')