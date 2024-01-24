# Amend your program by implementing a menu system.
# • The user should be prompted for which shape they want to find the area and boundary
# length of.
# • Once this choice has been read in, create an instance of the relevant shape and then
# output the area and boundary length of the shape.
# • Once this is done, prompt the user to see if they want to calculate the area and boundary
# of another shape.
# • At the end of the program output how many Shapes were created and how many
# individual Circles, Triangles, and Squares were created as well. See the screenshot on
# the following page as to how your code could look when run

from Shapes_tl import Shape, Square, Triangle, Circle


def main():
    print("Enter 1 for Square, 2 for Triangle, 3 for Circle: ")

    go_again = 'y'

    while go_again == 'y':
        user_choice = input("Enter choice: ")
        user_dimension = float(input("Enter dimension: "))

        if user_choice == '1':
            print("You chose Square")
            user_square(user_dimension)

        elif user_choice == '2':
            print("You chose Triangle")
            user_triangle(user_dimension)

        elif user_choice == '3':
            print("You chose Circle")
            user_circle(user_dimension)

        else:
            print("Weird input")

        go_again = input("Do you want to go again? ('y' for yes): ")

    print(f"How many times instance of SHAPE class has been created: {Shape.getCount()}")
    print(f"How many times instance of Square class has been created: {Square.getCount()}")
    print(f"How many times instance of Triangle class has been created: {Triangle.getCount()}")
    print(f"How many times instance of circle class has been created: {Circle.getCount()}")


def user_square(dimension):
    # create instance
    sqr = Square()

    print(f"Area of square: {sqr.getArea(dimension)}")
    print(f"Boundary of square: {sqr.getBoundary(dimension)}")

    print(f"How many times instance of SHAPE class has been created: {Shape.getCount()}")
    print(f"How many times instance of SQUARE class has been created: {Square.getCount()}")


def user_triangle(dimension):
    # create instance
    triangle = Triangle()

    print(f"Area of Triangle: {triangle.getArea(dimension)}")
    print(f"Boundary of Triangle: {triangle.getBoundary(dimension)}")

    print(f"How many times instance of SHAPE class has been created: {Shape.getCount()}")
    print(f"How many times instance of triangle class has been created: {Triangle.getCount()}")


def user_circle(dimension):
    # create instance
    circle = Circle()

    print(f"Area of circle: {circle.getArea(dimension)}")
    print(f"Boundary of circle: {circle.getBoundary(dimension)}")


# Call main
main()

# Need to FIX - Count method for each shape not working
# - FIXED - Each subclass needed a __count class property.
