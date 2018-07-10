# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:43:00 2018

@author: vaibh
"""


print("This program will show the probability of getting employed and not getting employed if you know java or python or both\nNOTE:assuming that you only want to get a job in related field\nNOTE:please re-run the program after getting the results to choose different skills")
Skill = int(input("Enter 1 for Python or 2 for Java or 3 for both : "))


if Skill == 1:
    platform1 = int(input("Enter 1 for Naukri.com and 2 for indeed.co.in 3 for both : "))
    if platform1 == 1:
        totaljobs1 = 40735  + 22572
        pyjobs1 = 22572
        probability = 22572 / (40735  + 22572)
        print("The probability of getting employed is : " , probability)
        print("The probability of not getting employed is : " , 1 - probability )
    elif platform1 == 2:
         totaljobs2 = 29566 + 9712
         pyjobs2 = 9712
         probability = 9712 / (29566 + 9712)
         print("The probability of getting employed is : " , probability)
         print("The probability of not getting employed is : " , 1 - probability )
    elif platform1 == 3:
         totaljobs3 = 29566 + 9712 + 40735  + 22572
         pyjobs3 = 9712 + 22572
         probability = (9712 + 22572) / (29566 + 9712 + 40735  + 22572)
         print("The probability of getting employed is : " , probability)
         print("The probability of not getting employed is : " , 1 - probability )
elif Skill == 2:
    platform2 = int(input("Enter 1 for Naukri.com and 2 for indeed.co.in 3 for both : "))
    if platform2 == 1:
        totaljobs1 = 40735  + 22572
        jjobs1 = 40735
        probability = 40735 / (40735  + 22572)
        print("The probability of getting employed is : " , probability)
        print("The probability of not getting employed is : " , 1 - probability )
    elif platform2 == 2:
         totaljobs2 = 29566 + 9712
         jjobs2 = 29566
         probability = 29566 / (29566 + 9712)
         print("The probability of getting employed is : " , probability)
         print("The probability of not getting employed is : " , 1 - probability )
    elif platform2 == 3:
         totaljobs3 = 29566 + 9712 + 40735  + 22572
         jjobs3 = 40735 + 29566
         probability = (40735 + 29566) / (29566 + 9712 + 40735  + 22572)
         print("The probability of getting employed is : " , probability)
         print("The probability of not getting employed is : " , 1 - probability )
    
elif Skill == 3:
    print("Probability of getting employed is 1 and probability of not getting employed is 0")
else:
    print("INVALID INPUT!!!\nRE-RUN the program \nPlease Enter 1 for Python or 2 for Java or 3 for both ")
