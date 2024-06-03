import turtle
import random

def generate_maze(size):
    maze = [[1 for x in range(size)] for y in range(size)]
    
    # Carve out a starting point
    start_x = random.randint(1, size-2)
    start_y = random.randint(1, size-2)
    maze[start_x][start_y] = 0
    
    stack = [(start_x, start_y)]
    
    while stack:
        x,y = stack.pop()
        
        directions = [(x-2,y), (x+2,y), (x,y-2), (x,y+2)]
        random.shuffle(directions)
        
        for new_x,new_y in directions:
            if new_x >= 1 and new_x < size-1 and new_y >= 1 and new_y < size-1:
                if maze[new_x][new_y] == 1:
                    maze[(new_x+x)//2][(new_y+y)//2] = 0
                    maze[new_x][new_y] = 0
                    stack.append((new_x,new_y))
    
    return maze

def draw_maze(maze):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,-200)
    turtle.pendown()
    
    cell_size = 400/len(maze)
    
    for row in maze:
        for cell in row:
            if cell == 1:
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(cell_size)
                    turtle.left(90)
                turtle.end_fill()
            turtle.forward(cell_size)
        turtle.backward(cell_size*len(row))
        turtle.left(90)
        turtle.forward(cell_size)
        turtle.right(90)

    # Find an open space for destination
    destination_x = len(maze) - 2
    destination_y = len(maze) - 2
    while maze[destination_x][destination_y] == 1:
        destination_x -= 1
        if destination_x < 1:
            destination_x = len(maze) - 2
            destination_y -= 1

    # Draw green circle at destination
    screen_x = -200 + (destination_y+0.5)*cell_size
    screen_y = -200 + (destination_x+0.5)*cell_size
    radius = cell_size/2

    # Move to starting position of circle arc
    turtle.penup()
def move(maze, position, direction):
    x, y = position
    if direction == 'Up':
        x += 1
    elif direction == 'Down':
        x -= 1
    elif direction == 'Left':
        y -= 1
    elif direction == 'Right':
        y += 1
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
        return position
    return (x,y)

def play_game():
    size = int(input('Enter the size of the maze: '))
    
    maze = generate_maze(size)

    draw_maze(maze)

    cell_size = 400/size

    turtle.shape('circle')
    turtle.color('red')
    turtle.penup()
    turtle.goto(-200+cell_size/2,-200+cell_size/2)

    position = (1,1)

    def on_key_press(event):
        nonlocal position
        
        direction = event.keysym
        
        new_position = move(maze, position, direction)
        if new_position != position:
            position = new_position
            
            x,y = position
            
            turtle.goto(-200+cell_size/2+y*cell_size,-200+cell_size/2+x*cell_size)

        if position == (size-2,size-2):
            print('You win!')
            turtle.bye()

    canvas = turtle.getcanvas()
    canvas.bind('<KeyPress>', on_key_press)
    canvas.focus_set()

    turtle.listen()
    turtle.mainloop()

play_game()