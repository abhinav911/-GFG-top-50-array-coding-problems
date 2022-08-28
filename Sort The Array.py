#User function Template for python3
class Solution:
    def sortArr(self, arr, n):
        i=0
        h=n-1
        piv=arr[i]
        p=0
        arr=self.quicksort(p,h,arr)
        return arr

    def quicksort(self,l,r,nums):
        if (len(nums) <= 1):
            return nums
        if (l < r):
            pi = self.partition(l, r, nums)
            self.quicksort(l, pi-1, nums) # Recursively sorting the left values
            self.quicksort(pi+1, r, nums) # Recursively sorting the right values return nums
    def partition(self,l, r, nums):
        # Last element will be the pivot and the first element the pointer
        pivot, ptr = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:

                # Swapping values smaller than the pivot to the front
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
                # Finally swapping the last element with the pointer indexed number
                nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr


class Solution:
    def sortArr(self, arr, n):
        i=0
        h=n-1
        piv=arr[i]
        while(i<h):
            j=h
            while(arr[i]<=piv):
                i=i+1
            while(piv>arr[j]):
                j=j-1
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                p=j
            self.sortArr(i,p-1)
            self.soerArr(p+1,j)
            return arr
            #{ # Driver Code Starts#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
    for i in ans:
        print(i,end=" ")
        print()# } Driver Code Ends