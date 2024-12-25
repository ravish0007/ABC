class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def mergesort(arr, s, e):
            if (e-s+1) <= 1:
                return arr
            
            mid = (s+e)//2

            mergesort(arr, s, mid)
            mergesort(arr, mid+1, e)
            merge(arr,s,mid,e)
            return arr
        
        def merge(arr, s, m, e):

            L = arr[s: m]
            R = arr[m: e+1]

            i = 0
            j = 0
            k = s

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return mergesort(nums, 0, len(nums)-1)   
