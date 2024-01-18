import requests
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
# Coords * 3
window.geometry("1080x540")
window.title("ISS position with Python")
window.config(
  background="black"
)

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

window.mainloop()

######---- http://api.open-notify.org/iss-now.json ---######
######---- http://api.open-notify.org/astros.json ----######