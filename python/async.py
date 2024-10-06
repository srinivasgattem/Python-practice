import asyncio

async def function1():
    await asyncio.sleep(1)
    print("hiii")
    #print("harry")
    return "harry"
async def function2():
    await asyncio.sleep(1) 
    print("good") 
async def function3():
    await asyncio.sleep(4)
    print("morning")
    
async def main():
    #task=asyncio.create_task(function1())
    #await function1()
   # await function2()          
   # await function3()
   L=await asyncio.gather(
          function1(),
          function2(),
          function3(),
   )
   print(L)
    
asyncio.run(main())    