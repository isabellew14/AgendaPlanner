
import time
# identifies the month and places the inputted event in the correct file
def month_Append(x):
        if x == "01":
            with open("jan.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy)) #appends the file
                    
        if x == "02":
            with open("feb.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "03":
            with open("mar.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "04":
            with open("apr.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "05":
           with open("may.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "06":
            with open("jun.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "07":
           with open("jul.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "08":
           with open("aug.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "09":
           with open("sep.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "10":
           with open("octo.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "11":
           with open("nov.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
        if x == "12":
            with open("dec.txt","a") as f:
                    f.write("\nDate: {}\nEvent Details:{}\r" .format(datey , eventy))
                    
# identifies the correct file based on month
def month_Find(x):
        if x == "01":
            month= "jan.txt"
            return month
        if x == "02":
            month= "feb.txt"
            return month
        if x == "03":
            month= "mar.txt"
            return month
        if x == "04":
            month= "apr.txt"
            return month
        if x == "05":
            month= "may.txt"
            return month
        if x == "06":
            month= "jun.txt"
            return month
        if x == "07":
            month= "jul.txt"
            return month
        if x == "08":
            month= "aug.txt"
            return month
        if x == "09":
            month= "sep.txt"
            return month
        if x == "10":
            month= "octo.txt"
            return month
        if x == "11":
            month= "nov.txt"
            return month
        if x == "12":
            month= "dec.txt"
            return month
        
#prints all of the inputed events (all months)
def viewAll():
       with open("jan.txt") as jan, open("feb.txt") as feb,open("mar.txt") as mar,open("apr.txt") as apr,open("may.txt") as may,open("jun.txt") as jun,open("jul.txt") as jul,open("aug.txt") as aug,open("sep.txt") as sep,open("octo.txt") as octo,open("nov.txt") as nov,open("dec.txt") as dec:
              events= jan.readlines() +  feb.readlines() + mar.readlines() + apr.readlines() + may.readlines() + jun.readlines() +  jul.readlines() + aug.readlines() + sep.readlines() + octo.readlines() + nov.readlines() + dec.readlines()
              print ("/"*100)
              
              for lines in events[0:]:
                      print (lines)
                      
              print ("/"*100)
#prints one specific month
def viewOne(x):
        if x == "January" or x == "january":
                 with open("jan.txt") as jan:
                         events= jan.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
                                 
        elif x == "February" or x == "february":
                 with open("feb.txt") as feb:
                         events= feb.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "March" or x == "march":
                 with open("mar.txt") as mar:
                         events= mar.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "April" or x == "april":
                 with open("apr.txt") as apr:
                         events= apr.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "May" or x == "may":
                 with open("may.txt") as may:
                         events= may.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)                                
                         
        elif x == "June" or x == "june":
                 with open("jun.txt") as jun:
                         events= jun.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)                         
        elif x == "July" or x == "July":
                 with open("jul.txt") as jul:
                         events= jul.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)                 
        elif x == "August" or x == "august":
                 with open("aug.txt") as aug:
                         events= aug.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "September" or x == "september":
                 with open("sep.txt") as sep:
                         events= sep.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "October" or x == "october":
                 with open("octo.txt") as octo:
                         events= octo.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "November" or x == "november":
                 with open("nov.txt") as nov:
                         events= nov.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        elif x == "December" or x == "december":
                 with open("dec.txt") as dec:
                         events= dec.readlines()
                         for lines in events[0:]:
                                 print (lines)
                                 print ("*"*100)
        else:
                print ("\nInvalid")
########################################################################################################################################################
print ("This is an event planner brought to you by FIMA")                                                  
while True:
    
    ask= input("\n What do you want to do?\n a)instructions\n b)view\n c)add\n d)edit\n e)remove\n f)Exit\n ")
    #Shows instructions
    if ask == "a" or ask == "A":
        print ("INSTRUCTIONS")
        print ("- This is a program to keep track of your events/appointments.")
        print ("- The events are stored in a monthly basis.\n- Choose add in the menu in order to create a new event. While doing so, PLEASE ENTER THE DATE IN THE ORDER OF DD/MM/YY")
        print ("- Select delete in order to delete any events")
        print ("- To edit events select edit.")
        print ("- Select view to view the events in your agenda.")
    # View events
    elif ask == "b" or ask == "B":
            monthy = input("\nDo you wish to view A) all months or B)one particular month?\n")
            if monthy == "A" or monthy == "a":
                    viewAll()      #calls function that views all months
            elif monthy == "B" or monthy == "b":
                    monthly= input("\nWhich month do you wish to view?(please enter full month name):")
                    viewOne(monthly) #calls function that views a specific month
            else:
                    print ("\nInvalid")
               
     #Add events   
    elif ask == "c" or ask == "C":
        valid = False    
        while not valid: #makes sure date is inputted in correct format
                datey = input("What is the date of your event(DD/MM/YY):\n")                
                try:
                        time.strptime(datey, "%d/%m/%y")
                        valid = True
                        
                except ValueError:
                        print ("Invalid, please try again\n")
                        valid = False
                        
        
        eventy= input ("Enter description:")
        month_Append(datey[3:5]) # index [3:5] gives the number of the month (MM)
    #Edit events
    elif ask == "d" or ask == "D":
            
            edity = input("Do you wish to edit A) the date or B) the description:")
            if edity == 'A' or edity == 'a':
                  valid = False    
                  while not valid:    #this makes sure date is inputted in correct format
                        datey = input("What is the date of your event(DD/MM/YY):\n")
                        try:
                                time.strptime(datey, "%d/%m/%y")
                                valid = True
                        
                        except ValueError:
                                print ("Invalid, please try again\n")
                                valid = False
                  valid = False 
                  while not valid: #makes sure date in in correct foramt
                        newdatey= input("Enter the new date:(DD/MM/YY)")
                        try:
                                time.strptime(newdatey, "%d/%m/%y")
                                valid = True
                                break
                        except ValueError:
                                print ("Invalid, please try again\n")
                                valid = False
                        
                  month= month_Find(datey[3:5])
                     
                  with open(month) as f:
                        lines= f.readlines()
                        for i in range (len(lines)):
                                        if datey in lines[i]: #finds the line in the file that corresponds to the date
                                                lines[i]= "Date: " + newdatey + '\n' #edits the date
                                                with open(month, 'w') as f:  #rewrites whole file with the new edits
                                                        f.writelines(lines)
                    
                  
            elif edity == 'B' or edity == 'b':
                  valid = False    
                  while not valid:
                        datey = input ("What is the date of the description that you want to change?")
                        try:
                                time.strptime(datey, "%d/%m/%y")
                                valid = True
                        
                        except ValueError:
                                print ("Invalid, please try again\n")
                                valid = False
                        
                  month= month_Find(datey[3:5]) 
                  with open(month) as f:
                        lines= f.readlines()
                        newdesty= input("Enter new description:\n")
                        for i in range (len(lines)):
                                        if datey in lines[i]: #finds the line in the file that corresponds to the date
                                                lines[i+1]= "Event Details: " + newdesty #edits the description 
                                                with open(month, 'w') as f:  #rewrites whole file with the new edits
                                                        f.writelines(lines)
                      
            else:
                  print ("\nInvalid")
                                                  
     #Remove events       
    elif ask == "e" or ask == "E":
            valid = False    
            while not valid:
                datey= input("Enter date you wish to remove(DD/MM/YY):")           
                try:
                        time.strptime(datey, "%d/%m/%y")
                        valid = True
                                        
                except ValueError:
                        print ("Invalid, please try again\n")
                        valid = False
            month= month_Find(datey[3:5])
            with open(month) as f:
                 
                 lines= f.readlines()
                 for i in range (len(lines)):
                                 if datey in lines[i]: #finds the line in the file that corresponds to the date
                                         lines[i]= ""  #makes line empty
                                         lines[i+1]= ""  
                                         with open(month, 'w') as f:  #rewrites whole file with the new edits
                                                 f.writelines(lines)
       
                 
                                   
                       
    #exit program
    elif ask == "f" or ask == "F":
            break
        
    else:
        print ("\nInvalid\n")
        
        
     
