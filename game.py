from random import randint

player=input('rock(r),paper(p),scissors(s)?')
print(player, 'vs' , end=' ')
choosen = randint(1,3)
#print(choosen)
if choosen == 1:
  computer = 'r'
elif choosen == 2:
  computer = 'p'
else :
  computer = 's'
print(computer)
if player==computer:
  print('draw!')
elif player=='r' and computer=='p' :
  print('computer wins')
elif player=='p' and computer=='r' :
  print('you wins')
elif player=='r' and computer=='s' :
  print('player wins')
elif player=='s' and computer=='r' :
  print('computer wins')  
elif player=='s' and computer=='p' :
  print('player wins')
elif player=='p' and computer=='s' :
  print('computer wins')  
  
