 # your task is to complete this function# function should return index to the any valid peak elementclass Solution:

 def peakElement(arr, n):
     a=1
    # Code here

     if n>1:
         for i in range(n):
             j=n-i;
             if j>1:
                 if(arr[j-1]>arr[j-2]):
                     return j-1;
                 else:
                     return 0;
     return 0

     #{ # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1: flag = True
        elif index==0 and arr[index]>=arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>=arr[index-1]:
            flag = True
        elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
        flag = True
        else:
            flag = False
        if flag:
            print(1)
        else: print(0)
        # Contributed by: Harshit Sidhwa# } Driver Code Ends