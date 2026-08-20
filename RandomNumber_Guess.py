import random   # pythons built in module
import time      # pythons built in module

def Random_Guess():
    number=random.randint(1,100)  #to generate a random integer number
    
    
    print("I have selected a random number,Try to guess the number - ")
    start_time=time.perf_counter() # this is the built in module to calculate the exact start time 
    
    while True:
        try:
            guess=int(input("Enter your number you have  guesed - "))
            
            
            if guess<1 or guess >100:
                print("Please guess a number between 1 and 100")
                
            elif guess < number:
                print ("Wrong answer... Too low")
            elif guess > number:
                print ("Wrong answer... Too High")   
            else:
                endtime=time.perf_counter()  # to calculate the end time to guess the nulmer
                timeTaken=endtime -  start_time   # this is the time taken from start to end to guess the number to check how fast it took to guess the number.
                print("The number " + str(number)+ " guesed was correct" )
                print(f"time taken :{timeTaken} seconds" )
                break
                
        except ValueError:
               print ("Invalid input please try again")
               
    
Random_Guess()
            