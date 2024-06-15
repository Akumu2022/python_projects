print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~                                 ~")
print("~   Computer Science Revision     ~")
print("~        Progress Tracker         ~")
print("~                                 ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

topics = ["System Architecture",
          "Memory and Storage",
          "Computer Networks",
          "Network Security",
          "Systems Software",
          "Ethical, Legal, Cultural & environmental Impacts of digital technology",
          "Algorithms",
          "Programming Fundamentals",
          "Producing Robust Programs",
          "Boolean Logic",
          "Programming Languages and IDEs"]

no_of_topics=len(topics)
rev_score=0
for topic in topics:
    revised=input(f"Did you complete revision about {topic} (Yes or No)?")
    if revised.lower() == "yes":
        no_of_topics+=1
        rev_score+=1
        print(revised)
        continue
        
    elif revised.lower() == "no":
        print(revised)
        continue
    else:
        print("invalid input")
        break

def calc_per_score():
    percentage=float(rev_score/no_of_topics)*100
    
    if percentage<40:
        print(f"You can not sit exams because your score is {percentage}")
        
    else:
        
        print(f"Your Revision Score is: {percentage}%\nYou can sit exams")

calc_per_score()





    
        
          
  
            

