
   # """
#*******pseudo code*******
   # This program is used to display a specific pattern on the screen
    #The for loop and if else control structure is used to print the pattern
    #First we intialize two variable that we will use to check the count and save the string 
    #Then for loop is used to control the iteration
    #if else is used inside the loop body , if part is used to print the first five lines of the pattern 
    #else part is used to print the last four lines of the pattern
    #The for loop will execute nine times
    #when the control will enter in the loop body it will check the value of variable which is used to control
    #the loop iteration
    #if the valua of variable doesnt match the condtion it will go to else part
    #"""


# check and star variable are intialized to use after
check = 0
star = 1

#for loop will iterate 1 to 9
for i in range(1, 10):
    
    # if will compare that 'i' value is less or equal to 5
    if i <= 5:
        
        # every time control enters into if body it will increased by 1
        check += 1
        # the star will multiplied by the time of check value
        star = "*" * check
        
        # print function is used to print the value of star 
        print(star)
    
    # else part will execute when if condition will false
    else:
        # every time control enter into else body check value decrease by 1
        check -= 1
        
        # star will multiplied with the check vale 
        star = "*" * check
        
        #print function is used to print the value of string
        print(star)
