#For Linda & Arianna
#you guys sort it bettwen yourselfs thing that still nee dto be added: 
 #-graphics (profs/closet) (for clothes i added 4 of each piece but feel free to add more or less its bacaully a copt and paste)
 #-music (find a sound and impoirt it into the document you can search up how to do it)
 #-font (we have arial as a defult cause thats the only one in pythons software but yo uhave to downlrad one online and basically change the 'ariel' parts to whatever font you selected.)
 #-level two? (if you guys want to do that you can, im lowkey tapped out of this code, unless tehre is probelms with it)
 #-doc string (this i will help, cause i undestand the code better, i can also write but like not today idk)
 # pls i beg try to get itdone by sunday i dont want this to be any more4 of our problems for the wek, so we can acc test and show it to pender on monday, I really wanna study this week.
 #last note: if you have thing to say about my poor grammer and spelling stfu 

import pygame
import sys
import random

pygame.init()

'''
doc string please
'''

#screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Start Up Page")

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)

#png background file
background_1 = pygame.image.load("background_one.png")
background_1 = pygame.transform.scale(background_1, (screen_width, screen_height))
background_2 = pygame.image.load("background_two.png")
background_2 = pygame.transform.scale(background_2, (screen_width, screen_height))
background_3 = pygame.image.load("background_three.png")
background_3 = pygame.transform.scale(background_3, (screen_width, screen_height))
background_4 = pygame.image.load("background_four.png")
background_4 = pygame.transform.scale(background_4, (screen_width, screen_height))
background_ranking = pygame.image.load("background_five.png")
background_ranking = pygame.transform.scale(background_ranking, (screen_width, screen_height))

#define all the varibales here: 
ranking_score= None
current_page = "start"
selected_prof = None
prof_list = []
prof_names = []

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

#ranking button
ranking_button = Button(300, 400, 200, 50, "Submit")

#button graphics
start_button = Button(250, 250, 200, 50, "Start")
exit_button  = Button(470, 250, 200, 50, "Exit")

#male/female buttons
male_button   = Button(200, 250, 180, 50, "Male")
female_button = Button(420, 250, 180, 50, "Female")

<<<<<<< HEAD
#defining the pages
=======
#definig the pages
>>>>>>> 9a9ec61393186e6eb85edc46d04624608169738a
start_page = "start"
gender_page = "gender"
ranking_page = "ranking"
prof_page = "prof_selection"
mannequin_page = "mannequin"

#professor_png
#female professors
<<<<<<< HEAD
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
=======
pendar = pygame.image.load("pendar.png")
pendar = pygame.transform.scale(pendar, (100, 100))
comfort = pygame.image.load("comfort.png")
comfort = pygame.transform.scale(comfort, (100, 100))
mary = pygame.image.load("mary.png")
mary = pygame.transform.scale(mary, (100, 100))

#male professors
michael = pygame.image.load("michael.png")
michael = pygame.transform.scale(michael, (100, 100))
jordan = pygame.image.load("jordan.png")
jordan = pygame.transform.scale(jordan, (100, 100))
boxin = pygame.image.load("boxin.png")
>>>>>>> 9a9ec61393186e6eb85edc46d04624608169738a
boxin = pygame.transform.scale(boxin, (100, 100))

#lists of all profs
female_profs = [pendar, comfort, mary]
female_names = ["Pendar Mahmoudi", "Comfort Mintah", "Mary Wells"]
male_profs = [michael, jordan, boxin]
male_names = ["Michael Tam", "Jordan Hamilton", "Boxin Zhao"]

#shirts
shirt_list = []
for i in range(1, 5):
    surf = pygame.image.load(f"shirt{i}.png")
    surf = pygame.transform.scale(surf, (140, 140))
    shirt_list.append(surf)

#pants
pants_list = []
for i in range(1, 5):
    surf = pygame.image.load(f"pants{i}.png")
    surf = pygame.transform.scale(surf, (160, 140))
    pants_list.append(surf)

#shoes
shoes_list = []
for i in range(1, 5):
    surf = pygame.image.load(f"shoes{i}.png")
    surf = pygame.transform.scale(surf, (140, 60))
    shoes_list.append(surf)

#hats
hat_list = []
for i in range(1, 5):
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

#Positions of clothing items inside the closet
item_x_start = 40
item_y_start = 60
item_gap_x = 170
#shirts
for i in range(4):
    button = Button(item_x_start + i*item_gap_x, item_y_start, 140, 140, f"S{i+1}", image=shirt_list[i])
    shirt_buttons.append(button)
#pants
for i in range(4):
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
            if background_1:
                screen.blit(background_1, (0, 0))
            else:
                screen.fill(WHITE)

            start_button.draw(screen)
            exit_button.draw(screen)

        #gender selection page
        elif current_page == gender_page:
            if background_2:
                screen.blit(background_2, (0, 0))
            else:
                screen.fill((230, 230, 255))  
            title_font = pygame.font.SysFont("Arial", 40)
            title_text = title_font.render("Choose Your Character", True, BLACK)
            screen.blit(title_text, (220, 150))

            male_button.draw(screen)
            female_button.draw(screen)

        #professor selection page
        elif current_page == prof_page:
            if background_3:
                screen.blit(background_3, (0,0))
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
            if background_4:
                screen.blit(background_4, (0,0))
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