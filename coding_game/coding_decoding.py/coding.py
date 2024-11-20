# import random

# alpha = "abcdefghijklmnopqrstuvwxyz"

# def coding_sentence():
#     entry = input("Enter your sentence you want to decode: ")
#     words = entry.split() 
#     coded_words = select(words)
#     return coded_words

# def select(words):
#     coded_words = []
#     for word in words:
#         coded_word = coding_word(word)
#         coded_words.append(coded_word)
#     return ' '.join(coded_words)

# def coding_word(word):
#     if len(word) > 3:
#         first = word[0]
#         rest = word[1:]
#         return rest + first
#     else:
#         return word

# # Example usage
# result = coding_sentence()
# print(result)



import random

alpha=str(("abcdefghijklmnopqrstuvwxyz"))
final = ""
final2 = ""

def coding_sentence():
    entry = input("enter your sentance you want to decode:")
    word = entry.split()
    input1 = select(word) 
    # print(word)
    return input1


def select(word):
    N = len(word)
    first=[]
    for i in range(0,N):
        first.append(word[i])
        # print(first)
        input2 = coding_word(first)
        # print(input2)
        return input2
        





def coding_word(get_in):
    # print(get_in)
    string_1 = str(get_in[0])
    # print(string_1)
    # print(type(string_1))


    first = ""
    rest = ""
    n = len(string_1)
    for i in range(0,n):
        if n>3:
            first+=string_1[0]
            rest+=string_1[1:]
        
        first1 = adding3(rest+first)
        first2 = adding3(first)
        
        return first1
    else:
        return first2
    
def adding3(three):
    val = (random.choices(alpha,k=24))
    N = len(val)
    for i in range(0,3):
        final+=val[i]
        final2+=val[i+2]
    
    # rendom_value_adding= rand+three+rand
    # print(rendom_value_adding)




# name = coding_word("names")
# print(name)
coding_sentence()



