############ CHECK IF QUEUE IS FULL #################

def IsFull():
    global QueueTail
    global MaxSize
    if (QueueHead == (QueueTail + 1) % MaxSize):
        # THEN
        QueueFull = True
    else:
        QueueFull = False
    # ENDIF
    return QueueFull

#END IsFull.

def IsFull2():
    global QueueTail
    return(QueueHead == (QueueTail + 1) % MaxSize)
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
    global MaxSize
    if (IsFull() == True):
        # THEN
        print("The Queue is full")
    else:
        QueueTail = (QueueTail + 1) % MaxSize
        Queue[QueueTail] = N
    # ENDIF

#END AddToQ.


#####################################################

############## DELETE FROM THE QUEUE ################

def DeleteFromQ():
    global QueueHead    
    global MaxSize
    N = 0
    if (IsEmpty() == True):
        # THEN
        print("The Queue is Empty")
    else:
        N = Queue[QueueHead]
        QueueHead = (QueueHead + 1) % MaxSize
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
QueueTail =  3


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
AddToQ(9999)
print(Queue)
AddToQ(9999)
print(Queue)


#END QueueAsArray.

