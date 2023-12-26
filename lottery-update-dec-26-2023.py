import random

class LotteryFactory:
    @staticmethod
    def generate_numbers(start, end, count):
        numbers = random.sample(range(start, end + 1), count)
        numbers.sort()
        return numbers

    @staticmethod
    def generate_multiple_sets(times, start, end, count):
        return [LotteryFactory.generate_numbers(start, end, count) for _ in range(times)]

def display_menu():
    print('\n\nSelect an option:\n')
    print('1. Nebraska Pick Three')
    print('2. Nebraska Pick Five')
    print('3. Powerball picks')
    print('4. Mega Millions picks')
    print('Q. Quit')

def process_choice(choice):
    if choice == '1':
        print('\nNebraska Pick Three:', LotteryFactory.generate_multiple_sets(3, 0, 9, 1))
    elif choice == '2':
        print('\nNebraska Pick Five:', LotteryFactory.generate_numbers(1, 38, 5))
    elif choice == '3':
        print('\nPowerball:', LotteryFactory.generate_numbers(1, 55, 5), LotteryFactory.generate_numbers(1, 42, 1))
    elif choice == '4':
        print('\nMega Millions:', LotteryFactory.generate_numbers(1, 75, 5), LotteryFactory.generate_numbers(1, 15, 1))

def worker_function():
    while True:
        display_menu()
        choice = input('\nEnter your choice: ').lower()

        if choice.startswith('q'):
            print("Done! Thanks for playing.")
            break
        else:
            process_choice(choice)

if __name__ == '__main__':
    worker_function()
