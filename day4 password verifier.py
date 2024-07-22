# password verifier
# mrX is trying to create a new password for his instagram account these are the required condition for creating a new password
# con1:min length is 8 max length is 15
# con2:only @,/ is allowed in a password
# con3:no spaces are allowed
# con4:only aplha numerics are allowed
# you are supposed to print weak if length is exact 8
# medium length medium 8 to 12
# strong if length is between 12 to 15
n=input("enter the string")
str=["@","/"]
n1=len(n)
c=0
for i in n:
    if(i==str[0] or i==str[1] and i==" "):
        c+=1
        break
if c==0 and n1==8:
    print("password is weak")
elif c>=1 and (n1>=8 and n1<=12):
    print("password is medium")
elif c>=1 and (n1>=12 and n1<=15):
    print("password is strong")

       
