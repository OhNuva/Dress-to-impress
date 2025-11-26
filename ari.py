
import pygame
import sys
import random

pygame.init()

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
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Start Up Page")

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
        self.font = pygame.font.SysFont("Arial", 26)
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
Navigates to the next screen, beginning the game #positioned at (250, 250).
>>> exit_button : Button
Closes the application when clicked. Positioned next to the Start button
at (470, 250) with a size of 200×50 pixels.

male_button : Button
    Allows users to select a male profile category or filter option.
    Positioned at (200, 250) with dimensions 180×50 pixels.

female_button : Button
    Allows users to select a female profile category or filter option.
    Positioned at (420, 250) with dimensions 180×50 pixels.

'''

#ranking button
ranking_button = Button(300, 400, 200, 50, "Submit")

#button graphics
start_button = Button(250, 250, 200, 50, "Start")
exit_button  = Button(470, 250, 200, 50, "Exit")

#male/female buttons
male_button   = Button(200, 250, 180, 50, "Male")
female_button = Button(420, 250, 180, 50, "Female")

#defining the pages
start_page = "start"
gender_page = "gender"
ranking_page = "ranking"
prof_page = "prof_selection"
mannequin_page = "mannequin"

#professor_png
#female professors
pendar = pygame.image.load("images/pendar_cartoon_trans.png")
pendar = pygame.transform.scale(pendar, (100, 100))
comfort = pygame.image.load("images/comfort_cartoon_trans.png")
comfort = pygame.transform.scale(comfort, (100, 100))
mary = pygame.image.load("images/dean_mary_cartoon_trans.png")
mary = pygame.transform.scale(mary, (100, 100))

#male professors
michael = pygame.image.load("images/tam_cartoon_trans.png")
michael = pygame.transform.scale(michael, (100, 100))
jordan = pygame.image.load("images/jhammy_cartoon_trans.png")
jordan = pygame.transform.scale(jordan, (100, 100))
boxin = pygame.image.load("images/boxin_cartoon_trans.png")
boxin = pygame.transform.scale(boxin, (100, 100))

#lists of all profs
female_profs = [pendar, comfort, mary]
female_names = ["Pendar Mahmoudi", "Comfort Mintah", "Mary Wells"]
male_profs = [michael, jordan, boxin]
male_names = ["Michael Tam", "Jordan Hamilton", "Boxin Zhao"]

#shirts_png
shirt1 = pygame.image.load("Images/shirt1.png")
shirt1 = pygame.transform.scale(shirt1, (140, 140))
shirt2 = pygame.image.load("Images/shirt2.png")
shirt2 = pygame.transform.scale(shirt2, (140, 140))
shirt3 = pygame.image.load("Images/shirt3.png")
shirt3 = pygame.transform.scale(shirt3, (140, 140))
shirt4 = pygame.image.load("Images/shirt4.png")
shirt4 = pygame.transform.scale(shirt4, (140, 140))
shirt5 = pygame.image.load("Images/shirt5.png")
shirt5 = pygame.transform.scale(shirt5, (140, 140))
shirt6 = pygame.image.load("Images/shirt6.png")
shirt6 = pygame.transform.scale(shirt6, (140, 140))
shirt7 = pygame.image.load("Images/shirt7.png")
shirt7 = pygame.transform.scale(shirt7, (140, 140))

#pants_png
pants1 = pygame.image.load("Images/pants1.png")
pants1 = pygame.transform.scale(pants1, (160, 140))
pants2 = pygame.image.load("images/pants2.png")
pants2 = pygame.transform.scale(pants2, (160, 140))
pants3 = pygame.image.load("images/pants3.png")
pants3 = pygame.transform.scale(pants3, (160, 140))
pants4 = pygame.image.load("images/pants4.png")
pants4 = pygame.transform.scale(pants4, (160, 140))
pants5 = pygame.image.load("images/pants5.png")
pants5 = pygame.transform.scale(pants5, (160, 140))

#shoes_png
shoe1 = pygame.image.load("Images/shoe1.png")
shoe1 = pygame.transform.scale(shoe1, (140, 60))
shoe2 = pygame.image.load("Images/shoe2.png")
shoe2 = pygame.transform.scale(shoe2, (140, 60))
shoe3 = pygame.image.load("Images/shoe3.png")
shoe3 = pygame.transform.scale(shoe3, (140, 60))

#hats_png
hat1 = pygame.image.load("Images/hat1.png")
hat1 = pygame.transform.scale(hat1, (90, 70))
hat2 = pygame.image.load("Images/hat2.png")
hat2 = pygame.transform.scale(hat2, (90, 70))
hat3 = pygame.image.load("Images/hat3.png")
hat3 = pygame.transform.scale(hat3, (90,70))

#lists of clothes
shirt_list = [shirt1, shirt2, shirt3, shirt4, shirt5, shirt6, shirt7]
pants_list = [pants1]
shoes_list = [shoe1, shoe2, shoe3]
hats_list = [hat1, hat2, hat3]

#shirts
shirt_list = [shirt1, shirt2, shirt3, shirt4, shirt5, shirt6, shirt7]
for i in range(1, 8):
    surf = pygame.image.load(f"shirt{i}.png")
    surf = pygame.transform.scale(surf, (140, 140))
    shirt_list.append(surf)

#pants
pants_list = [pants1]
for i in range(1, 6):
    surf = pygame.image.load(f"pants{i}.png")
    surf = pygame.transform.scale(surf, (160, 140))
    pants_list.append(surf)

#shoes
shoes_list = [shoe1, shoe2, shoe3]
for i in range(1, 4):
    surf = pygame.image.load(f"shoe{i}.png")
    surf = pygame.transform.scale(surf, (140, 60))
    shoes_list.append(surf)

#hats
hat_list = [hat1, hat2, hat3]
for i in range(1, 4):
    surf = pygame.image.load(f"hat{i}.png")
    surf = pygame.transform.scale(surf, (90, 70))
    hat_list.append(surf)

#status of clothing 
current_shirt = None
current_pants = None
current_shoes = None
current_hat = None

#closet slide-down menu
closet_open = False
menu_height = 320
menu_y = -menu_height  
menu_speed = 18  #pixels

# Create closet and category buttons (positions will be used with offset)
closet_button = Button(650, 20, 120, 40, "Closet")
# category buttons inside closet (y is relative to closet top)
shirts_cat_button = Button(40, 10, 160, 40, "Shirts")
pants_cat_button = Button(220, 10, 160, 40, "Pants")
shoes_cat_button = Button(400, 10, 160, 40, "Shoes")
hats_cat_button = Button(580, 10, 160, 40, "Hats")

#item buttons for each category
shirt_buttons = []
pants_buttons = []
shoes_buttons = []
hat_buttons = []

'''
The following block of code creates buttons for shirts, pants, shoes and hats and spaces them out on the wardrobe selection screen accordingly. 
The starting x-position is at 40 pixels, the starting y-position is at 60 pixels, and the gap between each item (button) is 170 pixels.

