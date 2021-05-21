import itertools
import os 
os.system('clear')
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
logo =f"""{y}
           [wordlister]{r}
       █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█                                 █
█                                 █
█   █████                 █████   █
█  ██▓▓▓███             ███▓▓▓██  █
█  ██▓▓▓▓▓██           ██▓▓▓▓▓██  █
█  ██▓▓▓▓▓▓██         ██▓▓▓▓▓▓██  █
█▄  ████▓▓▓▓██       ██▓▓▓▓████  ▄█
▀█▄   ▀███▓▓▓██     ██▓▓▓███▀   ▄█▀
  █▄    ▀█████▀     ▀█████▀    ▄█
 ▄██           ▄█ █▄           ██▄
 ███           ██ ██           ███
 ███                           ███
  ▀██  ██▀██  █  █  █  ██▀██  ██▀
   ▀████▀ ██  █  █  █  ██ ▀████▀
    ▀██▀  ██  █  █  █  ██  ▀██▀
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█
           
         {g}by BLINKING-IDIOT
      insta: @a.r.n.beatzzzz
"""
print(logo)
k = 'abcdefghijklmnopqrstuvwxyz'
y=input("Do you what to add numbers? (y/n)")
if y=='y':
	k+='1234567890'
le = int(input("Enter the length of words using:"))
for i in itertools.product(k, repeat=le):
 x=(''.join(i))
 print (x)
print("finished")
