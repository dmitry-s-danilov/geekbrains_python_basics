class Player:
    attribute_1 = 'player attribute'
    def method_1(self):
        print('player method')


class Navigator:
    attribute_1 = 'navigator attribute'
    def method_1(self):
        print('navigator method')


class Mobile(Player, Navigator):
    attribute_2 = 'mobile attribute'
    def method_2(self):
        print('mobile method')


player = Player()
print(type(player),
      player.attribute_1,
      sep='\n')
player.method_1()

print()

navigator = Navigator()
print(type(navigator),
      navigator.attribute_1,
      sep='\n')
navigator.method_1()

print()

mobile = Mobile()
print(type(mobile),
      mobile.attribute_1,
      mobile.attribute_2,
      sep='\n')
mobile.method_1()
mobile.method_2()
