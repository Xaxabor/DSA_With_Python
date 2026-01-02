"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" 
length of the string. (Note: If implementing in Java, please use a character array so that you can 
perform this operation in place.) 
EXAMPLE 
Input: "Mr 3ohn Smith", 13
Output: "Mr%203ohn%20Smith
"""

def urlify(string: str, true_length: int) -> str:
    # Convert the string to a list to allow in-place modifications
    char_list = list(string)
    
    # Count the number of spaces within the true length
    space_count = 0
    for i in range(true_length):
        if char_list[i] == ' ':
            space_count += 1
    
    # Calculate the new length after replacements
    new_length = true_length + space_count * 2
    
    # Index for the end of the new string
    index = new_length - 1
    
    # Modify the string in reverse order
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[index] = '0'
            char_list[index - 1] = '2'
            char_list[index - 2] = '%'
            index -= 3
        else:
            char_list[index] = char_list[i]
            index -= 1
    
    return ''.join(char_list[:new_length])


    if __name__ == "__main__":
        input_string = "Mr John Smith    "
        true_length = 13
        output_string = urlify(input_string, true_length)
        print(f"Input: '{input_string}' with true length {true_length}")
        print(f"Output: '{output_string}'")