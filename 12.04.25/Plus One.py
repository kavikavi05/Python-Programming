class Solution(object):
    def plusOne(self, digits):
        int1=int("".join(map(str,digits)))#converts list to int type store in int1(variable)
        int2=int1+1 #add plus one to int1 and store in int2
        list1=list(map(int,str(int2)))# convert int to list type and store in list1(variable)
        print(list1)
        return list1
        
