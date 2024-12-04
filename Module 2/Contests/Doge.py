#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def doge_count(str):
    
    # Initialize a counter to keep track of the number of modified "doge" patterns
    count = 0
    
    # Loop through the string, stopping 3 characters before the end to avoid index out of range error
    for i in range(0, len(str) - 3):
        # Check if the substring starting at index i matches "do" and ends with "e"
        if str[i] == "d" and str[i+1] == "o" and str[i+3] == "e":
            # If the pattern matches, increment the counter
            count= count + 1
    
    # Return the final count of the modified "doge" patterns
    return count

#{ 
 # Driver Code Starts.



def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(doge_count(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends
