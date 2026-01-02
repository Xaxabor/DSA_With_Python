
def isPalindrome(st: str) -> bool:
    """
    Check if the given string is a palindrome.
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation 
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    Input: Tac t Coa 
    Output: Tru e (permutations : "tac o cat" , "atc o eta" , etc. )
    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """

    st = st.lower()
    s = set()

    for char in st:
        if char in s:
            s.remove(char)
        else:
            s.add(char)
    

    if len(s)>1:
        return False
    return True


# Example usage:
if __name__ == "__main__":
    test_strings = [
        "samadam",
        "hello",
        "tacocat",
        "112233",
        "aAbcd",
        "AaBbCc"
    ]

    for test_str in test_strings:
        result = isPalindrome(test_str)
        print(f"'{test_str}': {result}")