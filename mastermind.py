import random


class Mastermind:
    def __init__(self, x=1, y=1):
        if x > 8 or x < 1:
            raise ValueError("x must be a number between 1 and 8, inclusive")
        if y < 1 or y > 10:
            raise ValueError("y must be a number between 1 and 10, inclusive")
        self.__x = x
        self.__y = y
        self.__answered = ''.join(str(random.randint(1, x)) for _ in range(y))

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new):
        self.__y = new

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new):
        self.__x = new

    def clue(self, guess):
        exact_position = sum(i == j for i, j in zip(guess, self.__answered))
        exact_color = sum(min(guess.count(k), self.__answered.count(k)) for k in set(self.__answered)) - exact_position
        return '*' * exact_position + 'o' * exact_color

    def play(self):
        print(f'Playing Mastermind with {self.__x} colors and {self.__y} positions')
        attempt = 0
        while True:
            attempt += 1
            guess = str(int(input('What us your guess?: ')))
            if len(guess) != self.__y:
                if len(guess) < self.__y:
                    print("Row is not complete!!\n")
                    continue
                else:
                    print(f"Row contained only {self.__y} positions!!\n")
                    continue
            print(f'Your guess is {guess}')
            print(Mastermind.clue(self, guess) + '\n')
            if guess == self.__answered:
                break
        print(f"You solve it after {attempt} rounds")


if __name__ == "__main__":
    x = Mastermind(6, 4)
    x.play()