Each button is spaced apart horizontally by adding item_x_start to item_gap_x multiplied by the i.
Each row is then spaced apart vertically by adding a fixed amount to the item_y_start value. 

The arguments for buttons follow this structure: (item_x_start + i*item_gap_x, item_y_start) 

>>>



'''
#Positions of clothing items inside the closet
item_x_start = 40
item_y_start = 60
item_gap_x = 170
#shirts
for i in range(8):
    button = Button(item_x_start + i*item_gap_x, item_y_start, 140, 140, f"S{i+1}", image=shirt_list[i])
    shirt_buttons.append(button)
#pants
for i in range(6):
    button = Button(item_x_start + i*item_gap_x, item_y_start + 150, 160, 140, f"P{i+1}", image=pants_list[i])
    pants_buttons.append(button)
#shoes
for i in range(4):
    button = Button(item_x_start + i*item_gap_x, item_y_start + 300, 140, 60, f"Sh{i+1}", image=shoes_list[i])
    shoes_buttons.append(button)
#hats
for i in range(4):
    button = Button(item_x_start + i*item_gap_x, item_y_start + 380, 90, 70, f"H{i+1}", image=hat_list[i])
    hat_buttons.append(button)

#when categories are not clicked
shirts_open = False
pants_open = False
shoes_open = False
hats_open = False

#Vertical offset buttons for the closet
def draw_button_with_offset(button, offset_y):
    old_y = button.rect.y
    button.rect.y += offset_y
    button.draw(screen)
    button.rect.y = old_y

#checking is the click is offset
def is_clicked_with_offset(button, event, offset_y):
    old_y = button.rect.y
    button.rect.y += offset_y
    clicked = button.is_clicked(event)
    button.rect.y = old_y
    return clicked
'''

