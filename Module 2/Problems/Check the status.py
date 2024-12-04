#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to check value and 
# return accordingly
def check_status(a, b, flag):
    
    # Check the first condition
    if (a >= 0 or b >= 0) and not (a >= 0 and b >= 0) and not flag:
        return True
    
    # Check the second condition
    elif a < 0 and b < 0 and flag:
        return True
        
    # If none of the conditions are met
    else:
        return False
        
#{ 
 # Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
# } Driver Code Ends
