class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)        # Number of rows
        n = len(matrix[0])     # Number of columns
        
        # Treat the matrix as a virtual 1D array from index 0 to (m * n) - 1
        left = 0
        right = (m * n) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Map the 1D index 'mid' back to 2D coordinates (row, col)
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
