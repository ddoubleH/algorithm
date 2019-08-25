class queue():

    def __init__(self):
        self.queue = []
        self.len = 0

    def push(self, N):
        self.queue.append(N)
        self.len += 1

    def pop(self):
        try:
            delete = self.queue[0]
            del self.queue[0]
            self.len -= 1
            return delete
        except:
            return -1

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def size(self):
        return len(self.queue)

    def front(self):
        if queue is None:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if queue is None:
            return -1
        else:
            return self.queue[-1]


if __name__ == '__main__':
    N = int(input())
    Q = queue()

    while(N > 0):
        N -= 1
        Input = input().split()

        word = Input[0]

        if word == 'quit' or word == 'q':
            break

        elif word == 'push':
            Q.push(Input[1])

        elif word == 'pop':
            print(Q.pop())

        elif word == 'empty':
            print(Q.empty())

        elif word == 'size':
            print(Q.size())

        elif word == 'front':
            print(Q.front())

        elif word == 'back':
            print(Q.back())

        else:
            print('Command Not Found')
