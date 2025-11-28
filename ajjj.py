import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

'''
The following will provide the music audio that will be played throughout the game. 
'''

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

# screen size
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

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)

# backgrounds
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
>>> timer_enabled : bool
>>> timer_limit : int
A timer of 40 seconds will be incorporated into the game.
'''

# game state variables
ranking_score = None
current_page = "start"
selected_prof = None
prof_list = []
prof_names = []

# Timer settings
timer_enabled = True
time_limit = 40
start_time = None

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

# Button class
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
        if self.image:
            iw, ih = self.image.get_size()
            bw, bh = self.rect.w - 8, self.rect.h - 28
            scale = min(bw / iw, bh / ih)
            img2 = pygame.transform.scale(self.image, (max(1, int(iw * scale)), max(1, int(ih * scale))))
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
>>> yes_button : Button
Allows users to select yes when prompted to play again, #positioned at ()
>>> no_button : Button
Allows users to select no when prompted to play again, 
'''

# UI buttons
start_button = Button(300, 500, 200, 50, "Start")
exit_button = Button(520, 500, 200, 50, "Exit")
male_button = Button(320, 450, 180, 50, "Male")
female_button = Button(540, 450, 180, 50, "Female")
yes_button = Button(300, 500, 200, 50, "Yes")
no_button = Button(520, 500, 200, 50, "No")

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

# pages
start_page = "start"
gender_page = "gender"
prof_page = "prof_selection"
mannequin_page = "mannequin"
ranking_page = "ranking"

