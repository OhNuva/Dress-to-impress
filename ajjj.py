import pygame
import sys
import random

pygame.init()

pygame.mixer.init()

# Load background music
pygame.mixer.music.load("Music/game_sound.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


'''
The following will provide the standard aspects of the game, particularly the screen configuration. 
>>> screen_width : int
The width of the application window in pixels.
>>> screen_height : int
The height of the application window in pixels.
>>> screen : pygame. Surface
The main display surface returned by the function. #all drawing operations are rendered onto this surface.
'''

#screen size
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Professor Dress-Up Game")

'''
The following will  provide the colour constraints and backgrounds that will be used throughout the course of the game.
>>> WHITE : tuple[int, int, int]
Standard white color (255, 255, 255).
>>> BLACK : tuple[int, int, int]
Standard black color (0, 0, 0).
>>> GRAY : tuple[int, int, int]
Gray used for default button color (150, 150, 150).
>>> LIGHT_GRAY : tuple[int, int, int]
Light gray used for button hover effects (200, 200, 200).
>>> RED : tuple[int, int, int]
Standard red color (255, 0, 0).
>>> background_one : pygame. Surface
>>> background_two : pygame. Surface
>>> background_three : pygame. Surface
>>> background_four : pygame. Surface
>>> background_ranking : pygame. Surface
Background images that will be used for various screens in the game.
#Each image is loaded from the Images/ directory and scaled to match the screen dimensions (`screen_width` × `screen_height`).
'''

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)

#png background file
background_one = pygame.image.load("Images/background_one.png")
background_one = pygame.transform.scale(background_one, (screen_width, screen_height))
background_two = pygame.image.load("Images/background_two.png")
background_two = pygame.transform.scale(background_two, (screen_width, screen_height))
background_three = pygame.image.load("Images/background_three.png")
background_three = pygame.transform.scale(background_three, (screen_width, screen_height))
background_four = pygame.image.load("Images/background_four.png")
background_four = pygame.transform.scale(background_four, (screen_width, screen_height))
background_ranking = pygame.image.load("Images/background_ranking.png")
background_ranking = pygame.transform.scale(background_ranking, (screen_width, screen_height))

'''
The following will define the variables needed in order for the game to perform properly.
>>> ranking_score : int or None
Stores the users ranking score. #Initialized to None until a score is calculated.
>>> current_page : str
A string representing the current screen (e.g., "start", "menu", "results"). Defaults to "start".
>>> selected_prof : object or None
Holds the selected character. None means no profile has been chosen.
>>> prof_list : list
A list containing all professor names available to be selected in the game.
>>> prof_names : list
A list of professor names (strings).
'''

#define all the varibales here: 
ranking_score= None
current_page = "start"
selected_prof = None
prof_list = []
prof_names = []

'''
The following function will create a rectangular button for the user to select. It will store the text
in an Arial font and optionally stores an image that will be displayed above the text.
>>> x : int
The x-coordinate of the top-left corner of the button. #The same is to be said of the y, w, and h
>>> text : str
The text displayed on the button.
>>> font : pygame
The font used to render button text.
>>> image : pygame. Surface, optional
Optional image #image will be scaled proportionally to fit inside the button without distortion
>>> rect : pygame
Rectangular area #of the button used for drawing and collision.
>>> draw(surface):
Draws the button onto the given surface, applying hover colour(s), scaling the image to fit, and placing text near the bottom.
>>>is_clicked(event):
Returns True if the user pressed the mouse button while the cursor was inside the button.
'''

#define all classes here
#button class type  
class Button:
    def __init__(self, x, y, w, h, text, image=None):

        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 22)
        self.image = image  

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        color = LIGHT_GRAY if self.rect.collidepoint(mouse) else GRAY
        pygame.draw.rect(surface, color, self.rect)

        #scaling images to the buttons
        if self.image:
            img = self.image
            iw, ih = img.get_size()
            bw, bh = self.rect.w - 8, self.rect.h - 28
            scale = min(bw / iw, bh / ih)
            new_size = (max(1, int(iw*scale)), max(1, int(ih*scale)))
            img2 = pygame.transform.scale(img, new_size)
            img_rect = img2.get_rect(center=(self.rect.centerx, self.rect.centery - 8))
            surface.blit(img2, img_rect)

        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=(self.rect.centerx, self.rect.bottom - 14))
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

