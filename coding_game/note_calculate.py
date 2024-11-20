total=100
n=10
arr=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,20,50,20]
# ten rupess note/coin not acceptable

sum=0
for i in range(0,len(arr)):
    if sum==100:
        print(f"mil gya solution {sum}")
    else:
        sum+=arr[i]

