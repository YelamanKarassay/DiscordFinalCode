import random


def _numberToEmoji_(n):
    if n == "0":
        return ":zero:"
    elif n == "1":
        return ":one:"
    elif n == "2":
        return ":two:"
    elif n == "3":
        return ":three:"
    elif n == "4":
        return ":four:"
    elif n == "5":
        return ":five:"
    elif n == "6":
        return ":six:"
    elif n == "7":
        return ":seven:"
    elif n == "8":
        return ":eight:"
    elif n == "9":
        return ":nine:"
    else:
        return n


class InvalidInput(Exception):
    def __init__(self, message):
        self.message = message


class InputField:
    def __init__(self, digits):
        """Creates a InputField for a password with the given number of digits."""
        self.size = digits
        self.password = [":cd:" for i in range(digits)]
        self.rightNumberAndPosition = 0
        self.rightNumber = 0

    def __str__(self):
        ret = ""
        for x in self.password:
            ret += _numberToEmoji_(x) + " "

        ret += "    "

        for i in range(self.rightNumberAndPosition):
            ret += ":green_circle:  "
        for i in range(self.rightNumber):
            ret += ":yellow_circle:  "
        for i in range(self.size - self.rightNumber - self.rightNumberAndPosition):
            ret += ":red_circle:  "

        return ret

    def fill(self, playerAnswer, correctAnswer):
        """Put the player answer in the pasword field."""
        if len(playerAnswer) != self.size:
            raise InvalidInput("Given password is invalid")

        for digit in playerAnswer:
            if not digit.isnumeric():
                raise InvalidInput("Given password is invalid")

        if len(set(playerAnswer)) != len(playerAnswer):
            raise InvalidInput("Given password is invalid")

        for i in range(self.size):
            self.password[i] = playerAnswer[i]

        self.checkAnswer(correctAnswer)

    def checkAnswer(self, correctAnswer):
        """Check how many digits are present in the answer and how many are in correct positions."""
        for i in range(self.size):
            if correctAnswer[i] in self.password:
                if correctAnswer[i] == self.password[i]:
                    self.rightNumberAndPosition += 1
                else:
                    self.rightNumber += 1

    def solved(self):
        return self.rightNumberAndPosition == self.size


class Level:
    def __init__(self, passwordSize, numberOfAttempts):
        """Create a level with certain password size and max number of attempts."""
        self.passwordSize = passwordSize
        self.numberOfAttempts = numberOfAttempts

        self.password = ""
        for i in range(passwordSize):
            x = str(random.randint(0, 9))
            while x in self.password:
                x = str(random.randint(0, 9))

            self.password += x

        self.attempts = [InputField(passwordSize) for i in range(numberOfAttempts)]

        self.currentAttempt = 0

        self.solved = False

    def __str__(self):
        ret = ""

        for x in self.password:
            ret += (_numberToEmoji_(
                x) if self.solved == True or self.currentAttempt == self.numberOfAttempts else ":asterisk:") + " "
        ret += ("   :unlock:" if self.solved == True else "   :lock:") + "\n\n"

        for attempt in self.attempts:
            ret += str(attempt) + "\n"

        return ret

    def tryAnswer(self, attempt):
        try:
            self.attempts[self.currentAttempt].fill(attempt, self.password)
        except Exception as exc:
            raise exc

        self.solved = self.attempts[self.currentAttempt].solved()
        self.currentAttempt += 1


class Game:
    difficulty = [(3, 10), (4, 10), (5, 10)]
    WON = 1
    PLAYING = 0
    LOST = -1

    def __init__(self):
        self.currentDifficulty = 0

        self.status = self.PLAYING
        self.active = True

        self.level = Level(*self.difficulty[0])

    def __str__(self):
        ret = ""

        if self.active == True:
            ret = f":regional_indicator_l: :regional_indicator_e: :regional_indicator_v: :regional_indicator_e: :regional_indicator_l:    {_numberToEmoji_(str(self.currentDifficulty + 1))}\n\n"
            ret += str(self.level)

        return ret

    def startNextLevel(self):
        if self.currentDifficulty < 2:
            self.currentDifficulty += 1
            self.status = self.PLAYING
            self.active = True
            self.level = Level(*self.difficulty[self.currentDifficulty])

    def attempt(self, playerAttempt):
        at = playerAttempt.split()
        at = "".join(at)

        try:
            self.level.tryAnswer(at)
        except Exception as exc:
            raise exc

        if self.level.solved:
            self.status = self.WON
        elif self.level.currentAttempt == self.difficulty[0][1]:
            self.status = self.LOST