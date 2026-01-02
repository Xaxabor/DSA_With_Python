"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0.
"""

def zero_matrix(matrix):
    s = set()

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                s.add("r"+str(i))
                s.add("c"+str(j))
    for i in range(m):
        for j in range(n):
            if "r"+str(i) in s or "c"+str(j) in s:
                matrix[i][j] = 0

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12],
        [0, 14, 15, 16]
    ]
    print(matrix)
    zero_matrix(matrix)
    print(matrix)
