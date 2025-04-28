class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        next_dir = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }

        direction = (0, 1)
        visited = set()
        r, c = 0, 0

        res = []

        for _ in range(ROWS * COLS):  # Visit every cell exactly once
            res.append(matrix[r][c])
            visited.add((r, c))

            nxt_r, nxt_c = r + direction[0], c + direction[1]
            if (nxt_r < 0 or nxt_r >= ROWS or
                nxt_c < 0 or nxt_c >= COLS or
                (nxt_r, nxt_c) in visited):
                # Change direction if necessary
                direction = next_dir[direction]
                nxt_r, nxt_c = r + direction[0], c + direction[1]

            r, c = nxt_r, nxt_c

        return res
