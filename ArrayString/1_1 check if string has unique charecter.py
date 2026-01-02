
def check_string_has_unique_characters(s):
    """
    Check if a string has all unique characters.
    Implement an algorithm to determine if a string has all unique characters. What if you 
    cannot use additional data structures?
    Args:
    s (str): The input string.

    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    char_set = set()

    for char in s:
        if char.lower() in char_set:
            return False
        char_set.add(char.lower())

    return True


if __name__ == "__main__":
    test_strings = [
        "abcdef",
        "hello",
        "123456",
        "112233",
        "aAbcd",
        "AaBbCc"
    ]

    for test_str in test_strings:
        result = check_string_has_unique_characters(test_str)
        print(f"'{test_str}': {result}")