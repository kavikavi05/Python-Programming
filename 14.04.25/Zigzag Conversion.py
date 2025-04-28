class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        arr = [["" for _ in range(len(s))] for _ in range(numRows)]
        row = 0
        going_down = False

        if numRows == 1:
            return s

        for j in range(len(s)):
            arr[row][j] = s[j]
            
            if row == 0 or row == numRows - 1:
                going_down = not going_down

            if going_down:
                row += 1
            else:
                row -= 1

        # for row in arr:
        #     print("".join(row))

        string_result = ""
        for i in range(numRows):
            for j in range(len(s)):
                string_result += arr[i][j]

        return string_result
