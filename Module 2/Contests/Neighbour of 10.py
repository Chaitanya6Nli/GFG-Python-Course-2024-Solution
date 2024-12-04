#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def isNeighbour(N):
    return N % 10 <= 2 or N % 10 >= 8


#{ 
 # Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(isNeighbour(N))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends
