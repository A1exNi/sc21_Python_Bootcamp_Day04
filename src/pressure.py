from random import randint
from time import sleep


def main():
    test()


def test():
    v = valve()
    for i in v:
        print(i)
        sleep(1)


def emit_gel(step: int):
    pressure = 50
    sign_step = 1
    exit = False
    while not exit:
        random_step = randint(0, step)
        i = yield pressure
        if i is not None:
            sign_step *= i
        pressure += random_step*sign_step


def valve():
    g = emit_gel(16)
    sign_step = 1
    while True:
        pressure = next(g)
        yield pressure
        if pressure < 20 and sign_step == -1:
            sign_step = 1
            g.send(-1)
        elif pressure > 80 and sign_step == 1:
            sign_step = -1
            g.send(-1)
        if pressure < 10 or pressure > 90:
            g.close()


if __name__ == '__main__':
    main()
