import random #import random library

boxes = {'box 1':10, 'box 2': 4000, 'box 3': 1000000, 'box 4': 600, 'box 5': 100} #a dictionary called boxes; 'box 1' is the key and 10 is its value

def game(): #function called game

    one_box = random.choice(list(boxes)) #first box gets randomly chosen from the list of boxes
    list(boxes).remove(one_box) #that box gets removed from the list

    other_box = random.choice(list(boxes)) #second box then also gets randomly chosen

    print("You got " + str(one_box) + ".") #user gets feedback on which box they got

    
    choice = input("Would you like to stick with this box? Type in Yes or No.") #user gets asked whether they want to keep the box

    if choice == "Yes": #if the user wants to keep their box
        print("The value of your box is " + str(boxes.get(one_box)) + ".") #the value of his box gets printed
        print("The value of the other box is " + str(boxes.get(other_box)) + ".") #the value of the second box gets printed
        if (boxes[one_box]) > (boxes[other_box]): #if user box is bigger than the second box
            print("You won!") #user gets feedback that they have won
        else: #if the user box is smaller than the other box
            print("You lose!")#user gets input that they have lost
                
    elif choice == "No": #if the user wants to change their box
        print("Your new box is " + str(other_box) + " and its value is " + str(boxes.get(other_box)) + ".")
        #user finds out their new box and its value
        print("The value of the other box is " + str(boxes.get(one_box)) + ".")
        #user finds out value of the other box
        if  (boxes[other_box]) > (boxes[one_box]):
            print("You won!")
        else:
            print("You lose!")

    else: #if the user types in anything other than Yes or No
        print("Write only Yes and No!")
        game() #the function gets called and starts again
        
game() #call to function



##COMMENTS##
#Every now and then box 2 generates the same value as box 1 which means I haven't implemented .remove properly.
#Also, sometimes when the box the user chose is smaller, the 'score' comes out as "You've won!" which is false.
#I haven't been able to fix these issues but other than that everything seems to work!
    

  
        
