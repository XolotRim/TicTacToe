"""
Tic Tac Toe Player
"""
import copy

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    countX = sum([i.count(X) for i in board])
    countO = sum([i.count(O) for i in board])
    if (countX <= countO):
        return X
    else :
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actionsSet = set()
    if (terminal(board)):
        return None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionsSet.add((i,j))
    return actionsSet
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempBoard = copy.deepcopy(board)
    playerWithTurn = player(board)
    i = action[0]
    j = action[1]
    
    if tempBoard[i][j] == EMPTY:
        tempBoard[i][j] = playerWithTurn
    else :
        raise Exception
    
    return tempBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(len(board)):

        if board[i][0] != EMPTY :
            c = board[i][0]
            if board[i][0]==c and board[i][1]==c and board[i][2]==c :
                return c
            
        if board[0][i] != EMPTY:
            c = board[0][i]
            if board[0][i]==c and board[1][i]==c and board[2][i]==c :
                return c
            
    if board[0][0] != EMPTY :
        c = board[0][0]
        if board[0][0]==c and board[1][1]==c and board[2][2]==c :
            return c
    
    if board[0][2] != EMPTY:
        c= board[0][2]
        if board[0][2]==c and board[1][1]==c and board[2][0]==c :
            return c
        
    return None      
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winnerOfTheBoard = winner(board)
    if winnerOfTheBoard==X or winnerOfTheBoard==O:
        return True

    if winnerOfTheBoard == None:
        if sum([i.count(EMPTY) for i in board]) == 0 :
            return True
        
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X : return 1
        elif winner(board) == O : return -1
        else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    playerWithTurn = player(board)
    setOfActions = actions(board)

    if (playerWithTurn == X):
        return MaximumValue(board)[0]
    else :
        return MinimumValue(board)[0]
    

def MaximumValue(board) :
   
    
    if terminal(board) : return [(0,0),utility(board)]

    currentMaximumValue = float('-inf')
    setOfActions = actions(board)
    optimalAction = (0,0)
    for action in setOfActions:
        minValueAnticipated = MinimumValue(result(board,action))[1]
        if minValueAnticipated > currentMaximumValue : 
            optimalAction = action
            currentMaximumValue = minValueAnticipated
        if currentMaximumValue == 1 : break
    return [optimalAction,currentMaximumValue]


def MinimumValue(board):
   
    
    if terminal(board) : return [(0,0),utility(board)]
    setOfActions = actions(board)
    currentMinimumValue = float('inf')
    optimalAction = (0,0)
    for action in setOfActions:
        maxValueAnticipated = MaximumValue(result(board,action))[1]
        if maxValueAnticipated < currentMinimumValue : 
            optimalAction = action
            currentMinimumValue = maxValueAnticipated
        if currentMinimumValue == -1 : break
    return [optimalAction,currentMinimumValue]

