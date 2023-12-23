import asyncio


async def my_coroutine(num):
    print(f"Task {num} started")
    await asyncio.sleep(num)
    result = num * 2
    print(f"Task {num} finished with result {result}")
    return result


async def main():
    tasks = [my_coroutine(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

# 运行主程序
asyncio.run(main())

