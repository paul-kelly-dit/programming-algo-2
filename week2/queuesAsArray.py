############ CHECK IF QUEUE IS FULL #################

def IsFull():
    global QueueTail
    if (QueueTail + 1 == MaxSize):
        # THEN
        QueueFull = True
    else:
        QueueFull = False
    # ENDIF
    return QueueFull

#END IsFull.

def IsFull2():
    global QueueTail
    return(QueueTail + 1 == MaxSize)
#END IsFull2.

#####################################################


############ CHECK IF QUEUE IS EMPTY #################

def IsEmpty():
    global QueueTail
    global QueueHead    
    if (QueueTail == QueueHead):
        # THEN
        QueueEmpty = True
    else:
        QueueEmpty = False
    # ENDIF
    return QueueEmpty

#END IsEmpty.

def IsEmpty2():
    global QueueTail
    global QueueHead    
    return(QueueTail == QueueHead)
#END IsEmpty2.

#####################################################

############### ADD INTO THE QUEUE #################

def AddToQ(N):
    global QueueTail
    if (IsFull() == True):
        # THEN
        print("The Queue is full")
    else:
        QueueTail = QueueTail + 1
        Queue[QueueTail] = N
    # ENDIF

#END AddToQ.


#####################################################

############## DELETE FROM THE QUEUE ################

def DeleteFromQ():
    N = 0
    global QueueHead    
    if (IsEmpty() == True):
        # THEN
        print("The Queue is Empty")
    else:
        N = Queue[QueueHead]
        QueueHead = QueueHead + 1
    # ENDIF
    return N

#END DeleteFromQ.


#####################################################


################ CLEAR QUEUE ##################

def ClearQ():
    global QueueTail
    global QueueHead    

    QueueTail = -1
    QueueHead = QueueTail

#END ClearQ.


#####################################################


# PROGRAM QueueAsArray:

Queue = [31,41,59,26,53,59,67]
MaxSize = 7
QueueHead =  0
QueueTail =  1


AnswersFull = IsFull()
print(AnswersFull)
AnswersFull2 = IsFull2()
print(AnswersFull2)

AnswersEmpty = IsEmpty()
print(AnswersEmpty)
AnswersEmpty2 = IsEmpty2()
print(AnswersEmpty2)

print(Queue)
AddToQ(9999)
print(Queue)
x1 = DeleteFromQ()
print(x1)
x2 = DeleteFromQ()
print(x2)
x3 = DeleteFromQ()
print(x3)
x4 = DeleteFromQ()
print(x4)
x5 = DeleteFromQ()
print(x5)
x6 = DeleteFromQ()
print(x6)
print(Queue)
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)


#END QueueAsArray.

