# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxStack = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.__maxStack or a >= self.__maxStack[-1]:
            self.__maxStack.append(a)

    def Pop(self):
        if self.__stack.pop() == self.__maxStack[-1]:
            self.__maxStack.pop()

    def Max(self):
        return self.__maxStack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