'''
The following will produce buttons that will be used throughout the game.
>>> ranking_button : Button
Used to illustrate the score of the outfit #(300, 400) with 200×50 pixels.
>>> start_button : Button
Navigates to the next screen, beginning the game, #positioned at (250, 250).
>>> exit_button : Button
Closes the game when clicked, #postitioned at (470, 250) with 200×50 pixels.
>>> male_button : Button
Allows users to select a male character, #positioned at (200, 250) with 180×50 pixels.
>>> female_button : Button
Allows users to select a female character, #positioned at (420, 250) with 180×50 pixels.
'''

#ranking button
ranking_button = Button(300, 500, 200, 50, "Submit")

#button graphics
start_button = Button(250, 350, 200, 50, "Start")
exit_button  = Button(470, 350, 200, 50, "Exit")
start_button = Button(300, 500, 200, 50, "Start")
exit_button  = Button(520, 500, 200, 50, "Exit")

#male/female buttons
male_button   = Button(320, 450, 180, 50, "Male")
female_button = Button(540, 450, 180, 50, "Female")
'''
The following are strings that introduce and represent various game pages that will be used throughout the game.
>>> start_page : str
The initial "start" screen.
>>> gender_page : str
The page where the user selects a gender option (Male/Female).
>>> prof_page : str
The professor selection page, where the user chooses from available professor avatars.
>>> mannequin_page : str
The page containing the outfit customization interface.
>>> ranking_page : str
The page that displays ranking results.
'''

#defining the pages
start_page = "start"
gender_page = "gender"
prof_page = "prof_selection"
mannequin_page = "mannequin"
ranking_page = "ranking"

'''
The following displays the professor avatars that may be chosen and the associated name of the professor.
Each professor image is loaded from the Images/ directory and scaled to
100×100 pixels for menu display.
>>> pendar : pygame. Surface #female professor example
Uploads a cartoon image of Professor Pendar Mahmoudi.
>>> michael : pygame. Surface #male professor example
Uploads a cartoon image of Professor Michael Tam.
>>> female_profs : list[pygame.Surface]
List of female professor images.
>>> female_names : list[str]
List of names associated with each image.
>>> male_profs : list[pygame.Surface]
List of male professor images.
>>> male_names : list[str]
List of corresponding names for each image.
'''
#professor_png
#female professors
pendar = pygame.image.load("Images/pendar_cartoon_trans.png")
pendar = pygame.transform.scale(pendar, (100, 100))
comfort = pygame.image.load("Images/comfort_cartoon_trans.png")
comfort = pygame.transform.scale(comfort, (100, 100))
mary = pygame.image.load("Images/dean_mary_cartoon_trans.png")
mary = pygame.transform.scale(mary, (100, 100))

#male professors
michael = pygame.image.load("Images/tam_cartoon_trans.png")
michael = pygame.transform.scale(michael, (100, 100))
jordan = pygame.image.load("Images/jhammy_cartoon_trans.png")
jordan = pygame.transform.scale(jordan, (100, 100))
boxin = pygame.image.load("Images/boxin_cartoon_trans.png")
boxin = pygame.transform.scale(boxin, (100, 100))

