# # this the codes to change the file in python and here the result

# f= open('myfile.txt', 'r')

# a= f.read()
# f.close()
# print(a)
# # while True:
# #     line =  f.readline()
# #     if not line:
# #         break
# #     print(line)


# this the codes to change the file in python and here the result
f = open('myfile.txt', 'r')
# print(f)
i = 0
while True:
    i =i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f'marks of student {i} in maths is: {m1}')
    print(f'marks of student {i} in sst is: {m2}')
    print(f'marks of student {i} cs is: {m3}\n')
    
    # print(line)


# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")
