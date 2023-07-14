def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class VendingFSM:
    def __init__(self):
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()
        self.juiceA = self._create_juiceA()
        self.juiceB = self._create_juiceB()
        self.juiceC = self._create_juiceC()


        self.current_state = self.q1
        self.stopped = False

    def send(self, char):
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        if self.stopped:
            return False
        return self.current_state == self.q3


    @prime
    def _create_q1(self):
        while True:
            char = yield
            print("Hello and Welcome! Pls choose one of the juices. \n\n.........\n")
            x = input("Enter the code of the juice you would like: ")
            if char == 'a':
                self.current_state = self.juiceA
            elif char == 'b':
                self.current_state = self.juiceB
            elif char == 'c':
                self.current_state = self.juiceC
            else:
                self.current_state = self.q1

    @prime
    def _create_q2(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2
            elif char == 'c':
                self.current_state = self.q3
            else:
                break

    @prime
    def _create_juiceA(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2
            elif char == 'c':
                self.current_state = self.q3
            else:
                break

    @prime
    def _create_q3(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2
            else:
                break


def grep_regex(text):
    vending_machine = VendingFSM()
    for ch in text:
        vending_machine.send(ch)
    return vending_machine.does_match()


print(grep_regex('ab'))
