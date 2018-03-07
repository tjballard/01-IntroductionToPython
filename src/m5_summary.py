"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and TJ Ballard.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

orange_turtle = rg.SimpleTurtle('turtle')
orange_turtle.pen = rg.Pen('orange', 10)
orange_turtle.speed = 20

orange_turtle.pen_up()
orange_turtle.left(90)
orange_turtle.forward(300)
orange_turtle.left(90)
orange_turtle.forward(300)
orange_turtle.pen_down()
orange_turtle.left(90)
orange_turtle.forward(600)
orange_turtle.left(120)
orange_turtle.forward(200)
orange_turtle.right(20)
orange_turtle.forward(300)
orange_turtle.left(135)
orange_turtle.forward(500)
orange_turtle.right(125)
orange_turtle.forward(300)

window.close_on_mouse_click()