#lists of all profs
female_profs = [pendar, comfort, mary]
female_names = ["Pendar Mahmoudi", "Comfort Mintah", "Mary Wells"]
male_profs = [michael, jordan, boxin]
male_names = ["Michael Tam", "Jordan Hamilton", "Boxin Zhao"]
'''
The following will provide a list of clothing graphics that will be used for character customization during the game.
All uplaods are loaded from the Images/ or images/ directory and scaled to consistent sizes for display.
>>> shirt1–shirt7 : pygame. Surface
A list of shirt graphics (seven), #scaled to 140x140 pixels.
>>> pants1–pants5 : pygame. Surface
A list of pant graphics (five), #scaled to 160×140 pixels.
>>> shoe1–shoe3 : pygame. Surface
A list of shoe graphics (three), #scaled to 140×60 pixels.
>>> hat1–hat3 : pygame. Surface
A list of hat/accessory graphics (three), #scaled to 90×70 pixels.
>>> shirt_list : list[pygame.Surface]
Contains all available shirt options.
>>> pants_list : list[pygame.Surface]
Contains all available pants options.
>>> shoes_list : list[pygame.Surface]
Contains all available shoe options.
>>> hats_list : list[pygame.Surface]
Contains all available hat options.
'''
#shirts_png
shirt1 = pygame.image.load("Images/shirt1.png")
shirt1 = pygame.transform.scale(shirt1, (385, 300))
shirt2 = pygame.image.load("Images/shirt2.png")
shirt2 = pygame.transform.scale(shirt2, (450, 300))
shirt3 = pygame.image.load("Images/shirt3.png")
shirt3 = pygame.transform.scale(shirt3, (450, 300))
shirt4 = pygame.image.load("Images/shirt4.png")
shirt4 = pygame.transform.scale(shirt4, (375, 300))
shirt5 = pygame.image.load("Images/shirt5.png")
shirt5 = pygame.transform.scale(shirt5, (375, 300))
shirt6 = pygame.image.load("Images/shirt6.png")
shirt6 = pygame.transform.scale(shirt6, (375, 300))
shirt7 = pygame.image.load("Images/shirt7.png")
shirt7 = pygame.transform.scale(shirt7, (375, 300))

#pants_png
pants1 = pygame.image.load("Images/pants1.png")
pants1 = pygame.transform.scale(pants1, (150, 150))
pants2 = pygame.image.load("Images/pants2.png")
pants2 = pygame.transform.scale(pants2, (150, 150))
pants3 = pygame.image.load("Images/pants3.png")
pants3 = pygame.transform.scale(pants3, (150, 150))
pants4 = pygame.image.load("Images/pants4.png")
pants4 = pygame.transform.scale(pants4, (150, 150))
pants5 = pygame.image.load("Images/pants5.png")
pants5 = pygame.transform.scale(pants5, (150, 150))

#shoes_png
shoe1 = pygame.image.load("Images/shoe1.png")
shoe1 = pygame.transform.scale(shoe1, (150, 70))
shoe2 = pygame.image.load("Images/shoe2.png")
shoe2 = pygame.transform.scale(shoe2, (150, 70))
shoe3 = pygame.image.load("Images/shoe3.png")
shoe3 = pygame.transform.scale(shoe3, (150, 70))

#hats_png
hat1 = pygame.image.load("Images/hat1.png")
hat1 = pygame.transform.scale(hat1, (120, 80))
hat2 = pygame.image.load("Images/hat2.png")
hat2 = pygame.transform.scale(hat2, (120, 80))
hat3 = pygame.image.load("Images/hat3.png")
hat3 = pygame.transform.scale(hat3, (120,80))

#lists of clothes
shirt_list = [shirt1, shirt2, shirt3, shirt4, shirt5, shirt6, shirt7]
pants_list = [pants1]
shoes_list = [shoe1, shoe2, shoe3]
hats_list = [hat1, hat2, hat3]

'''
The following loads and scales clothing pieces, putting them in their respective lists using filename patterns.
#This allows the program to expand available clothing options without manually loading each image.
>>> shirt_list : list[pygame.Surface]
This loop loads the aforementioned shirt files, scales them, and appends them to the list.
>>> pants_list : list[pygame.Surface]
This loop loads the aforementioned pants files, scales them, and appends them to the list.
>>> shoes_list : list[pygame.Surface]
This loop loads the aforementioned shoe files, scales them, and appends them to the list.
>>> hat_list : list[pygame.Surface]
This loop loads the aforementioned hat files, scales them, and appends them to the list.
'''
#clothing lists
shirt_list = [shirt1, shirt2, shirt3, shirt4, shirt5, shirt6, shirt7]
pants_list = [pants1, pants2, pants3, pants4, pants5]
shoes_list = [shoe1, shoe2, shoe3]
hat_list = [hat1, hat2, hat3]
'''
The following will store the selected clothing items. This storage helps determine which shirt, pants, shoes, and hat are displayed
during the customization process.
>>> current_shirt : pygame. Surface or None
Displays the shirt currently selected for the mannequin. None means no shirt has been selected.
>>> current_pants : pygame. Surface or None
Displays the pants currently selected for the mannequin. None means no pants have been selected.
>>> current_shoes : pygame. Surface or None
Displays the shoes currently selected for the mannequin. None means no shoes have been selected.
>>> current_hat : pygame. Surface or None
Displays the hat currently selected for the mannequin. None means no hat has been selected.
'''

