def convert_time(x,y):
    time_24_hour=x*y
    time_24_hour%=24
    if time_24_hour==0:
        return "12AM"
    elif 1<=time_24_hour<=11:
        return f"{time_24_hour}AM"
    elif time_24_hour==12:
        return "12PM"
    else:
        return f"{time_24_hour-12}PM"
x=3
y=5
result=convert_time(x,y)    
print(f"usual time is:{result} ")