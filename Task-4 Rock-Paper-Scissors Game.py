#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing random library for random choices of computer
   
import random  

print("Hi! \nWelcome to Rock-Paper-Scissors !!")

options = ("rock", "paper", "scissors")

playing = True

# initialiing for displaying scores
player_score = 0
computer_score = 0

while playing:

   player = None
   computer = random.choice(options)      #for the computer to give random choice outputs

   while player not in options:
       player = input("Enter your choice :- (rock, paper, scissors):")

   print(f"Player: {player}")
   print(f"Computer: {computer}")
   
   
# selecting game choices and displaying desired outputs

   if player == computer:
       print("\n It's a tie!!")    #no one gets any point

   elif player == "rock" and computer == "scissors":
       print("\n You Win!!")
       player_score += 1          #player gets one point

   elif player == "paper" and computer == "rock":
       print("\n You Win!!")
       player_score += 1          #player gets one point

   elif player == "scissors" and computer == "paper":
       print("\n You Win!!")
       player_score += 1         #player gets one point

   else:
       print("\nYou Lose!")
       computer_score += 1       #computer gets one point

   print(f"Player Score: {player_score}")        #displays player's score
   
   print(f"Computer Score: {computer_score}")    #displays computer's score

   continue_game = input("\nDo you want to continue the game? (y/n)").lower()

   if not continue_game == "y": #if 'y', then the game continues & if 'n' , the game ends
       playing = False

print("\n Thanks for playing!!")

