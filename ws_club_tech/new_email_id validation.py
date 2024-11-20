# this is the code that is written from the scrached 
# lets move on to the topic of the email validation
# vikaschaudhary@gmail.com
# v@k.in

def email_validator():
    email = input("Enter your email hear: ").lower()
    k = 0
    if email[0].isalpha():
        if (email[-3]==".") ^ (email[-4]=="."):
            
            if ("@" in email) and (email.count("@") == 1 ):
                for i in email:
                    # if i==i.isspace():
                    if i == " ":
                         k=1
                if k==1:

                    print("Wrong email id space problem 4")
                else:
                    print("this email is correct")


            else:
                print("wrong email id @ 3")


        else:           
            print("Wrong email id alpha 2")                
    else:
        print("Wrong email id alpha 1") 

if __name__=="__main__":
    
    email_validator()

# this email validator is working fine but i still have a way :)

