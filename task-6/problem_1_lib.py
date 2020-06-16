from time import sleep


class TrafficLight:
    def __init__(self, mode):
        self.__mode = mode

    def running(self, n):
        for _ in range(n):
            for c, t in self.__mode:
                for s in range(t):
                    print(f'\r{c:>6}:{t - s:>02d}', end='')
                    sleep(1)
        print()
