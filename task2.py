import turtle
import math

def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return

    # Draw the initial square
    for _ in range(4):
        turtle.forward(branch_length)
        turtle.left(90)
    
    # Move to the top right corner of the square
    turtle.forward(branch_length)
    turtle.left(45)

    # Draw the right subtree
    new_length = branch_length / math.sqrt(2)
    turtle.forward(new_length)
    draw_pythagoras_tree(new_length, level - 1, angle)

    # Backtrack
    turtle.backward(new_length)
    turtle.right(90)

    # Draw the left subtree
    turtle.forward(new_length)
    draw_pythagoras_tree(new_length, level - 1, angle)

    # Backtrack
    turtle.backward(new_length)
    turtle.left(45)
    turtle.backward(branch_length)
    turtle.left(90)
    turtle.forward(branch_length)
    turtle.right(90)

def main():
    # Ask the user for the level of recursion
    level = int(input("Enter the level of recursion: "))

    # Set up the turtle
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(-50, -200)
    turtle.down()

    # Calculate the initial branch length based on the level
    initial_branch_length = 200 / (level + 1)

    # Start drawing the tree
    draw_pythagoras_tree(initial_branch_length, level, 45)

    # Finish
    turtle.done()

if __name__ == "__main__":
    main()
