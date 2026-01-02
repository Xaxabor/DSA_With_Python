"""
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
"""

def compress_string(string: str) -> str:
    s = "aabcccccaaa"
    ans=""
    cc=s[0]
    c = 0
    nc = 0
    for char in s:
        if char == cc:
            c = c+1
        else:
            ans = ans + str(cc)+str(c)
            cc = char
            c = 1
            
    ans = ans + str(char)+str(c)
            
    print(ans)


if __name__ == "__main__":
        compress_string("aabcccccaaa")
