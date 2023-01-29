import clavier_souris as cs

# Function to check if the color of the pixel at x,y is yellow
def yellow(x,y):
    R,G,B=cs.pixelRGB(x,y)
    # Check if R is greater than or equal to 220, G is between 100 and 150 and B is less than or equal to 50
    if 220<=R and 100<=G<=150 and B<=50 :
        return(True)
    else :
        return(False)

# Function to check if the color of the pixel at x,y is gray
def gray(x,y):
    R,G,B=cs.pixelRGB(x,y)
    # Check if R, G, and B are between 100 and 150
    if 100<=R<=150 and 100<=G<=150 and 100<=B<=150 :
        return(True)
    else :
        return(False)
    
# Function to check if the color of the pixel at x,y is dark gray
def dark_gray(x,y):
    R,G,B=cs.pixelRGB(x,y)
    # Check if R, G, and B are between 100 and 170
    if 100<=R<=170 and 100<=G<=170 and 100<=B<=170 :
        return(True)
    else :
        return(False)
    
# Function to check if the color of the pixel at x,y is light green
def light_green(x,y):
    R,G,B=cs.pixelRGB(x,y)
    # Check if R is between 140 and 170, G is between 180 and 220, and B is between 120 and 140
    if 140<=R<=170 and 180<=G<=220 and 120<=B<=140 :
        return(True)
    else :
        return(False)

# Function to check if the color of the pixel at x,y is beige
def beige(x,y):
    # Check if the color of the pixel at x,y is (247, 224, 194)
    if cs.pixelRGB(x,y)==(247, 224, 194):
        return(True)
    else:
        return(False)