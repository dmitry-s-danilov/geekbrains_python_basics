my_list = [_ for _ in range(20, 240 + 1) if not _ % 20 or not _ % 21]

my_list_1 = []
for x in range(20, 240 + 1):
    if x % 20 == 0 or x % 21 == 0:
        my_list_1.append(x)

my_list_2 = list(filter(lambda _: _ % 20 == 0 or _ % 21 == 0,
                        range(20, 240 + 1)))

my_check = my_list == my_list_1 == my_list_2

print(f'list: {my_list}\ncheck: {my_check}')
