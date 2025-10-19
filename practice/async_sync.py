import asyncio
async def boil():
    print("Boil the rice")
    await asyncio.sleep(5)
    print("Rice boiled")
async def cook():
    print("Cook the Handi")
    await asyncio.sleep(3)
    print("Handi cooked")
async def main():
    await asyncio.gather(
        boil(),
        cook()
    )
asyncio.run(main())  