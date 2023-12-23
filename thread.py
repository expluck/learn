import concurrent.futures
import re


def task(n):
    print(f"Processing {n}")
    return n


if __name__ == '__main__':
    # 创建线程池，包含4个线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # 提交任务到线程池中
        futures = executor.map(task, range(10))
        # 等待所有任务完成

        for future in futures:
            print(f"Task returned {future}")

print('我学会了git')
