class stack():

    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, N):
        self.stack.append(N)
        self.len += 1

    def pop(self):
        try:
            delete = self.stack[-1]
            del self.stack[-1]
            self.len -= 1
            return delete
        except:
            return -1

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def size(self):
        return len(self.stack)

    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]


if __name__ == '__main__':
    N = int(input())
    S = stack()

    while(N > 0):
        N -= 1
        Input = input().split()

        word = Input[0]

        if word == 'quit' or word == 'q':
            break

        elif word == 'push':
            S.push(Input[1])

        elif word == 'pop':
            print(S.pop())

        elif word == 'empty':
            print(S.empty())

        elif word == 'size':
            print(S.size())

        elif word == 'top':
            print(S.top())

        else:
            print('Command Not Found')
