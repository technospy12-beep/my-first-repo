class animal:
    

  class prey:
    def flee(self):
        print(f"this animal is fleeing")


class predature:
    def hunt(self):
        print(f"this animal is hunting")

class Rabbit(prey):
    pass

class hawk(predature):
    pass

class Fish(prey,predature):
    pass



rabbit = Rabbit()
hawk = hawk()
fish = Fish()


fish.flee()