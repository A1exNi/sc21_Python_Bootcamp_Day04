
def main():
    test1()
    test2()
    

def test1():
    print('===============TEST1===================')
    plugs = ['plug1', None, 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 1, 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4', 1]
    iter = fix_wiring(cables, sockets, plugs)
    for c in iter:
        print(c)


def test2():
    print('===============TEST2===================')
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    iter = fix_wiring(cables, sockets, plugs)
    for c in iter:
        print(c)


def fix_wiring(cables, sockets, plugs):
    return map(
        lambda x: f'plug {x[0]} into {x[1]} using {x[2]}' if x[2] else f'weld {x[0]} to {x[1]} without plug',
        zip(
            filter(lambda cable: isinstance(cable, str), cables),
            filter(lambda socket: isinstance(socket, str), sockets),
            list(
                filter(
                    lambda plug: isinstance(plug, str),
                    plugs
                )
            ) 
            + [None]
            * (len(
                    list(
                        zip(
                            filter(lambda cable: isinstance(cable, str), cables),
                            filter(lambda socket: isinstance(socket, str), sockets)
                        )   
                    )
                )
                - len(
                    list(
                        filter(
                            lambda plug: isinstance(plug, str),
                            plugs
                        )
                    )
                )
            )
        )
    )


if __name__ == '__main__':
    main()
