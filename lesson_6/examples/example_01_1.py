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


# create object
auto = Auto()

# get attributes
print(f'name: {auto.auto_name}',
      f'model: {auto.auto_model}',
      f'year: {auto.auto_year}',
      sep='\n')

# apply methods
auto.on_auto_start()
auto.on_auto_stop()
