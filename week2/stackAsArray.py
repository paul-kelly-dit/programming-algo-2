


############ CHECK IF STACK IS FULL #################

def IsFull():
    global StackTop
    if (StackTop + 1 == MaxSize):
        # THEN
        StackFull = True
    else:
        StackFull = False
    # ENDIF
    return StackFull

#END IsFull.

def IsFull2():
    global StackTop
    return(StackTop + 1 == MaxSize)
#END IsFull2.

#####################################################


############ CHECK IF STACK IS EMPTY #################

def IsEmpty():
    global StackTop
    if (StackTop == -1):
        # THEN
        StackEmpty = True
    else:
        StackEmpty = False
    # ENDIF
    return StackEmpty

#END IsEmpty.

def IsEmpty2():
    global StackTop
    return(StackTop == -1)
#END IsEmpty2.

#####################################################

############### PUSH ONTO THE STACK #################

def Push(N):
    global StackTop
    if (IsFull() == True):
        # THEN
        print("The stack is full")
    else:
        StackTop = StackTop + 1
        Stack[StackTop] = N
    # ENDIF

#END IsFull.


#####################################################

################ POP OFF THE STACK ##################

def Pop():
    N = 0
    global StackTop
    if (IsEmpty() == True):
        # THEN
        print("The stack is Empty")
    else:
        N = Stack[StackTop]
        StackTop = StackTop - 1
    # ENDIF
    return N

#END IsFull.


#####################################################


################ POP OFF THE STACK ##################

def Top():
    N = 0
    global StackTop
    if (IsEmpty() == True):
        # THEN
        print("The stack is Empty")
    else:
        N = Stack[StackTop]
    # ENDIF
    return N

#END IsFull.


#####################################################


# PROGRAM StackAsArray:

Stack = [31,41,59,26,53,59,67]
MaxSize = 7
StackTop =  5


AnswersFull = IsFull()
print(AnswersFull)
AnswersFull2 = IsFull2()
print(AnswersFull2)

AnswersEmpty = IsEmpty()
print(AnswersEmpty)
AnswersEmpty2 = IsEmpty2()
print(AnswersEmpty2)

print(Stack)
Push(56)
print(Stack)
x1 = Pop()
print(x1)
x2 = Pop()
print(x2)
x3 = Pop()
print(x3)
x4 = Pop()
print(x4)
x5= Pop()
print(x5)
x6= Pop()
print(x6)
x7= Pop()
print(x7)
x8= Pop()
print(x8)
x9= Pop()
print(x9)
x10= Pop()
print(x10)
Push(56)
print(Stack)
Push(56)
print(Stack)
Push(56)
print(Stack)
Push(56)
print(Stack)


#END StackAsArray.

