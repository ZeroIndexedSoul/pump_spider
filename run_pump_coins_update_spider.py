import os
from scrapy import cmdline
from multiprocessing import Process


def start_crawl():
    command = f'scrapy crawl pump_coins_update_spider'
    cmdline.execute(command.split())


if __name__ == '__main__':
    process_count = 8
    processes = []

    for _ in range(process_count):
        p = Process(target=start_crawl)  # 实例化一个进程对象
        processes.append(p)
        p.start()  # 开启一个子进程
        print(f"processes start, pid:{os.getpid()}")

    # 等待所有进程执行完毕
    for p in processes:
        p.join()
