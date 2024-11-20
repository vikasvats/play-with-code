# kaun banega carorpati
'''please try the game it is fun'''

questions=[
    ['Which language was used to create fb?',"python","French","javascript","Php","None",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","None",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","None",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","None",4],
    ['Which language was used to create fb?',"python","French","javascript","Php","None",4],
           ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,16000,32000]

for i in range(0, len(questions)):
    question=questions[i]
    print(f"Question for rs.{levels[i]}")
    print(f"Here is your question:\n{question[]}")
    print(f"a. {question[1]}            b.{question[2]} ")
    print(f"c. {question[3]}            d.{question[4]} ")
    reply = int(input("Enter your answer (1-4): "))
    if(reply == questions[-1]):
        print(f"correct answer, you have won rs.{levels[i]}")