# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:05:33 2022

@author: lejla
"""


#import packages

from numpy.random import random, randint, normal, shuffle
from psychopy.hardware import keyboard
from psychopy import visual, core, event, clock
import numpy as np
import contextlib
import sys
import subprocess
from psychopy import gui


# Create a window
win = visual.Window(screen=1, color=[0.709803921568627, -0.12156862745098, 0.67843137254902], colorSpace='rgb') #you may change the colour of you want!

# Create a stimulus for a certain window

message = visual.TextStim(win, text="Remember you choose the color of the letters, ignoring the word. If the color is red press left. If blue press right and if green press down")


# Draw the stimulus to the window.
message.draw()
 
# Flip backside of the window.
win.flip()
 
#Here we create the title of our Dialogue Box:
myDialogueBox = gui.Dlg(title = "Dialogue Box Exercise")

#Here we also create a title for our Dialogue Box, however we also specify a position on the screen for the box:
myDialogueBox = gui.Dlg(title = "My Box", pos = (400,350))

#Here we add some description text to our Dialogue Box (positioned right under the title):
myDialogueBox.addText('Please fill in the following fields:')

#Here we add fields to our Dialogue Box for the participant to fill in with certain information:
myDialogueBox.addField('Age:')


#Here we add a field to the Dialogue Box for the participant to fill in with certain information, however we also specify that the colour of the writing in the field should be blue:
myDialogueBox.addField('Participant ID:', color = "blue")

#Here we add a field to the Dialogue Box for the participant to fill in with certain information, however we specify that we want the participant to choose between two answers:
myDialogueBox.addField('Gender:', choices = ["F", "M", "O"])

#Here we command Python to show the Dialogue Box when we're done editing it:
myDialogueBox.show()

#Here we check whether the information filled into the Dialogue Box is okay. And if it is okay, we save the information the participant filled in, to a variable we call ID:
if myDialogueBox.OK:
    ID = myDialogueBox.data




i = 0
c = None
while c==None:   # loop until a key is pressed
    message = visual.TextStim(win, text=str(i)+   "   when you are ready press any key to start")
    message.draw()
    win.flip()
    c = event.waitKeys(maxWait=1.0)
    i = i + 1



# set parameters/ things you need for the experiment to work, words and reaction time and number of trials, words, colors, correct keys


score =[]

words = ['Red', 'Green', 'Blue', 'Green', 'Blue', 'Red'] 
colour_list = ['red', 'green', 'blue', 'green', 'blue', 'red']



answer_keys = {'left': 'red', 'right': 'blue', 'down': 'green'} 
answer_keys['right'] == 'blue'  # boolean
answer_keys['left'] == 'red'  # boolean
answer_keys['down'] == 'green' 



data = [] # declare our list data



for i in range(1,21):
    print(i)
    data_dictionary = {}
    reaction_time_clock = core.Clock()    
    np.random.shuffle(words)
    np.random.shuffle(colour_list)
    reaction_time_clock = core.Clock() 
    message.text = words[0]
    message.color = colour_list[1]
    message.draw()
    win.flip()
   
 
       
 
    keys, rt = event.waitKeys(keyList={'left': 'red', 'right': 'blue', 'down': 'green'}, timeStamped=reaction_time_clock)[0000000000]
    #keys, rt = event.waitKeys(keyList=answer_keys.keys(), timeStamped=True)[0000000]  # Only listen for allowed keys. [0] to get just first and only response
    score = answer_keys[keys] == colour_list[1] # Whether the "meaning" of the key is identical to the ink color of the word.
  



    
     
    if score:
        data_dictionary['Response'] = "correct"
        print('correct')
        message = visual.TextStim(win, text="correct, you did it!")
        message.text += '\nRT=%i ms' %(rt*1000) 
        print('\nRT=%i ms' %(rt*1000)) 
    else: 
        data_dictionary['Response'] = "incorrect"
        print('incorrect')
        message = visual.TextStim(win, text="Oh-no, Fail")
        message.text += '\nRT=%i ms' %(rt*1000)  # Add RT to text
        print('\nRT=%i ms' %(rt*1000))
    message.draw()
    win.flip()
    core.wait(0.5)
    

    data_dictionary['ID'] = ID
    data_dictionary['Reaction Time'] = rt
    data_dictionary['keys'] = keys
    data.append(data_dictionary)




i = 0
c = None
while c==None:   # loop until a key is pressed
    message = visual.TextStim(win, text=str(i)+   "    You are done!, press any key to exit")
    message.draw()
    win.flip()
    c = event.waitKeys(maxWait=1.0)
    i = i + 1

presentationTime = [3.5, 5.5, 7.5]



# Close the window
win.close()

import pandas as pd 




data = pd.DataFrame(data)
data.to_excel('dataa.xlsx', sheet_name='sheet1', index=False)


 