'''

# main loop
def main():
    global current_page, ranking_score, selected_prof, prof_list, prof_names
    global closet_open, menu_y, shirts_open, pants_open, shoes_open, hats_open
    global current_shirt, current_pants, current_shoes, current_hat

    running = True
    clock = pygame.time.Clock()

    while running:
        # event loop - single loop only (no nested event.get)
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
                x_start = 150
                y_start = 300
                for i in range(len(prof_names)):
                    button = Button(x_start + i*200, y_start, 120, 120, prof_names[i])
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
                #closet button (open drop_down)
                if closet_button.is_clicked(event):
                    closet_open = not closet_open
                    #closet button (close drop_down) 
                    if not closet_open:
                        shirts_open = pants_open = shoes_open = hats_open = False

                #check is the closet menu is open
                if closet_open and event.type == pygame.MOUSEBUTTONDOWN:
                    #compute current offset (menu_y)
                    offset = menu_y
                    #clothing catogery buttons 
                    if is_clicked_with_offset(shirts_cat_button, event, offset):
                        shirts_open = not shirts_open
                    if is_clicked_with_offset(pants_cat_button, event, offset):
                        pants_open = not pants_open
                    if is_clicked_with_offset(shoes_cat_button, event, offset):
                        shoes_open = not shoes_open
                    if is_clicked_with_offset(hats_cat_button, event, offset):
                        hats_open = not hats_open

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
            # slide down (menu_y increases toward 0)
            if menu_y < 0:
                menu_y += menu_speed
                if menu_y > 0:
                    menu_y = 0
        else:
            # slide up (menu_y moves back to its original height) 
            if menu_y > -menu_height:
                menu_y -= menu_speed
                if menu_y < -menu_height:
                    menu_y = -menu_height

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
            title_font = pygame.font.SysFont("Arial", 40)
            title_text = title_font.render("Choose Your Character", True, BLACK)
            screen.blit(title_text, (220, 150))

            male_button.draw(screen)
            female_button.draw(screen)

        #professor selection page
        elif current_page == prof_page:
            if background_three:
                screen.blit(background_three, (0,0))
            else:
                screen.fill(WHITE)
            title_font = pygame.font.SysFont("Arial", 40)
            title_text = title_font.render("Choose Your Professor", True, BLACK)
            screen.blit(title_text, (200,150))

            #professors as buttons
            prof_x = 150
            prof_y = 300
            for i in range(len(prof_names)):
                button = Button(prof_x + i*200, prof_y, 120, 120, prof_names[i])
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
                screen.blit(selected_prof, (350,130))

            #positions of clothing to manquine
            #shirt
            if current_shirt:
                screen.blit(current_shirt, (330, 210)) 
            #pants
            if current_pants:
                screen.blit(current_pants, (320, 320))
            #shoes
            if current_shoes:
                screen.blit(current_shoes, (325, 420))
            #hat
            if current_hat:
                screen.blit(current_hat, (360, 95))   

            #slidedown menu button
            if menu_y > -menu_height:
                #menu background
                pygame.draw.rect(screen, (220,220,220), (0, menu_y, screen_width, menu_height))
                draw_button_with_offset(shirts_cat_button, menu_y)
                draw_button_with_offset(pants_cat_button, menu_y)
                draw_button_with_offset(shoes_cat_button, menu_y)
                draw_button_with_offset(hats_cat_button, menu_y)

        
                if shirts_open:
                    for button in shirt_buttons:
                        draw_button_with_offset(button, menu_y)
                if pants_open:
                    for button in pants_buttons:
                        draw_button_with_offset(button, menu_y)
                if shoes_open:
                    for button in shoes_buttons:
                        draw_button_with_offset(button, menu_y)
                if hats_open:
                    for button in hat_buttons:
                        draw_button_with_offset(button, menu_y)

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
                screen.blit(score_text, (380, 250))

        pygame.display.update()
        clock.tick(60)  # something chat made me do to control the animations

    pygame.quit()


#running the game
if __name__ == "__main__":
    main()