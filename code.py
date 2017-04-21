# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck
    deck = [4,6,3,1,0,2,7,5]
    deck.extend([0,6,7,4,5,2,3,1])
    random.shuffle(deck)
    global exposed
    exposed = [[]] * 16
    exposed[0].append("false")
    global state
    state = 0
    global index_1
    index_1 = 0
    global index_2
    index_2 = 0
    global turns 
    turns =0
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global points
    global state
    global exposed
    global index_1
    global index_2
    global turns
    x = pos[0]
    y = pos[1]
    if x in range(801) and y in range(101):
        index = pos[0] // 50
        if exposed[index] == "true":
            exposed[index] == "true"
        else:
            exposed[index] = "true"
            if state == 0:
                state = 1
                turns = turns + 1
                index_1 = index
            elif state == 1:
                state = 2
                index_2 = index                      
            else:
                state = 1
                turns = turns + 1
                if deck[index_1] == deck[index_2]:
                    exposed[index_1] = "true"
                    exposed[index_2] = "true"
                else:
                    exposed[index_1] = "false"
                    exposed[index_2] = "false"  
                index_1 = index
           
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text(turns)
    
    y=-50
    z=0
    global deck
    global exposed
    for i in range(16):
        y = y + 50
        if exposed[i] == "true":
            #for x in deck:
            canvas.draw_text(str(deck[i]), [15+y, 60], 30, 'White')
            
        else:
            for z in range(51):
                if z== 0 or z== 50:
                    canvas.draw_line([z+y,0], [z+y,100], 1, "Red")
                else:    
                    canvas.draw_line([z+y,0], [z+y,100], 1, "Green")
                
     
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
  


# register event handlers

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label1 = frame.add_label("Moves:")
label = frame.add_label("Turns = ")


# get things rolling
new_game()
frame.start()

