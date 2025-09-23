num = int(input("Enter:"))


num_factors = 1
output= ''
def check(number):
    global num_factors,output
    j = 2
    while j <= number:
        if number % j == 0:
            
            num_factors += 1
            

        if num_factors ==2:
            output = "not prime"
            break
        else:
            if j == number-1:
                
                output = "prime"
                break


        
        j += 1
    return output
             
i = 1
while i<=num:
    if check(i) == 'prime':
        print("it is prime"+ str(i) ) 
    else:
        print("not prime")        

    i += 1