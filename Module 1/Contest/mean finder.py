#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def mean(D,M):
    # your code here
    # Calculate the sum of A, B, and C
    sum_abc = 3 * M
    # Add D to the sum
    total = sum_abc + D
    # Calculate the new mean
    new_mean = total // 4  # Using integer division for floor
    return new_mean

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        D = int(input()) ##taking d as input
        M = int(input()) ## taking mean of 3 numbers
        print(mean(D, M))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends
