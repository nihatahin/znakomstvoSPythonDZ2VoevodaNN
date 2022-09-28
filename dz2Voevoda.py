from curses.ascii import isdigit
from random import randrange
from re import S


def taskChoice():
    while True:
        global taskNum
        taskNum = int(input("Enter task number: "))
        if 0 < taskNum <= maxTaskNum:
            return
        else:
            print("Invalid task number was entered. Please, try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------            
def taskFuncChoice():
    global taskNum
    match taskNum:
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()
        case _:
            print('Invalid task number')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task1():
    print('Task #1.')
    while True:
        realNum = input("Enter real number or '/break' to change task: ")
        if realNum == '/break':
            return
        else:
            print(f"The digit sum of {realNum} is {digitSum(realNum)}.")
#--------------------------------------------------------------------
def digitSum (num):
    sum = 0
    for i in range(len(num)):
        if isdigit(num[i]):
            sum += int(num[i])
    return sum
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task2():
    print('Task #2.')
    while True:
        intNum = input("Enter positive integer number or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 1:
            print("Invalid integer. Try again.")
        else:
            print(f"The factorial subsequence from 1 to {intNum} is {factorialSubseq(int(intNum))}.")
#-------------------------------------------------------------------- 
def factorialSubseq(num):
    f_list = [1]
    for i in range(2, num+1):
        f_list.append(f_list[i - 2] * i)
    return f_list
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task3():
    print('Task #3.')
    while True:
        intNum = input("Enter positive integer number or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 1:
            print("Invalid integer. Try again.")
        else:
            sequence = seqList(int(intNum))
            print(f'The (1+1/n)^n subsequence list of {intNum} numbers is {sequence}.')
            print(f'The rounded sum of numbers is {sumSeqList(sequence)}.')
#--------------------------------------------------------------------
def seqList(num):
    s_list = []
    for i in range(1, num + 1):
        s_list.append(round((1+1/i)**i, 3))
    return s_list
#--------------------------------------------------------------------
def sumSeqList(seq):
    sum = 0
    for i in range(len(seq)):
        sum += seq[i]
    return sum
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task4():
    print('Task #4.')
    while True:
        intNum = input("Enter positive integer number or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 1:
            print("Invalid integer. Try again.")
        else:
            sequence_list = seqMinPl(int(intNum))
            print(f"The sequence from {-1*intNum} to {intNum} is {sequence_list}.")
            print(f"Multiplication result is {prodProc(sequence_list)}.")
#--------------------------------------------------------------------
def seqMinPl(num):
    mp_list = []
    for i in range(num ):
        mp_list.append(randrange(-num, num+1))
    return mp_list
#--------------------------------------------------------------------
def prodProc(seq):
    max = len(seq)
    while True:
        a = int(input("Enter position of the first multiplier: "))
        if (a >= max) or (a < 0):
            print("Invalid position. Try again.")
            continue
        b = int(input("Enter position of the second multiplier: "))
        if (b >= max) or (b < 0):
            print("Invalid position. Try again.")
            continue
        break
    return seq[a] * seq[b]
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task5():
    print('Task #5.')
    while True:
        intNum = input("Enter integer number (>= 2) or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 2:
            print("Invalid integer. Try again.")
        else:
            sequence_list = listCreation(int(intNum))
            print(f"Before mix list - {sequence_list}.")
            print(f"After mix list - {listMix(sequence_list)}.")
#--------------------------------------------------------------------
def listCreation(num):
    cr_list = []
    for i in range(num):
        cr_list.append(randrange(-10, 11))
    return cr_list
#--------------------------------------------------------------------
def listMix(seq):
    num = len(seq)
    randIndex = None
    buffer = None
    for i in range(num):
        randIndex = randrange(num)
        buffer = seq[randIndex]
        seq[randIndex] = seq[i]
        seq[i] = buffer
    return seq
#####################################################################
#####################################################################
##################################################################### 
taskNum = None
maxTaskNum = 5

while True:
    taskChoice()
    print()
    taskFuncChoice()
    print()

    
    