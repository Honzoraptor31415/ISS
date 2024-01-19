import requests
import pygame

pygame.init()
width = 1080
height = 540
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("ISS with Python")

clock = pygame.time.Clock()

black = (20, 20, 20)

class ApiCall:
  def __init__(self, url):
    self.url = url
  
  def get_data(self):
    response = requests.get(self.url)
    data = response.json()
    return data

iss_people = ApiCall("http://api.open-notify.org/astros.json")
iss_position = ApiCall("http://api.open-notify.org/iss-now.json")

print(f"{iss_people.get_data()}\n\n")
print(iss_position.get_data())

map_image = pygame.image.load("img/map.png")
map_image = pygame.transform.scale(map_image, (width, height))
map_rect = map_image.get_rect()
map_rect.center = (width//2, height//2)

iss_image = pygame.image.load("img/iss.png")
iss_image = pygame.transform.scale(iss_image, (50, 50))
iss_rect = iss_image.get_rect()
iss_rect.center = (width//2, height//2)

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  window.blit(map_image, map_rect)
  window.blit(iss_image, iss_rect)

  # pygame.draw.line(window, black, (0, height), (width, height), 50)

  pygame.display.update()
  clock.tick(60)

pygame.quit()

######---- http://api.open-notify.org/iss-now.json ---######
######---- http://api.open-notify.org/astros.json ----######