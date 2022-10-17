# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 12, 2022
# This program asks the user for 2 angles in a triangle
# it then tells the user if the triangle is equilateral, isosceles, or scalene
# it also tells the user if it is not possible
# for the 2 angles to make up a triangle
# it also checks input errors like words and negative numbers



# gets all required input from the user
def user_input():

    # access the global variables from within this function
    global angle1
    global angle2
    global finished

    # gets user input for two of the angles of a triangle
    print("Please input two angles of a triangle,")
    angle1 = input("Angle1: ")
    angle2 = input("Angle2: ")

    # adds extra line
    print("")


# calculates the third angle and checks for input errors
def third_angle():

    # ensures the program is not supposed to be closed, stops a specific error
    if finished == False:

        # access the global variable from within this function
        global angle3

        # try function is used to catch any improper inputs
        try:

            # checks that the to angles are valid and make a triangle
            if (float(angle1) > 0) & (float(angle2) > 0):

                # calculates the third angle of the triangle
                angle3 = 180 - float(angle1) - float(angle2)

            # called if the input was negative or zero
            else:
                # ensures the program is not supposed to be closed, stops a specific error
                if finished == False:
                    print(
                        "You can not have a negative or zero angle, please try again."
                    )
                    restart_from_error()

        except:
            # ensures the program is not supposed to be closed, stops a specific error
            if finished == False:
                print("There was an error in your inputs, please try again.")
                restart_from_error()


# casts the angle variables into floats (happens after error checking)
def make_angles_floats():

    # access the global variables from within this function
    global angle1
    global angle2
    global angle3

    # casts all of the variables into floats
    angle1 = float(angle1)
    angle2 = float(angle2)
    angle3 = float(angle3)


# check the angles to see what triangle they form
def check_triangle():

    # ensures the program is not supposed to be closed, stops a specific error
    if finished == False:

        # if the angles dont make up a triangle
        if angle3 <= 0:
            print("Your angels will not make a triangle, please try again.")
            restart_from_error()

        # check the type of the triangle
        elif (angle3 == angle2) | (angle2 == angle1) | (angle1 == angle3):
            if angle3 == angle2 == angle1:
                print("Your triangle is equilateral")

            else:
                print("Your triangle is isosceles")

        elif (angle3 != angle2) & (angle2 != angle1) & (angle1 != angle3):
            print("Your triangle is scalene")

        # if none of the triangles are selected (this error should never be called)
        else:
            print("An error occurred, please try again.")
            restart_from_error()

        # add extra line
        print("")


# asks the user if they want to restart after the program is finished
def user_restart():

    # access the global variable from within this function
    global finished

    # ensures the program is not supposed to be closed, stops a specific error
    if finished == False:

        # ask the user if they want to restart
        restart = input("Would you like to try again? (y/n)\n")

        # if the response is y restart the program
        if restart == "y":
            main()

        # if the response is n exit the program
        elif restart == "n":
            finished = True
            exit()

        # if the response isn't y or n restart this function
        else:
            print("Please enter y or n")
            print("")
            user_restart()


# this function restarts the program, it is called any time there is an error
def restart_from_error():
    input("Press enter to continue")
    print("")
    main()


# runs the program by calling the functions in the correct order
def main():

    # access the global variable from within this function
    global finished

    # sets finished to false at the start of the program
    finished = False

    user_input()
    third_angle()
    make_angles_floats()
    check_triangle()
    user_restart()


if __name__ == "__main__":
    main()
