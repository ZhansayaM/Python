import random
import time


class CantMove(Exception):
    def __init__(self, reason):
        self.__reason = reason

    def __repr__(self):
        return "unable to find a move: {}".format(self.__reason)


class Nim:
    def __init__(self, startstate):
        self.state = startstate

    # Goal is to be unambiguous :

    def __repr__(self):
        word = ""
        for x in range(len(self.state)):
            word += str(x + 1)
            word += ("  : ")
            for y in range(self.state[x]):
                word += "1 "
            word += "\n"
        return word

    # Return sum of all rows:

    def sum(self):
        num = 0
        for x in range(len(self.state)):
            num += int(self.state[x])
        return num

    # Return nimber (xor of all rows):

    def nimber(self):
        nimb = int(self.state[0])
        for x in range(len(self.state)):
            if x != 0:
                nimb ^= int(self.state[x])
        return nimb

    # Make a random move, raise a CantMove if
    # there is nothing left to remove.

    def randommove(self):
        if self.sum() == 0:
            raise CantMove("no sticks left")
        else:
            while True:
                rows = random.randrange(0, len(self.state), 1)
                if self.state[rows] != 0:
                    break
            self.state[rows] = random.randrange(0, self.state[rows])

    # Try to force a win with misere strategy.
    # This functions make a move, if there is exactly
    # one row that contains more than one stick.
    # In that case, it makes a move that will leave
    # an odd number of rows containing 1 stick.
    # This will eventually force the opponent to take the
    # last stick.
    # If it cannot obtain this state, it should raise
    # CantMove( "more than one row has more than one stick" )

    def removelastmorethantwo(self):
        count = 0
        count2 = 0
        for x in range(len(self.state)):
            if (self.state[x]) > 1:
                count += 1
                y = x
            if self.state[x] == 0:
                count2 += 1
        if count == 1:
            if (len(self.state)-count2) % 2 == 0:
                self.state[y] = 0
            elif (len(self.state)-count2) % 2 == 1:
                self.state[y] = 1
        elif count > 1 or count == 0:
            raise CantMove("more than one row has more than one stick")

    # Try to find a move that makes the nimber zero.
    # Raise CantMove( "nimber is already zero" ), if the
    # nimber is zero already.

    def makenimberzero(self):
        if self.nimber() == 0:
            raise CantMove("nimber is already zero")
        else:
            count = False
            while not count:
                rowrand = random.randrange(len(self.state))
                if self.state[rowrand] ^ self.nimber() < self.state[rowrand]:
                    self.state[rowrand] = self.state[rowrand] ^ self.nimber()
                    count = True


    def optimalmove(self):
        try:
            self.removelastmorethantwo()
        except CantMove:
            try:
                self.makenimberzero()
            except CantMove:
                self.randommove()

    # Let the user make a move. Make sure that the move
    # is correct. This function never crashes, not
    # even with the dumbest user in the world.

    def usermove(self):
        while True:
            row = input("Please, enter the number of the row: ")
            if not row.isdigit() or int(row) <= 0:
                print("Please, enter a positive integer")
            elif int(row) > len(self.state) or self.state[int(row)-1] == 0:
                print("Please, enter the row that exists")
            elif row.isdigit() and 0 < int(row) <= len(self.state):
                break
        a = int(row)
        while True:
            stick = input("Please, enter the number of remaining sticks: ")
            if not stick.isdigit():
                print("Please, enter a positive integer")
            elif int(stick) >= self.state[a-1]:
                print("You're trying to do an impossible thing! Please, try again")
            elif stick.isdigit() and int(stick) < self.state[a-1]:
                break
        self.state[a-1] = int(stick)

    def play():
        st = Nim([1, 2, 3, 4, 5, 6])
        turn = 'user'
        while st.sum() > 1:
            if turn == 'user':
                print("\n")
                print(st)
                print("hello, user, please make a move")
                st.usermove()
                turn = 'computer'
            else:
                print("\n")
                print(st)
                print("now i will make a move\n")
                print("thinking")
                for r in range(15):
                    print(".", end="", flush=True)
                    time.sleep(0.1)
                print("\n")

                st.optimalmove()
                turn = 'user'
        print("\n")
        if turn == 'user':
            print("you lost\n")
        else:
            print("you won\n")