'''
The following displays the professor avatars that may be chosen and the associated name of the professor.
Each professor image is loaded from the `images/` directory and scaled to
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

# professor images
pendar = pygame.image.load("Images/pendar_cartoon_trans.png"); pendar = pygame.transform.scale(pendar, (110, 110))
comfort = pygame.image.load("Images/comfort_cartoon_trans.png"); comfort = pygame.transform.scale(comfort, (110, 110))
mary = pygame.image.load("Images/dean_mary_cartoon_trans.png"); mary = pygame.transform.scale(mary, (110, 110))
michael = pygame.image.load("Images/tam_cartoon_trans.png"); michael = pygame.transform.scale(michael, (110, 110))
jordan = pygame.image.load("Images/jhammy_cartoon_trans.png"); jordan = pygame.transform.scale(jordan, (110, 110))
boxin = pygame.image.load("Images/boxin_cartoon_trans.png"); boxin = pygame.transform.scale(boxin, (110, 110))

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
shirt3 = pygame.transform.scale(shirt3, (455, 300))
shirt4 = pygame.image.load("Images/shirt4.png")
shirt4 = pygame.transform.scale(shirt4, (420, 300))
shirt5 = pygame.image.load("Images/shirt5.png")
shirt5 = pygame.transform.scale(shirt5, (365, 300))
shirt6 = pygame.image.load("Images/shirt6.png")
shirt6 = pygame.transform.scale(shirt6, (460, 300))
shirt7 = pygame.image.load("Images/shirt7.png")
shirt7 = pygame.transform.scale(shirt7, (460, 300))

# clothing images
shirt1 = pygame.image.load("Images/shirt1.png"); shirt1 = pygame.transform.scale(shirt1, (385, 300))
shirt2 = pygame.image.load("Images/shirt2.png"); shirt2 = pygame.transform.scale(shirt2, (450, 300))
shirt3 = pygame.image.load("Images/shirt3.png"); shirt3 = pygame.transform.scale(shirt3, (455, 300))
shirt4 = pygame.image.load("Images/shirt4.png"); shirt4 = pygame.transform.scale(shirt4, (420, 300))
shirt5 = pygame.image.load("Images/shirt5.png"); shirt5 = pygame.transform.scale(shirt5, (365, 300))
shirt6 = pygame.image.load("Images/shirt6.png"); shirt6 = pygame.transform.scale(shirt6, (460, 300))
shirt7 = pygame.image.load("Images/shirt7.png"); shirt7 = pygame.transform.scale(shirt7, (460, 300))

pants1 = pygame.image.load("Images/pants1.png"); pants1 = pygame.transform.scale(pants1, (742, 400))
pants2 = pygame.image.load("Images/pants2.png"); pants2 = pygame.transform.scale(pants2, (315, 350))
pants3 = pygame.image.load("Images/pants3.png"); pants3 = pygame.transform.scale(pants3, (370, 350))
pants4 = pygame.image.load("Images/pants4.png"); pants4 = pygame.transform.scale(pants4, (380, 300))
pants5 = pygame.image.load("Images/pants5.png"); pants5 = pygame.transform.scale(pants5, (380, 350))

shoe1 = pygame.image.load("Images/shoe1.png"); shoe1 = pygame.transform.scale(shoe1, (200, 100))
shoe2 = pygame.image.load("Images/shoe2.png"); shoe2 = pygame.transform.scale(shoe2, (200, 100))
shoe3 = pygame.image.load("Images/shoe3.png"); shoe3 = pygame.transform.scale(shoe3, (200, 100))

hat1 = pygame.image.load("Images/hat1.png"); hat1 = pygame.transform.scale(hat1, (95, 70))
hat2 = pygame.image.load("Images/hat2.png"); hat2 = pygame.transform.scale(hat2, (95, 70))
hat3 = pygame.image.load("Images/hat3.png"); hat3 = pygame.transform.scale(hat3, (95, 70))

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

# selected clothing
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

# closet sliding menu
closet_open = False
menu_height = 320
menu_y = -menu_height
menu_speed = 18
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

# closet category buttons
closet_button = Button(35, 35, 140, 50, "Closet")
shirts_cat_button = Button(20, 20, 140, 40, "Shirts")
pants_cat_button = Button(20, 70, 140, 40, "Pants")
shoes_cat_button = Button(20, 120, 140, 40, "Shoes")
hats_cat_button = Button(20, 170, 140, 40, "Hats")
close_closet_button = Button(20, 220, 140, 40, "Close")

shirt_buttons = []
pants_buttons = []
shoes_buttons = []
hat_buttons = []

# positions for closet items
item_x_start = 20
item_y_start = 280
item_gap_x = 160
item_gap_y_shirt = 120
item_gap_y_pant = 135
item_gap_y = 180
item_x_start_hat = 10

# shirts
for i in range(len(shirt_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y_shirt
    button = Button(x, y, 110, 110, f"S{i+1}", image=shirt_list[i])
    shirt_buttons.append(button)

# pants
for i in range(len(pants_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y_pant
    button = Button(x, y, 120, 120, f"P{i+1}", image=pants_list[i])
    pants_buttons.append(button)

# shoes
for i in range(len(shoes_list)):
    col = i % 2
    row = i // 2
    x = item_x_start + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 120, 90, f"Sh{i+1}", image=shoes_list[i])
    shoes_buttons.append(button)

# hats
for i in range(len(hat_list)):
    col = i % 2
    row = i // 2
    x = item_x_start_hat + col * item_gap_x
    y = item_y_start + row * item_gap_y
    button = Button(x, y, 120, 80, f"H{i+1}", image=hat_list[i])
    hat_buttons.append(button)

shirts_open = False
pants_open = False
shoes_open = False
hats_open = False

def draw_button_with_offset(button, offset_y):
    old_x = button.rect.x
    button.rect.x += offset_y
    button.draw(screen)
    button.rect.x = old_x

def is_clicked_with_offset(button, event, offset_y):
    old_x = button.rect.x
    button.rect.x += offset_y
    clicked = button.is_clicked(event)
    button.rect.x = old_x
    return clicked

def reset_game_state():
    global current_page, ranking_score, selected_prof, prof_list, prof_names
    global closet_open, menu_x, shirts_open, pants_open, shoes_open, hats_open
    global current_shirt, current_pants, current_shoes, current_hat
    global start_time

    # Go back to gender selection (you can change this to start_page if you prefer)
    current_page = gender_page

    ranking_score = None
    selected_prof = None
    prof_list = []
    prof_names = []

    closet_open = False
    menu_x = screen_width
    shirts_open = False
    pants_open = False
    shoes_open = False
    hats_open = False

    current_shirt = None
    current_pants = None
    current_shoes = None
    current_hat = None

    start_time = None

def main():
    global current_page, ranking_score, selected_prof, prof_list, prof_names
    global closet_open, menu_x, shirts_open, pants_open, shoes_open, hats_open
    global current_shirt, current_pants, current_shoes, current_hat
    global start_time, timer_enabled, time_limit

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # start page
            if current_page == start_page:
                if start_button.is_clicked(event):
                    current_page = gender_page
                if exit_button.is_clicked(event):
                    pygame.quit()
                    sys.exit()

            # gender page
            elif current_page == gender_page:
                if male_button.is_clicked(event):
                    current_page = prof_page
                    prof_list = male_profs
                    prof_names = male_names
                if female_button.is_clicked(event):
                    current_page = prof_page
                    prof_list = female_profs
                    prof_names = female_names

            # professor selection page
            elif current_page == prof_page:
                prof_buttons = []
                x_start = 160
                y_start = 420
                for i in range(len(prof_names)):
                    button = Button(x_start + i * 260, y_start, 220, 80, prof_names[i])
                    prof_buttons.append(button)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(prof_buttons)):
                        if prof_buttons[i].is_clicked(event):
                            selected_prof = prof_list[i]
                            start_time = pygame.time.get_ticks()
                            ranking_score = None
                            current_page = mannequin_page

            # mannequin page
            if current_page == mannequin_page:
                if closet_button.is_clicked(event):
                    closet_open = not closet_open
                    if not closet_open:
                        shirts_open = pants_open = shoes_open = hats_open = False

                if closet_open and event.type == pygame.MOUSEBUTTONDOWN:
                    offset = menu_x
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

        # animate sliding closet
        if closet_open:
            if menu_x > screen_width - menu_width:
                menu_x -= 18
                if menu_x < screen_width - menu_width:
                    menu_x = screen_width - menu_width
        else:
            if menu_x < screen_width:
                menu_x += 18
                if menu_x > screen_width:
                    menu_x = screen_width

        # drawing
        if current_page == start_page:
            screen.blit(background_one, (0, 0))
            start_button.draw(screen)
            exit_button.draw(screen)

        elif current_page == gender_page:
            screen.blit(background_two, (0, 0))
            title_font = pygame.font.SysFont("Arial", 48)
            title_text = title_font.render("Choose Your Character", True, BLACK)
            screen.blit(title_text, (325, 250))
            male_button.draw(screen)
            female_button.draw(screen)

        elif current_page == prof_page:
            screen.blit(background_three, (0, 0))
            title_font = pygame.font.SysFont("Arial", 48)
            title_text = title_font.render("Choose Your Professor", True, BLACK)
            screen.blit(title_text, (325, 250))
            prof_x = 160
            prof_y = 420
            for i in range(len(prof_names)):
                button = Button(prof_x + i * 260, prof_y, 220, 80, prof_names[i])
                button.draw(screen)

        elif current_page == mannequin_page:
            screen.blit(background_four, (0, 0))
            closet_button.draw(screen)
            if selected_prof:
                screen.blit(selected_prof, (450, 40))

            # timer display
            if timer_enabled and start_time is not None:
                elapsed = (pygame.time.get_ticks() - start_time) / 1000
                remaining = max(0, int(time_limit - elapsed))
                timer_font = pygame.font.SysFont("Arial", 40)
                timer_text = timer_font.render(f"Time Left: {remaining}", True, RED)
                screen.blit(timer_text, (800, 50))
                if remaining == 0:
                    ranking_score = random.randint(1, 10)
                    current_page = ranking_page
                    start_time = None

            # clothing overlays
            if current_shirt == shirt1:
                screen.blit(current_shirt, (315, 125))
            elif current_shirt == shirt2:
                screen.blit(current_shirt, (283, 125))
            elif current_shirt == shirt3:
                screen.blit(current_shirt, (282, 120))
            elif current_shirt == shirt4:
                screen.blit(current_shirt, (299, 135))
            elif current_shirt == shirt5:
                screen.blit(current_shirt, (324, 130))
            elif current_shirt == shirt6:
                screen.blit(current_shirt, (280, 120))
            elif current_shirt == shirt7:
                screen.blit(current_shirt, (280, 120))

            if current_pants == pants1:
                screen.blit(current_pants, (140, 300))
            elif current_pants == pants2:
                screen.blit(current_pants, (358, 330))
            elif current_pants == pants3:
                screen.blit(current_pants, (328, 295))
            elif current_pants == pants4:
                screen.blit(current_pants, (328, 330))
            elif current_pants == pants5:
                screen.blit(current_pants, (328, 330))

            if current_shoes == shoe1:
                screen.blit(current_shoes, (407, 600))
            elif current_shoes == shoe2:
                screen.blit(current_shoes, (407, 600))
            elif current_shoes == shoe3:
                screen.blit(current_shoes, (407, 600))

            if current_hat == hat1:
                screen.blit(current_hat, (457, 20))
            elif current_hat == hat2:
                screen.blit(current_hat, (457, 20))
            elif current_hat == hat3:
                screen.blit(current_hat, (457, 15))

            # sliding closet panel
            if closet_open or menu_x < screen_width:
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

        elif current_page == ranking_page:
            screen.blit(background_ranking, (0, 0))
            if ranking_score is not None:
                num_font = pygame.font.SysFont("Arial", 80)
                score_text = num_font.render(str(ranking_score), True, BLACK)
                screen.blit(score_text, (400, 300))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.is_clicked(event):
                    reset_game_state()
                elif no_button.is_clicked(event):
                    running = False
                
        pygame.display.update()
        clock.tick(40)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
