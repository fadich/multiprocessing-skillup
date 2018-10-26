from multiprocessing import Process, current_process


def target():
    for i in range(1000):
        print('[{}] {}'.format(current_process().name, i))


if __name__ == '__main__':
    p1 = Process(target=target)
    p2 = Process(target=target)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
