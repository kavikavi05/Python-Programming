class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        memo = {}

        def solve(s1_start, s1_end, s2_start, s2_end):
            if (s1_start, s1_end, s2_start, s2_end) in memo:
                return memo[(s1_start, s1_end, s2_start, s2_end)]

            sub_s1 = s1[s1_start:s1_end]
            sub_s2 = s2[s2_start:s2_end]

            if sub_s1 == sub_s2:
                memo[(s1_start, s1_end, s2_start, s2_end)] = True
                return True

            if sorted(sub_s1) != sorted(sub_s2):  # Early optimization
                memo[(s1_start, s1_end, s2_start, s2_end)] = False
                return False

            for i in range(1, len(sub_s1)):
                if (solve(s1_start, s1_start + i, s2_start, s2_start + i) and 
                    solve(s1_start + i, s1_end, s2_start + i, s2_end)):
                    memo[(s1_start, s1_end, s2_start, s2_end)] = True
                    return True

                if (solve(s1_start, s1_start + i, s2_start + len(sub_s1) - i, s2_end) and
                    solve(s1_start + i, s1_end, s2_start, s2_start + len(sub_s1) - i)):
                    memo[(s1_start, s1_end, s2_start, s2_end)] = True
                    return True

            memo[(s1_start, s1_end, s2_start, s2_end)] = False
            return False

        return solve(0, n, 0, n)
