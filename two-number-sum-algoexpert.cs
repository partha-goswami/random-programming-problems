/*
This is the solution I tried for two number sum problem for algoexpert
*/

using System;

public class Program {
	public static int[] TwoNumberSum(int[] array, int targetSum) {
		// Write your code here.
		int[] result = new int[2];
		for(int i = 0; i < array.Length; i++){
			for(int j = 0; j < array.Length; j++){
				if(i != j && (array[i] + array[j] == targetSum)){
					result[0] = array[i];
					result[1] = array[j];
					return result;
				}
			}
		}
		return new int[0];
