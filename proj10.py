

import cards #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card):
    """
    Add your function header here.
    """

    if (dest_card==[' '] and src_card.rank()!=13):
        raise RuntimeError('Invalid move:The card that you are trying to place is not Ace.')

    elif src_card.suit()!=dest_card.suit():
        raise RuntimeError('Invalide move:The card that you are trying to place is not of same suit.')

    elif (src_card.suit()==dest_card.suit() and src_card.rank()!=dest_card.rank()+1):
        raise RuntimeError('Invalide move:The card that you are trying to place is not next in rank.')
            
    else:
        pass
        
      
def valid_tab_move(src_card, dest_card):
    """
    Add your function header here.
    """    
    pass  #Replace this pass statement with your own code
    
def valid_cell_move(src_card, dest_card):
    """
    Add your function header here.
    """    
    
                    
def tableau_to_cell(tab, cell):
    """
    Add your function header here.
    """    
    if cell==[' '] and tab!=[' ']:  # if cell  and tableau are not empty
        cell[0]=[tab[-1]]
        tab[-1]=' '
    else:
        if cell!=[' ']:
            raise RuntimeError('Invalid move: Cell is not empty')
        else: 
            raise RuntimeError('Invalid move: Tableau is empty')            
            
def tableau_to_foundation(tab, fnd):
    """
    Add your function header here.
    """    
    fnd[0]=tab[-1]
    tab[-1]=' '
            
def tableau_to_tableau(tab1, tab2):
    """
    Add your function header here.
    """    
    pass  #Replace this pass statement with your own code


def cell_to_foundation(cell, fnd):
    """
    Add your function header here.
    """    
    pass  #Replace this pass statement with your own code


def cell_to_tableau(cell, tab):
    """
    Add your function header here.
    """    
    pass  #Replace this pass statement with your own code
              
              
def is_winner(foundations):
    """
    Add your function header here.
    """    
    pass  #Replace this pass statement with your own code


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck()
    stock.shuffle()
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    for i in range(len(cells)):
        cells[i].append(' ')
        foundations[i].append(' ')

    for i in range(len(tableaus)):
            for j in range(7):                
                if stock.is_empty()==False:
                    if i>3 and j==6:
                        pass
                    else:
                        tableaus[i].append(stock.deal())
                else:
                    tableaus[i].append(' ')
        
    
    return (cells, foundations, tableaus)


def display_game(cells, foundations, tableaus):
    """
    Add your function header here.
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")

    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))
    for i in range(len(cells)):
        if cells[i]==[' ']:
            print(cells[i],end='')             #--------> change required.. printing [' '] while expected [ ]
        else:
            print("{}".format(str(cells[i])),end='')
    print(' ',end='')
    for i in range(len(cells)):
        print(foundations[i],end='')

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")    
    for i in range(7):
        print("    ",end='')        
        for j in range(len(tableaus)):
            if j>3 and i==6:
                pass
            else:
                column=tableaus[j]
                print("{:>5}".format(str(column[i])),end='')
        print()
          
    

def main():
    #HERE IS THE MAIN BODY OF OUR CODE
    print(RULES)
    cells, fnds, tabs = setup_game()
    display_game(cells, fnds, tabs)
    print(MENU)
    command = input("prompt :> ").strip().lower()
    while command != 'q':
        try:      
            if command.lower().startswith('tc'):
                cell=cells[int(command.split()[2])-1]
                tab=tabs[int(command.split()[1])-1]
                tableau_to_cell(tab,cell)
            elif command.lower().startswith('tf'):
                fnd=fnds[int(command.split()[2])-1][0]
                tab=tabs[int(command.split()[1])-1]
                valid_fnd_move(tab,fnd)
                tableau_to_foundation(tab, fnd)
            else:
                raise RuntimeError('Invalid command')
               
        #Any RuntimeError you raise lands here
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        
        display_game(cells, fnds, tabs)                
        command = input("prompt :> ").strip().lower()


if __name__=='__main__':
    main()
    
    
    

