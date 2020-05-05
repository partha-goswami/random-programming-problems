#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

#Example 1:

#Input: "()"
#Output: true

#Ref LeetCode URL - https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            for i in range(0, len(s)):
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    st.append(s[i])
                elif s[i] == ')' and len(st) > 0 and st[-1] != '(':
                    return False
                elif s[i] == '}' and len(st) > 0 and st[-1] != '{':
                    return False
                elif s[i] == ']' and len(st) > 0 and st[-1] != '[':
                    return False
                elif s[i] == ')' and len(st) > 0 and st[-1] == '(':
                    st.pop()
                elif s[i] == '}' and len(st) > 0 and st[-1] == '{':
                    st.pop()
                elif s[i] == ']' and len(st) > 0 and st[-1] == '[':
                    st.pop()
            
            if len(st) > 0:
                return False
        
        return True
        
