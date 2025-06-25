##DS
##Saturday, March 25, 2023
##1:49 AM
 
##Add 2 numbers:
Input:nums = [2,7,11,15], target = 9
Output:[0,1]
Explanation:Because nums[0] + nums[1] == 9, we return [0, 1].
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums= nums
        self.target = target
        length = len(nums)
        for i in range(0,length-1):
            b = i+1
            c= nums[i] +nums[b]
            if c == target:
                return [i,b]
 
 
 
nums = [3,2,4]
target = 6
t= Solution()
t.twoSum(nums,target)
 https://pynative.com/online-python-code-editor-to-execute-python-code/
 
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [4,6,2,1,8]
target = 9
t= Solution()
result = t.twoSum(nums,target)
print(result)


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict= {}
        for i in range(0,len(nums)):
            complement = target-nums[i]
            if complement in dict:
                return [i,dict[complement]]
            else:
                dict[nums[i]]=i

nums = [4,6,2,1,8]
target = 6
t= Solution()
result = t.twoSum(nums,target)
print(result)

 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict= {}
        for i in range(0,len(nums)):
            complement = target-nums[i]
            if complement in dict:
                return [i,dict[complement]]
            else:
                dict[nums[i]]=i
 
 
 
# Find unique characters in a string
 
def miniMaxSum(arr):
    sum1 = 0
    max_sum = 0
    arr.sort()
    for i in range(0,len(arr)-1):
        sum1 = sum1 + arr[i]
    for n in range(1,len(arr)):
        max_sum = max_sum + arr[n]
    print(sum1,max_sum )
 
 
    i= 0
        ans = 0
        a = []
        for char in s:
            if char not in a:
                a.append(char)
                ans = max(len(a),ans)
            else:
                while i < len(a) and char in a:
                    a.pop(0)
                    i+=1
                a.append(char)
                i+=1
        return ans
 
 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        ans = 0
        for char in s:
            if char not in a:
                a.append(char)
                ans = max(len(a), ans)
            else:
                print(a)
                while i < len(s)-1 and char in a:
                    a.pop()
                    i=i+1
                a.append(char)
            return ans
 
 
class Solution:
    def lengthOfLongestSubstring(self, s):
        j=0
        i=0
        v=[]
        maxi=0
        while(j<len(s)):
            char=s[j]
            if char not in v:
                #update the length of the array
                v.append(char)
                maxi=max(maxi,len(v))
            else:
                print(v)
                while(char in v and i<len(s)):
                    v.pop(0)
                    #pop the character from the top till the character cannot be present in the array...
                v.append(char)
            j+=1
        return maxi




##Enter first 10 numbers


start_num = int(input("Enter starting num: "))
end_num = int(input("Enter ending num: "))
numbers = range(start_num,end_num+1)
sum = 0
for x in numbers:
  if (x%2!= 0):
    print(x)



##Leet Code 136 Find Single number


class Solution(object):
    def singleNumber(self, nums):
        h=defaultdict(int)
        for x in nums:
            h[x] = h[x]+1
        for x in nums:
            if h[x] == 1:
                return x
XOR-> If numbers are same returns 0 and if different returns number


class Solution(object):
    def singleNumber(self, nums):
       result = 0
       for x in nums:
        result = result ^ x
       return result



	##121. Best time to But and sell stocks
	
	class Solution(object):
	    def maxProfit(self, prices):
	        min_n = prices[0]
	        maxp = 0
	        for i in range(1,len(prices)):
	            if prices[i] < min_n:
	                min_n = prices[i]
	            profit = prices[i]-min_n
	            if maxp < profit:
	                maxp = profit
	        return maxp
	
