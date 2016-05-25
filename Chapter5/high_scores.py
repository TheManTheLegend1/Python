# High Scores
# Demonstrates list methods

scores = []

choice = None

while choice != "0":
    print(
        """
           High scores
           
           0 - exit
           1 - Show Scores 
           2 - Add a Score 
           3 - Delete a Score 
           4 - Sort Score  
        """
    )
    choice = input("Choice: ")
    print()
    
    # Exit 
    if choice == "0":
        print("Good-bye")
        
    # List high-score table
    elif choice == "1":
        print("High Score")
        for score in scores:
            print(score)
            
    # add a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)
        
    # remove a score
    elif choice == "3":
        score = int(input("Remove which score?:"))
        if score in scores:
            scores.remove(score)
        else:
            print(score, " isnt in the high scores list.")
            
    # sort scores
    elif choice == "4":
        scores.sort(reverse=True)
        
    # Some unkown choice 
    else:
        print("Sorry, but", choice, "isnt a valid choice.")
        
input("\n\nPress the enter key to exit")
