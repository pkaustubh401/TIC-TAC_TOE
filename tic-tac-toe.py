#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def choiceOfMarker():
    marker=''
    
    while not (marker=='X' or marker=='O'):
        marker=input("Player1: choose between'X' or 'O'." ).upper()
    
    if marker=='X':
        return('X','O')
    else:
        return('O','X')


# In[2]:


def choiceOfPlay():
    if random.randint(0,1)==0:
        return 'player_1'
    else:
        return 'player_2'


# In[3]:


def displayBoard(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    


# In[4]:


def choiceOfPosition(board):
    position=0
    
    while (position not in range(1,10)) or (not spaceAvailable(board,position)):
        position=int(input("where do you want to put your marker(1-9)."))
        
    return position    


# In[5]:


def spaceAvailable(board,position):
    return board[position]==' '


# In[6]:


def placeMarker(board,position,marker):
    board[position]=marker


# In[7]:


def winCheck(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[8]:


def fullBoardCheck(board):
    for i in range(1,10):
        if spaceAvailable(board,i):
            return False
    
    return True


# In[9]:


def replay():
    result=input("Play one more game(Y/N)").upper()
    
    return result=='Y'


# In[ ]:


#main block to run

while True:                                       #terminates when replay is false
    
    
    #setup
    the_board=[' ']*10
    
    #choose player marker
    p1_marker,p2_marker= choiceOfMarker()
    
    #who plays first
    import random
    turn=choiceOfPlay()
    print(turn + 'will go first.')
    
    #game on conformation
    play_game=input("ready to start (Y/N)").upper()
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
        
    
    #gameplay
    
    while game_on:
        ##player one turn
        
        if turn=='player_1':
            ###display board
            displayBoard(the_board)
            
            ###choice of position to be marked
            choosed_position=choiceOfPosition(the_board)
            
            ###mark on given position
            placeMarker(the_board,choosed_position,p1_marker)
            
            ###win check
            if winCheck(the_board,p1_marker):
                displayBoard(the_board)
                print("Player1 wins thhe game")
                game_on= False
                
            else:
            ###tie check
                if fullBoardCheck(the_board):
                    displayBoard(the_board)
                    print("Its a TIE!")
                    game_on= False
                else:
                    turn='player_2'
        else:
         ##player two turn
            ###display board
            displayBoard(the_board)
            
            ###choice of position to be marked
            choosed_position=choiceOfPosition(the_board)
            
            ###mark on given position
            placeMarker(the_board,choosed_position,p2_marker)
            
            ###win check
            if winCheck(the_board,p2_marker):
                displayBoard(the_board)
                print("Player2 wins thhe game")
                game_on= False
                
            else:
            ###tie check
                if fullBoardCheck(the_board):
                    displayBoard(the_board)
                    print("Its a TIE!")
                    game_on= False
                else:
                    turn='player_1'
            
             
           
    if not replay():
        break
            
            
            
    


# In[ ]:




