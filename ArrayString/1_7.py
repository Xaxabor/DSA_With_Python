"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate(matrix: list[list[int]]) -> None:
    
    N= len(matrix)
    
    for i in range(N-1):
        for j in range(i+1,N):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]

    for i in range(N):
        matrix[i] = [matrix[i][j] for j in range(N-1, -1, -1)]

# Time Complexity: O(N^2)
# Space Complexity: O(1)

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    rotate(matrix)
    
    for row in matrix:
        print(row)