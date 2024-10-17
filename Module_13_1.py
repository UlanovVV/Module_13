import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for number_ball in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {number_ball}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    man = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Apollon', 5)
    ]
    task = [asyncio.create_task(start_strongman(name, power)) for name, power in man]
    await asyncio.gather(*task)


asyncio.run(start_tournament())