class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Create sets to keep track of what numbers are used in each row, col, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        empty_cells = []
        
        # 1. First Pass: Initialize the sets and collect all empty cell coordinates
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    # The formula to find the 1D box index (0-8) from 2D coordinates
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)
                    
        # 2. The Backtracking Function
        def backtrack(index):
            # Base case: If we've successfully filled every cell in our list, we are done!
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)
            
            # Try numbers 1 through 9
            for val in map(str, range(1, 10)):
                # O(1) Check: Is the number missing from the row, col, and box sets?
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_index]:
                    
                    # Place the number
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_index].add(val)
                    
                    # Recurse to the next empty cell
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack: Remove the number
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_index].remove(val)
                    
            return False
            
        # Start the recursion at the first empty cell in our list
        backtrack(0)