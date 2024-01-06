# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

//thankyou



# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()





# from turtle import *
# color('black', 'blue')
# begin_fill()
# while True:
#     forward(200)
#     backward(350)
#     right(90)
#     left(280)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()








from turtle import * 
from random import randint 
bgcolor('black') 
x = 1 
speed(0) 
while True: 
  
 r = randint(0,255) 
 g = randint(0,255)  
 b = randint(0,255) 
  
 colormode(255)  
 pencolor(r,g,b) 
 fd(50 + x) 
 rt(90.991) 
 x = x+1 
exitonclick()
