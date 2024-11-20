# self written code for kbc
# from playsound import playsound
# playsound(r'C:\\Users\\vikas\\Downloads\\kbc_theme.mp3')
from playsound import playsound


questions=[
    ['Jalliyawala kand kaha hua tha',"rajasthan","bihar","amritsar","delhi","1 Phala",3],
    ['Which language was used to create fb?',"python","French","javascript","Php","2 Dusra",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","3 Teesra",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","4 Chautha",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","5 Pachwa",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","6 chatta",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","7 satwa",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","8 atthwa",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","9 nauwa",4],
           ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

total=0
for i in range(0,len(questions)):
    question=questions[i]

    
    
    print(f"{question[5]} Prashna apke screen par:\n{question[0]}")
    
    # print(question[6])
    
    print(f"A.  {question[1]}                 {question[2]}")
    print(f"C.  {question[3]}                 {question[4]}")

    # playsound(r'D:\Python\coding_game\kbc_theme.mp3')

    ans=int(input("Aapka jabab kya hai?:"))


    print(levels[i])
    if levels[i]==5000 or levels[i]==20000 or levels[i]==80000 or levels[i]==32000:
        total=levels[i]

    if ans==question[6]:
        print(f'sahi jabab aap jeet chuke hai {levels[i]}')

# checkpoints are 5000,20000,80000,32000
    else:
        # print("galat jabab")
        print(f"galat jabab {total}")
        break
