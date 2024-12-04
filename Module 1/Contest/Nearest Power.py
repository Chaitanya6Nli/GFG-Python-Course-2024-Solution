#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

    
def nearestPower(A, B):
    # Initialize variables
    closest_power = None
    min_diff = float('inf')
    
    # Start iterating powers
    P = 0
    while True:
        power_value = A ** P
        
        # If power value exceeds B, stop checking further
        if power_value > B:
            break
        
        # Check the difference between current power and B
        diff = abs(power_value - B)
        
        # Update closest_power if current is better
        if diff < min_diff:
            min_diff = diff
            closest_power = power_value
        
        P += 1
    
    # Consider the next power (as A^P > B) to ensure closest is correctly chosen
    next_power_value = A ** P
    if abs(next_power_value - B) < min_diff:
        closest_power = next_power_value
    
    return closest_power


#{ 
 # Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(nearestPower(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends
