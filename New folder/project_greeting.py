import time
timeframe=int(time.strftime("%H"))
# print(timeframe)

if timeframe<12 or timeframe>5:
    print("Good Morning sir")
elif timeframe==12 or timeframe>=4:
    print("Good Afternoon sir")
else:
    print("good evening")
