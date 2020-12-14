while True:
    n = int(input('input prime number:'))

    if n > 1:
        i = 2
        while i < n:
            if n % 2 == 0:
                break
            i += 1
        if i == n:
            print(n, "is a prime number")
            break

    print(n, "isn't a prime number")
