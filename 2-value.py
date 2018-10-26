from multiprocessing import Process, Value, current_process


def target(val: Value):
    for i in range(10):
        for j in range(1000):
            val.value += i
            print('[{}] {}'.format(current_process().name, val))


if __name__ == '__main__':
    v = Value('i', 0)

    p1 = Process(target=target, args=(v, ))
    p2 = Process(target=target, args=(v, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Result: {}'.format(v.value))
