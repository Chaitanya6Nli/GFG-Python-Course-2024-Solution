#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to print numbers from n-1 to 0 if n is positive
def pos(n):
    for i in range(n-1, -1, -1): 
        print(i, end=" ")
        
# Function to print numbers from n to 0 if n is negative
def neg(n):
    for i in range(n, 1): 
        print(i, end=" ")
    

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends
