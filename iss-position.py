import requests
import pygame

pygame.init()
width = 1080
height = 540
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("ISS with Python")

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

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  window.fill("black")

pygame.quit()

######---- http://api.open-notify.org/iss-now.json ---######
######---- http://api.open-notify.org/astros.json ----######