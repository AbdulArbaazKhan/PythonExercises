import multiprocessing
import time
import concurrent.futures


def func(sec):
    print(f"Sleeping for {sec}")
    time.sleep(sec)


processes = []
if __name__ == '__main__':
    #     for i in range(10):
    #         p = multiprocessing.Process(target=func, args=[i])
    #         p.start()
    #         processes.append(p)
    #
    # for p in processes:
    #     p.join()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l = [1, 3, 4, 5, 6, 7, 7]
        results = executor.map(func, l)
