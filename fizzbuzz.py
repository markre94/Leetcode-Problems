def play_fizz_buzz():
    for i in range(1, 100):
        output = ''

        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'

        if output == '':
            print(i)
        else:
            print(output)

print(play_fizz_buzz())
