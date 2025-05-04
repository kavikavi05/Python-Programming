class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numbers=sorted(nums)
        #at every integer in nums we can either add it or not add it to the solution
        #this creates a tree of possibilites, left is add, right is don't add. 
        #if we write an algorithm to create this tree, storing every leaf node in a set,
        #we can return the set
        seen=set()
        possibilities = [[]]  #create the initial none set, which is always a solution
        for i in range(len(numbers)):
            this_num=numbers[i]

            for j in range(len(possibilities)):
                #going through every branch, adding possibility
                new_possibility = possibilities[j][:]
                new_possibility.append(this_num)
                tupled=tuple(new_possibility)
                if tupled in seen:
                    continue 
                #we haven't seen this possibilit before,
                #add a possibility where this element was added on
                #to the possibilities list and the seen hashmap
                seen.add(tupled)
                possibilities.append(new_possibility)
        output_list=[[]]
        for i in range(len(possibilities)):
            if possibilities[i] in output_list:
                continue
            else:
                output_list.append(possibilities[i])
        return sorted(output_list
