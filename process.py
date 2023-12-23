import multiprocessing


def worker(queue):
    """进程函数"""
    # 从队列中获取任务数据
    task = queue.get()
    while task:
        # 处理任务
        print(f"Worker processing task: {task}")
        if queue.empty():
            break
        task = queue.get()


if __name__ == '__main__':

    # 创建队列，用于进程之间的通信
    queue = multiprocessing.Manager().Queue()

    # 创建进程池，包含4个进程
    with multiprocessing.Pool(processes=4) as pool:

        # 创建100000个任务，并将它们添加到队列中
        for i in range(1, 100001):
            queue.put(i)

        # 提交任务到进程池，每个任务都会调用worker函数进行处理
        pool.map(worker, [queue]*4)

    print("All workers have finished")
