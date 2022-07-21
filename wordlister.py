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
      insta:  @_arxhr007_
"""
print(logo)
k = 'abcdefghijklmnopqrstuvwxyz'
y=input("Do you what to add numbers? (y/n)")
if y.lower()=='y':
	k+='1234567890'
le = int(input("Enter the minimum length of words :"))
q = int(input("Enter the maximun length of words :"))
for j in range(le,q+1):
 for i in itertools.product(k, repeat=j):
  x=(''.join(i))
  print (x)
print("finished")
