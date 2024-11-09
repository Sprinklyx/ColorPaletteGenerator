import random


#place to store colors generated
num_colors = int(input("How many colors would you like?: "))
colors = [num_colors]

def color_choice():
    focal_point = str(input("Do you have a main color?: "))

    if focal_point == ('y'):
        color = str(input("Input the hex color of your choosing \'(#000000)\': "))
        #make a loop where the user has to input a color until it is valid
        for char in color.split():
            #looking for the color to start with a '#' sign
            if not char.startswith('#'):
                print("Invalid hex color. Please start you color choice with \'#\' symbol.")
            #looking for characters to stay within alphanumerical ranges
            elif char != range(0, 10) or range(ascii(65), ascii(71)):
                print("Invalid hex color. Hex colors use numbers 1-9 and letters A-F.")
                
    
        
                


#reminder of color ranges
'''
red_to_green = 'FF0000, 00FF00'
green_to_blue = '00FF00, 0000FF'
blue_to_red = '0000FF, FF0000'
'''



color_choice()