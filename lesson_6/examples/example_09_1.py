class Player:
    def player_method(self):
        print('player method')

class Navigator:
    def navigator_method(self):
        print('navigator method')

class Mobile(Player, Navigator):
    def mobile_method(self):
        print('mobile method')


player = Player()
print(type(player))
player.player_method()

print()

navigator = Navigator()
print(type(navigator))
navigator.navigator_method()

print()

mobile = Mobile()
print(type(mobile))
mobile.player_method()
mobile.navigator_method()
