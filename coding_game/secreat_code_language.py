''' there is a secreat code words
coding if the words contain at lest remove 1st word and append in last part
for example harry arryh
now append 3 random latters front and back

making coding and decodind app
'''
import random

# enter = ""

# def entry1(enter):
    
#     r = len(enter)
#     for i in range(0,r):
#         entry == enter[i] 
        
#         first_name_slicer(entry)
bag=""
new_bag = ""

final=""
final2=""

def start():

    entry = input("Enter your word want to decode: ")
    # a = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    alpha = str(('abcdefghijklmnopqrstuvwxyz'))

    # val = random.choice(alpha)


    def first_name_slicer(entry):
        global bag
        global new_bag
        n=len(entry)
        for i in range(0,n):
            if n>3:
                bag+=entry[0]
                new_bag=entry[1:]
                
                return new_bag+bag
                
                
                break

    first = first_name_slicer(entry)
    # print(first)



    # first_name_slicer()
    def random_str(val):
        global final

        global final2

        val = random.choices(val,k=24)
        N = len(val)
        for i in range(0,3):
            final+=val[i]
            final2+=val[i+2]

        
            # final+=val[0:2]+first_name_slicer()+val[N:N-3]
        
    random_str(alpha)
    # random_str(val)
    # print(final)

    if __name__ == "__main__":

        print(final+first+final2)


start()










