#Basic version of the game of rock, paper and scissors

import os
from msvcrt import getch

def initial_setup():
      os.system('cls')
      print("\n") #dla czytelnosci
      print("Welcome to the Rock, Paper, Scissors Game!")
      print("Two people are required to play, obviously.")
      print("Press Enter to start the game...")
      while(True):
            key_pressed= ord(getch())
            if key_pressed == 13: #enter
                  return
            elif key_pressed == 27: #escape
                  quit()
  
"""
def check_input(key_pressed,key_desired, max_tries):
      tries = 0
      while tries<max_tries:  
            if key_pressed != key_desired:
                  print("That's not ", chr(key_desired), "you dumb idiot!")
                  print("Try again...")
            tries += 1 
      print("Go play something else.....")
      quit()
"""

def collect_input():
      viable_inputs = ["rock", "paper","scissors"]
      tries=0
      os.system('cls')
      while(True):
            p1_input = input("Player 1: Enter 'rock', 'paper, or 'scissors': ")
            if p1_input in viable_inputs:
                  os.system('cls')
                  break
            else:
                  print("Your input is incorrect!!!")
                  if tries == 2: quit()
                  tries+=1
                  
      tries=0
      while(True):
            p2_input = input("Player 2: Enter 'rock', 'paper, or 'scissors': ")
            if p2_input in viable_inputs:
                  os.system('cls')
                  break
            else:
                  print("Your input is incorrect!!!")
                  if tries == 2: quit()
                  tries+=1       
      return p1_input, p2_input

def calculate_input(p1,p2):
      if p1==p2:
            print("It's a tie!")
      elif p1=="rock" and p2=="scissors" or p1=="paper" and p2=="rock" or p1=="scissors" and p2=="paper":
            print("Player 1 won the game!")
      elif p2=="rock" and p1=="scissors" or p2=="paper" and p1=="rock" or p2=="scissors" and p1=="paper":
            print("Player 2 won the game!")
 
def quit_or_play():
        print("Press Enter to play again, or Escape to quit...")
        while(True):
            play_again = ord(getch())
            if play_again == 27:
                quit()
            elif play_again == 13:
                break  
            
def main():
      while(True): 
            initial_setup()
            p1_choice, p2_choice = collect_input()
            calculate_input(p1_choice,p2_choice)
            quit_or_play()

main()