# Q1
"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.


Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
"""
# URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

# Solution

def findLucky(arr):
    # Step 1: Frequency count
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Check lucky numbers
    lucky = -1
    for num in freq:
        if freq[num] == num:
            lucky = max(lucky, num)

    return lucky

print(findLucky([2, 2, 3, 4])) 

# Q2
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
'''
# URL: https://leetcode.com/problems/valid-parentheses/description/
# Solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # opening brackets
                stack.append(char)
            elif char in bracket_map:  # closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                return False  # invalid character

        return not stack  # stack should be empty if valid

sol = Solution()

print(sol.isValid("()"))        
print(sol.isValid("()[]{}"))    
print(sol.isValid("(]"))     