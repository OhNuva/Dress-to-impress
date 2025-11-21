import pygame
import sys
import random

pygame.init()

# Screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Start Up Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)

# png background file 
background_1 = pygame.image.load("start_up_page.png")
background_1 = pygame.transform.scale(background_1, (screen_width, screen_height))
background_1 = None  


#button class type  
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        color = LIGHT_GRAY if self.rect.collidepoint(mouse) else GRAY
        pygame.draw.rect(surface, color, self.rect)

        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


# button graphics
start_button = Button(250, 250, 200, 50, "Start")
exit_button  = Button(470, 250, 200, 50, "Exit")

# male / female buttons
male_button   = Button(200, 250, 180, 50, "Male")
female_button = Button(420, 250, 180, 50, "Female")

#female character buttons
pendar_button=Button(250, 250, 300, 50, "~Pendar Mahmoudi~")
comfort_button=Button(250, 320, 300, 50, "~Comfort Mintah~")
dean_wells_button=Button(250, 390, 300, 50,"~Dean Mary Wells~")

#male character buttons
tam_button=Button(250, 250, 300, 50, "~Michael Tam~")
hamiltom_button=Button(250, 320, 300, 50, "~Jordan Hamilton~")
boxin_button=Button(250, 390, 300, 50, "~Boxin Zhao~")
                      

#definig the pages 
START_PAGE = "start"
GENDER_PAGE = "gender"
CHARACTER_PAGE= "character"

current_page = START_PAGE

#main loop
def main():
    global current_page, selected_gender
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # start_up_page 
            if current_page == START_PAGE:

                # Button clicker 
                if start_button.is_clicked(event):
                    print("start button clicked! Going to Male/Female page...")
                    current_page = GENDER_PAGE  

                if exit_button.is_clicked(event):
                    print("exit button clicked (exit the terminal)")
                    pygame.quit()
                    sys.exit()

            #gender_page
            elif current_page == GENDER_PAGE:

                if male_button.is_clicked(event):
                    print("Male Selected! (Next scene here)")
                    selected_gender="male"
                    current_page=CHARACTER_PAGE

                if female_button.is_clicked(event):
                    print("Female Selected! (Next scene here)")
                    selected_gender="female"
                    current_page=CHARACTER_PAGE
            
            #character_page
            elif current_page == CHARACTER_PAGE:
                
                if selected_gender=="female":
                    if pendar_button.is_clicked(event): 
                        print("You selected Pendar Mahmoudi!!!")
                    if comfort_button.is_clicked(event):
                        print("You selected Comfort Mintah!")
                    if dean_wells_button.is_clicked("You selected Dean Mary Wells!"):
                
                if selected_gender=="male":
                    if tam_button.is_clicked(event):
                        print("You selected Michael Tam!")
                    if hamilton_button.is_clicked(event):
                        print("You selected Jordan Hamilton!")
                    if boxin_button.is_clicked(event):
                        print("You selected Boxin Zhao!")
                           

        # Images 
        #background for page 1
        if current_page == START_PAGE:
            if background_1:
                screen.blit(background_1, (0, 0))
            else:
                screen.fill(WHITE)

            start_button.draw(screen)
            exit_button.draw(screen)

        # gender selection page
        elif current_page == GENDER_PAGE:
            screen.fill((230, 230, 255))  
            title_font = pygame.font.SysFont("Arial", 40)
            title_text = title_font.render("Choose Your Character", True, BLACK)
            screen.blit(title_text, (220, 150))

            male_button.draw(screen)
            female_button.draw(screen)
        
        #character selection page
        elif current_page== CHARACTER_PAGE:
            screen.fill((255, 240, 230))
            title_font= pygame.font.SysFont("Arial",40)
            title_text=title_font.render("Choose your Professor", True, BLACK)
            screen.blit(title_text, (240, 150))
            
            if selected_gender=="female":
                pendar_button.draw(screen)
                comfort_button.draw(screen)
                dean_wells_button.draw(screen)
                
            elif selected_gender == "male":
                tam_button.draw(screen)
                hamiltom_button.draw(screen)
                boxin_button.draw(screen)

        pygame. display.update()
        #character selection page
        
    pygame.quit()


#running the game
if __name__ == "__main__":
    main()