#status of clothing 
current_shirt = None
current_pants = None
current_shoes = None
current_hat = None

'''
The following will control the animation of the sliding closet menu used in the customization screen. The menu slides down from
the top of the window when opened, and retracts when closed.
>>> closet_open : bool
Indicates whether the closet menu is open (True) or closed (False).
>>> menu_height : int
The height of the closet menu in pixels.
>>> menu_y : int
The vertical position of the menu. #initialized to menu_height so it starts offscreen above the top edge.
>>> menu_speed : int
The number of pixels the menu moves per frame during sliding animations. #Higher values make the menu open/close faster.
'''

#closet slide-down menu
closet_open = False
menu_height = 320
menu_y = -menu_height  
menu_speed = 18  #pixels
menu_width = 350
menu_x = screen_width

'''
The following indicates the buttons that will be used for interacting with the sliding closet menu and the lists that will
store item buttons for each clothing type.
>>> closet_button : type(button)
The main toggle button that opens or closes the closet menu, #positioned at (650, 20) with 120×40 pixels.
>>> shirts_cat_button : type(button)
Displays the shirt category inside the closet menu, #positioned at (40, 10) relative to the top of the closet.
>>> pants_cat_button : type(button)
Displays the pants category inside the closet menu, #positioned at (220, 10) relative to the top of the closet.
>>> shoes_cat_button : type(button)
Displays the shoe category inside the closet menu, #positioned at (400, 10) relative to the top of the closet.
>>> hats_cat_button : type(button)
Displays the hat category inside the closet menu, #positioned at (40, 10) relative to the top of the closet.
>>> shirt_buttons : list[Button]
Will hold buttons representing each available shirt option.
>>> pants_buttons : list[Button]
Will hold buttons representing each available pair of pants.
>>> shoes_buttons : list[Button]
Will hold buttons for all available shoe options.
>>> hat_buttons : list[Button]
Will hold buttons for all available hat options.
'''

# Create closet and category buttons (positions will be used with offset)
closet_button = Button(35, 35, 140, 50, "Closet")
# category buttons inside closet (y is relative to closet top)
shirts_cat_button = Button(20, 20, 140, 40, "Shirts")
pants_cat_button = Button(20, 70, 140, 40, "Pants")
shoes_cat_button = Button(20, 120, 140, 40, "Shoes")
hats_cat_button = Button(20, 170, 140, 40, "Hats")
close_closet_button = Button(20, 220, 140, 40, "Close")

#item buttons for each category
shirt_buttons = []
pants_buttons = []
shoes_buttons = []
hat_buttons = []

'''
The following block of code generates and positions clothing item buttons for shirts, pants, shoes, hats in a
two-column grid layout inside the closet interface.

Each button is given the same statring positions, denoted by item_x_start and item_y_start, and these buttons are then offset using item_x_gap and item_y_gap.

Loops are used to create a button for every item in the respective clothing list (shirts, pants, hats or shoes). 
The button column is determined by 'i % 2' for i in each respective list, so that if i is even the button will be sorted into the left column and if i is odd it will be
sorted into the right column.
The button row is then determined by '1//2', so that after every two items, the following button will move down to the next row, giving two buttons per row. 

The row and column of each button is then converted into on-screen coordinates using the given starting x and y positions and x and y offsets. 
The buttons are then created with their respective size (which varies depending on clothing type) and images, and these buttonsare appended to the corresponding 
category button list. 

Each clothing category has its own list (shirt_list, pants_list, etc.).
For each item in the list:


Example
>>>If shirt_list has 4 items, the shirts are placed as:

    (20, 280)      (180, 280)
    (20, 460)      (180, 460)

'''

