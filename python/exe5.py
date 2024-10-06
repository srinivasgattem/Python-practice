import os
files=os.listdir("clutterfolder")
i =0
for file in files:
    print(file)
    os.rename(f"clutterfolder/{file}",f"clutterfolder/{i}.png") 
    i=i+1