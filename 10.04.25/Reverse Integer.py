class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Teskari sonni olish
        a = int(str(abs(x))[::-1])
        
        # Agar manfiy bo‘lsa, minusni qo‘shamiz
        if x < 0:
            a = -a
        
        # Overflowni tekshirish
        if a < INT_MIN or a > INT_MAX:
            return 0
        
        return a
