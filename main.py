# Импортируем библиотеку для работы с многопоточностью
import time
from random import random, randint
from threading import Thread

namesphilosophers = ["Сократ", "Аристотель", "Ницше", "Кант", "Руссо", "Макиавелли", "Платон", "Гоббс", "Фуко", "Конфуций"]

class fork:
    def __init__(self, number):
        # Номер вилки
        self.number = number
        # Статус вилки
        self.status = False

    # Функция вывода данных
    def printforks(self):
        print("Number fork: ", self.number)
        print("\t Status work: ", self.status)
class philosopher:

    def __init__(self, number, maxnumber):
        # Номер философа
        self.number = number
        # Имя философа
        self.name = namesphilosophers[number]
        # Время еды 10 секунд
        self.eattime = 10
        # Номер вилки для правой руки
        if number == 0:
            self.numberrightfork = maxnumber - 1
        else:
            self.numberrightfork = number - 1
        # Номер вилки для левой руки
        if number == maxnumber:
            self.numberleftfork = maxnumber
        else:
            self.numberleftfork = number
        # Переменная правая рука
        self.rightHend = False
        # Переменная левая рука
        self.leftHend = False
        self.printdates()

    # Функция вывода данных
    def printdates(self):
        print("Number philosopher: ", self.number)
        print("\tName philosopher: ", self.name)
        print("\tEat time: ", self.eattime)
        print("\tNumber right fork: ", self.numberrightfork)
        print("\tRightHend: ", self.rightHend)
        print("\tNumber left fork: ", self.numberleftfork)
        print("\tLeftHend: ", self.leftHend)

    # Функция еды
    def eat(self):
        # Для того чтобы философ поел ему неодходимы правая и левая вилка
        # Вычисляем вилки которая нужна философу
        numberLeftFork = self.number - 1
        numberRightFork = self.number + 1
        print("\tNumber philosopher: ", self.number,)
        print("\tLeftFork: ", numberLeftFork)
        print("\tRightFork: ", numberRightFork)

    # Функция ожидания(сон)
    def sleep(self, i):
        second = randint(5, 10)
        print("Поток", i, " засыпает на ", second, " секунд.")
        print("Время: ", self.eattime)
        print("Левая вилка: ", self.leftHend)
        print("Правая вилка: ", self.rightHend)
        time.sleep(second)
        print("Поток ", i, " сейчас проснулся.")

def table():
    print("Введите количество философов: ")
    input_a = int(input())
    print("Количество философов: ", input_a)
    philosophers = []
    forks = []
    for i in range(input_a):
        philosophers.append(philosopher(i, input_a))
        forks.append(fork(i))
    print("Вилки")
    #for i in range(input_a):
    #    th = Thread(target = philosopher.eat())
    #    th.start()

table()