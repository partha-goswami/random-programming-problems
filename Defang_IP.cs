/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

LeetCode Path - https://leetcode.com/submissions/detail/358867666/
*/

public class Solution {
    public string DefangIPaddr(string address) {
        string address_output = string.Empty;
        
        if(string.IsNullOrEmpty(address))
            return address;
        
        foreach(char c in address){
            if (c == '.'){
                address_output += "[.]";
            }
            else{
                address_output += c.ToString();
            }
        }
        return address_output;
    }
}
