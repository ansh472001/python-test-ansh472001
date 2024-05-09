class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0
    
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        

        def flood_fill(row, col):

            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "L":
               
                grid[row][col] = "W"
               
                flood_fill(row + 1, col)
                flood_fill(row - 1, col)
                flood_fill(row, col + 1)
                flood_fill(row, col - 1)
        
        
        for i in range(rows):
            for j in range(cols):
            
                if grid[i][j] == "L":
                    flood_fill(i, j)
                    island_count += 1
        
        return island_count