#Positions of clothing items inside the closet
item_x_start = 20
item_y_start = 280
item_gap_x = 160
item_gap_y = 180
#shirts
for i in range(len(shirt_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 110, 110, f"S{i+1}", image=shirt_list[i])
    shirt_buttons.append(button)
#pants
for i in range(len(pants_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 150, 150, f"P{i+1}", image=pants_list[i])
    pants_buttons.append(button)
#shoes
for i in range(len(shoes_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 150, 70, f"Sh{i+1}", image=shoes_list[i])
    shoes_buttons.append(button)
#hats
for i in range(len(hat_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 120, 80, f"H{i+1}", image=hat_list[i])
    hat_buttons.append(button)

#when categories are not clicked
shirts_open = False
pants_open = False
shoes_open = False
hats_open = False

'''
The following functions are utility functions that temporarily visually shift a button and check to see if the space where the shifted button occupies is clicked.
This essentially mimics the effect of actually shifting and moving every button, allowing the buttons to still be clickable, but without the additional complications this would cause.

draw_button_with_offset(button, offset_y) draws the existing button with a horizontal offset of offset_y and then restores it to its original position. \
This will be used to visually shift buttons when the clost panel slides.

is_clicked_with_offset(button,event,offset_y) checks to see if the visually shifted button is clicked on and uses the same offset_y as in draw_button_with_offset so the
clickable area matches what the player sees. 

>>>Closet panel is slid 200 pixels to the right
for b in shirt_buttons:
    draw_button_with_offset(b, offset_x=200)

>>>Detect clicks in the shifted closet
if is_clicked_with_offset(shirt_buttons[0], event, offset_x=200):
    print("Shirt 1 selected!")
'''

#Vertical offset buttons for the closet
#AD: I would group these next two together in a doc string
def draw_button_with_offset(button, offset_y):
    old_x = button.rect.x
    button.rect.x += offset_y
    button.draw(screen)
    button.rect.x = old_x

#checking is the click is offset
def is_clicked_with_offset(button, event, offset_y):
    old_x = button.rect.x
    button.rect.x += offset_y
    clicked = button.is_clicked(event)
    button.rect.x = old_x
    return clicked
'''
The following block of code is the main game loop for the game, which is repsonsible for the current page/ state of the game
all event handling, and drawing all user interface elements/ images/ clothing overlays.

>>>Game States
The game uses 'current_page' to switch between screens by setting the variable equal to different things.

If current_page= start_page, the game displays the backgroun image and start/exit buttons. If the start button
is clicked, the game continues to the next page: 'gender_page' and if the exit button is clicked the game exits.

If current_page=gender_page, the game displays buttons for either female or male character selection.
The game will then be directed to the prof_page, which will display a set of professor buttons based on the gender that was selected.
Clicking one of these buttons sets 'selected_prof' and moves on to the mannequin_page. 

If current_page=mannequin_page then the game will display the mannequin with the selected professor's head.
This page also includes the sliding closet panel containing all clothing types: shirts, pants, shoes, hats.
On this page players can open and close the closet and choose clothing items which are drawn onto the mannequin
using current_shirt, current_pants, current_shoes, current_hat. 

If current_page=ranking+page, the game will display a random score from 1-10 when the ranking button is pressed.
This page uses the 'random.randint()' function and is enabled because 'random' was imported at the beginning of the code.

>>>Event Handling
All pygame events are processed inside a single event loop. 
The events for each page are as follows: 
    start_page: start and exit buttons
    gender_page: male and female selection 
    prof_page: professor button selection 
    mannequin_page: open/close the closet, category selection (shirts, pants, shoes, hats),
    selecting individual clothing items, and uses 'is_clicked_with_offset()'to handle clicks on a sliding menu. 
    
>>>Sliding Closet Menu
When the sliding closet panel opens, category buttons and clothing buttons are drawn using the 'draw_button_with offset()' function
which temporarily shifts the buttons so they appear in the sliding panel. 

>>>Drawing and Rendering
Each frame depending on the current page, checks and draws the background image, buttons for that page,
mannequin and professor head images, the currently selected clothing items, the sliding closet panel and category/ item buttns, and in the case that its 
applicable, the ranking score. 

The screen is refrshed every frame using 'pygame.display.update' and the game runs at 60 FPS 
using 'clock.ticl(60)'.

The loop ends when the user closes the window and pygame is shit down.
'''

# main loop
#AD: This one should get its own. It should be detailed, but don't stress. It doesn't have to be excessive. The only thing I wouldn't include is the clock countdown, the quit part at the end, and name=main :)

def main():
    global current_page, ranking_score, selected_prof, prof_list, prof_names
    global closet_open, menu_y, menu_x, menu_width, shirts_open, pants_open, shoes_open, hats_open
    global current_shirt, current_pants, current_shoes, current_hat

    running = True
    clock = pygame.time.Clock()
    
    #Timer Variables
    
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            #start_up_page
            if current_page == start_page:

                #button clicker
                if start_button.is_clicked(event):
                    current_page = gender_page  

                if exit_button.is_clicked(event):
                    pygame.quit()
                    sys.exit()

            #gender_page
            elif current_page == gender_page:

                if male_button.is_clicked(event):
                    current_page = prof_page
                    prof_list = male_profs
                    prof_names = male_names

                if female_button.is_clicked(event):
                    current_page = prof_page
                    prof_list = female_profs
                    prof_names = female_names

            #professor selection page
            elif current_page == prof_page:
                #buttons for professors page #3
                prof_buttons = []
                x_start = 160
                y_start = 420
                for i in range(len(prof_names)):
                    button = Button(x_start + i*260, y_start, 220, 80, prof_names[i])
                    prof_buttons.append(button)

                #check if a prof is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(prof_buttons)):
                        if prof_buttons[i].is_clicked(event):
                            selected_prof = prof_list[i]
                            current_page = mannequin_page

            #ranking page
            elif current_page == ranking_page:

                if ranking_button.is_clicked(event):
                    ranking_score = random.randint(1, 10)

            #mannequin page events
            if current_page == mannequin_page:
                #closet button (open/close)
                if closet_button.is_clicked(event):
                    closet_open = not closet_open
                    if not closet_open:
                        shirts_open = pants_open = shoes_open = hats_open = False

                #check if the closet menu is open
                if closet_open and event.type == pygame.MOUSEBUTTONDOWN:
                    #compute current offset (menu_x)
                    offset = menu_x

                    #clothing catogery buttons 
                    if is_clicked_with_offset(shirts_cat_button, event, offset):
                        shirts_open = not shirts_open
                        pants_open = shoes_open = hats_open = False

                    if is_clicked_with_offset(pants_cat_button, event, offset):
                        pants_open = not pants_open
                        shirts_open = shoes_open = hats_open = False

                    if is_clicked_with_offset(shoes_cat_button, event, offset):
                        shoes_open = not shoes_open
                        shirts_open = pants_open = hats_open = False

                    if is_clicked_with_offset(hats_cat_button, event, offset):
                        hats_open = not hats_open
                        shirts_open = pants_open = shoes_open = False

                    if is_clicked_with_offset(close_closet_button, event, offset):
                        closet_open = False
                        shirts_open = pants_open = shoes_open = hats_open = False

                    #if a category is open,check the buttons of each catogery 
                    if shirts_open:
                        for i, button in enumerate(shirt_buttons):
                            if is_clicked_with_offset(button, event, offset):
                                current_shirt = shirt_list[i]
                    if pants_open:
                        for i, button in enumerate(pants_buttons):
                            if is_clicked_with_offset(button, event, offset):
                                current_pants = pants_list[i]
                    if shoes_open:
                        for i, button in enumerate(shoes_buttons):
                            if is_clicked_with_offset(button, event, offset):
                                current_shoes = shoes_list[i]
                    if hats_open:
                        for i, button in enumerate(hat_buttons):
                            if is_clicked_with_offset(button, event, offset):
                                current_hat = hat_list[i]

        if closet_open:
            # slide in from the right
            if menu_x > screen_width - menu_width:
                menu_x -= menu_speed
                if menu_x < screen_width - menu_width:
                    menu_x = screen_width - menu_width
        else:
            # slide out to the right
            if menu_x < screen_width:
                menu_x += menu_speed
                if menu_x > screen_width:
                    menu_x = screen_width

        #images and drawing
        #background for page 1
        if current_page == start_page:
            if background_one:
                screen.blit(background_one, (0, 0))
            else:
                screen.fill(WHITE)

            start_button.draw(screen)
            exit_button.draw(screen)

        #gender selection page
        elif current_page == gender_page:
            if background_two:
                screen.blit(background_two, (0, 0))
            else:
                screen.fill((230, 230, 255))  
            title_font = pygame.font.SysFont("Arial", 48)
            title_text = title_font.render("Choose Your Character", True, BLACK)
            screen.blit(title_text, (325, 250))

            male_button.draw(screen)
            female_button.draw(screen)

        #professor selection page
        elif current_page == prof_page:
            if background_three:
                screen.blit(background_three, (0,0))
            else:
                screen.fill(WHITE)
            title_font = pygame.font.SysFont("Arial", 48)
            title_text = title_font.render("Choose Your Professor", True, BLACK)
            screen.blit(title_text, (325, 250))

            #professors as buttons
            prof_x = 160
            prof_y = 420
            for i in range(len(prof_names)):
                button = Button(prof_x + i*260, prof_y, 220, 80, prof_names[i])
                button.draw(screen)

        #mannequin page
        elif current_page == mannequin_page:
            if background_four:
                screen.blit(background_four, (0,0))
            else:
                screen.fill(WHITE)

            #closet button 
            closet_button.draw(screen)

            #prof head on the maniquine
            if selected_prof:
                screen.blit(selected_prof, (450, 40))

            #positions of clothing to manquine
            #shirt
            if current_shirt == shirt1:
                screen.blit(current_shirt, (315, 125))
            if current_shirt == shirt2:
                screen.blit(current_shirt, (283, 125))
            if current_shirt == shirt3:
                screen.blit(current_shirt, (282, 120))
            if current_shirt == shirt4:
                screen.blit(current_shirt, (300, 125))
            if current_shirt == shirt5:
                screen.blit(current_shirt, (300, 125))
            if current_shirt == shirt6:
                screen.blit(current_shirt, (300, 125))
            if current_shirt == shirt7:
                screen.blit(current_shirt, (300, 125))
            #pants
            if current_pants == pants1:
                screen.blit(current_pants, (412, 400))
            if current_pants == pants2:
                screen.blit(current_pants, (412, 400))
            if current_pants == pants3:
                screen.blit(current_pants, (412, 400))
            if current_pants == pants4:
                screen.blit(current_pants, (412, 400))
            if current_pants == pants5:
                screen.blit(current_pants, (412, 400))
            #shoes
            if current_shoes == shoe1:
                screen.blit(current_shoes, (422, 580))
            if current_shoes == shoe2:
                screen.blit(current_shoes, (422, 580))
            if current_shoes == shoe3:
                screen.blit(current_shoes, (422, 580))
            #hat
            if current_hat == hat1:
                screen.blit(current_hat, (452, 120))
            if current_hat == hat2:
                screen.blit(current_hat, (412, 400))
            if current_hat == hat3:
                screen.blit(current_hat, (412, 400)) 

            #sliding closet side panel
            if closet_open or menu_x < screen_width:
                #menu background on the right
                pygame.draw.rect(screen, (220, 220, 220), (menu_x, 0, menu_width, screen_height))

                draw_button_with_offset(shirts_cat_button, menu_x)
                draw_button_with_offset(pants_cat_button, menu_x)
                draw_button_with_offset(shoes_cat_button, menu_x)
                draw_button_with_offset(hats_cat_button, menu_x)
                draw_button_with_offset(close_closet_button, menu_x)

                if shirts_open:
                    for button in shirt_buttons:
                        draw_button_with_offset(button, menu_x)
                if pants_open:
                    for button in pants_buttons:
                        draw_button_with_offset(button, menu_x)
                if shoes_open:
                    for button in shoes_buttons:
                        draw_button_with_offset(button, menu_x)
                if hats_open:
                    for button in hat_buttons:
                        draw_button_with_offset(button, menu_x)

        #ranking page
        elif current_page == ranking_page:
            if background_ranking:
                screen.blit(background_ranking, (0, 0))
            else:
                screen.fill(WHITE)
            ranking_button.draw(screen)

            if ranking_score is not None:
                num_font = pygame.font.SysFont("Arial", 60)
                score_text = num_font.render(str(ranking_score), True, RED)
                screen.blit(score_text, (480, 350))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


#running the game
if __name__ == "__main__":
    main()
