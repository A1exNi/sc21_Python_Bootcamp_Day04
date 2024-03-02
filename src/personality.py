import random


def main():
    test()


def test():
    turrets = turrets_generator()
    print(type(turrets))
    print(next(turrets))
    for i in range(2):
        print(f'==============Info turret {i+1}==================')
        turret = next(turrets)
        turret.shoot()
        turret.search()
        turret.talk()
        personality_traits = [
            turret.neuroticism,
            turret.openness,
            turret.conscientiousness,
            turret.extraversion,
            turret.agreeableness
        ]
        print(personality_traits, f'Sum: {sum(personality_traits)}')


def turrets_generator():
    def shoot(self):
        print('Shooting')

    def search(self):
        print('Searcing')

    def talk(self):
        print('Talking')

    while True:
        personality_traits = [random.randint(0, 100) for i in range(5)]
        if sum(personality_traits) == 100:
            Turret = type(
                'Turret',
                (object, ),
                dict(
                    shoot=shoot,
                    search=search,
                    talk=talk,
                    neuroticism=personality_traits[0],
                    openness=personality_traits[1],
                    conscientiousness=personality_traits[2],
                    extraversion=personality_traits[3],
                    agreeableness=personality_traits[4]
                )
            )
            yield Turret()


if __name__ == '__main__':
    main()
