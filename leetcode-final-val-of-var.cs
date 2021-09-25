/*
Leetcode Path - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

 

Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
*/


public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x = 0;
        
        for (int i = 0; i < operations.Length; i++){
            if(operations[i] == "++X" || operations[i] == "X++")
                x += 1;
            else if(operations[i] == "--X" || operations[i] == "X--")
                x -= 1;
        }
        return x;
    }
}
