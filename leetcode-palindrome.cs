/*
Leetcode problem - https://leetcode.com/problems/palindrome-number/

Problem statement - 

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
*/

/*
My Solution
*/

public class Solution {
    public bool IsPalindrome(int x) {
        string str_x = x.ToString();
        
        for (int i = 0; i < str_x.Length; i++){
            if(str_x[i] != str_x[str_x.Length - 1 - i])
                return false;
        }
        return true;
    }
}
