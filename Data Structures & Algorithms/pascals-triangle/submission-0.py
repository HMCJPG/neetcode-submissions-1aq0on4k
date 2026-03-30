class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(numRows - 1):

            prev_row = res[-1]
            temp_row = [0] + prev_row + [0]

            next_row = []

            for j in range(len(prev_row) + 1):
                next_row.append(temp_row[j] + temp_row[j + 1])

            
            res.append(next_row)

        return res