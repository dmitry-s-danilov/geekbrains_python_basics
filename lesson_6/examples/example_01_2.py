class Auto:
    # class attributes
    auto_name = 'Lexus'
    auto_model = 'RX 350L'
    auto_year = 2018

    # class methods
    def on_auto_start(self):
        print(f'{self.auto_name} start.')

    def on_auto_stop(self):
        print(f'{self.auto_name} stop.')


# create objects
auto = [Auto(), Auto()]

# display objects
for _ in enumerate(auto, 1):
    print(_[0], _[1], type(_[1]))

# compare objects
print(f' == : {auto[0] == auto[1]}',
      f' is : {auto[0] is auto[1]}',
      sep='\n')
