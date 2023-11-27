#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

class Solution:
    def subArraySum(self, arr, n, s): 
        start = 0
        array_sum = 0
        
        for j, element in enumerate(arr):
            array_sum += element
            while(array_sum > s):
                array_sum -= arr[start]
                start += 1
                
            if array_sum == s and start <= j:
                return [start+1, j+1]
        
        return [-1]
           
