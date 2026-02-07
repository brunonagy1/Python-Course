import asyncio

async def f1(x1:float,x2:float)->float:
    print(f"first number {x1} \n second number {x2}")
    await asyncio.sleep(2)
    return 2*x1+2*x2

asyncio.run(f1(1,2))