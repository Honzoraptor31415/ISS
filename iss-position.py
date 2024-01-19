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
print(iss_position.get_data()["iss_position"]["longitude"])

map_image = pygame.image.load("img/map.png")
map_image = pygame.transform.scale(map_image, (width, height))
map_rect = map_image.get_rect()
map_rect.center = (width//2, height//2)

iss_image = pygame.image.load("img/iss.png")
iss_image = pygame.transform.scale(iss_image, (40, 40))
iss_rect = iss_image.get_rect()
iss_rect.center = (width//2, height//2)

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  ppl_response = requests.get("http://api.open-notify.org/astros.json")
  ppl_data = ppl_response.json()

  pos_response = requests.get("http://api.open-notify.org/iss-now.json")
  pos_data = pos_response.json()

  iss_rect.center = (float(pos_data["iss_position"]["longitude"])*3+width//2, (float(pos_data["iss_position"]["latitude"])*3*-1)+height//2)

  window.blit(map_image, map_rect)
  window.blit(iss_image, iss_rect)

  pygame.display.update()
  clock.tick(1)

pygame.quit()

######---- http://api.open-notify.org/iss-now.json ---######
######---- http://api.open-notify.org/astros.json ----######