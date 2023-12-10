def check_number(a, b, c):
    # Count the number of positive number
    count = 0
    
    # Check the number of positive number
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    
    # Return True if exactly two numbers are positive, False otherwise
     
    if count > 1 :
        print("true") 
    else :
        print("false") 
check_number(1,-2,0)

    
