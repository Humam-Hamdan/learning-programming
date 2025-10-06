"""
Future Tasks:
    1. make lives system
    2.make score counter
    
"""
import random
import curses

# s = screen
s = curses.initscr()
# when == 0 curser = false = disappeared, or 1 or 2
curses.curs_set(0)
# height , width | getmax = getting the dimensions of the screen
sh, sw = s.getmaxyx()
# window in the screen
w = curses.newwin(sh, sw, 0, 0)
# == keyboard input = on
w.keypad(1)
# ms, refresh the screen every 100 mls
w.timeout(100)

# the start of the snake in the window
snk_x = sw//4
snk_y = sh//2
# list = have the body parts of the snake
snake = [
    # head
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# the start of the food
food = [sh//2, sw//2]
# the character of the food
w.addch(food[0], food[1], curses.ACS_PI)

# to store the key that's being pressed, starts with right
key = curses.KEY_RIGHT

# infinite loop, only closes when it's "False"
while True:
    # the input
    next_key = w.getch()
    # if there's no new input the take the same previous
    key = key if next_key == -1 else next_key

    # seeing if the snake hitted itself or the sides
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    # seeing the new loc of the head of the snake
    new_head = [snake[0][0], snake[0][1]]

    # moving the head of the screen
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # inserting the new head in the 1st index
    snake.insert(0, new_head)
    
    # checking if it ate the food
    if snake[0] == food:
        food == None
        # when food is none => randomize the place of the new food, not being on the outskirts so that you won't lose
        while food is None:
            nf = [
                random.radint(1, sh-1),
                random.radint(1, sw-1)
            ]   
            # if food isn't in the body of the snake then make it appear, if not? none
            food = nf if nf not in snake else None
        # add the new food
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # if teh snake didn't get the food, removing the tail of the snake so it won't be growing infinitely
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
    
    # showing the snake in the window
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)