def forward(num):
        bag=""
        for i in range(0,len(num)):
            bag+=num[i]
        return bag

if __name__=="__main__":
    forward()