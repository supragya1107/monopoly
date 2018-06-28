"""Ever played MONOPOLY?
This is a short code written for the game.
Game asks for the number of players in the beginning.
You should choose more than one player.
MADE BY-SUPRAGYA UPADHYAY :)
To start, execute the function game().
"""

###############################################################################

class Player:
    
    money=15.000                    #starting money
    
    def __init__(self,string):
        self.name=string
        #self.avatar=avatar
        self.properties={"Brown":[0],"LightBlue":[0],"Magenta":[0],"Orange":[0],
                    "Red":[0],"Yellow":[0],"Green":[0],"Blue":[0],"Services":[0]}
        self.plist=[]    

    bankrupt=False
    position=0
    in_jail=False
    

###############################################################################

no_of_players=0
players=[]                                                                          #list that contains objects of the class Player

###############################################################################

Place ={0 :"GO!!",                                                                  #These are the loacations on the board.
        1 :"Bhubhaneshwar",                                                         #There are 40 in total.
        2 :"Patna",                                                                 #
        3 :"Ranchi",                                                                #They are in groups of 3.
        4 :"Income Tax",                                                            #
        5 :"Air transport",                                                         #Groups are BROWN,LIGHTBLUE,MAGENTA,ORANGE,RED,YELLOW,GREEN,BLUE
        6 :"Shimla",                                                                #
        7 :"Lucknow",                                                               #If you own all 3 of a single colour the rent on each site doubles.
        8 :"Chance",                                                                #
        9 :"Jodhpur",                                                               #Also you become eligible to build hotel on any of those sites.
        10:"JAIL(Just Visiting)",                                                   #
        11:"Bhopal",                                                                #rent on a service will be proportional to number of services owned.
        12:"Gas services",                                                          #
        13:"Gandhinagar",                                                           #You get +$2.000 for completing round across te board.
        14:"Allahbad",                                                              #
        15:"Railway services",                                                      #You can mortgage any of your site for 90% of its cost but to unmortgage you need to pay full of its price again.
        16:"Varanasi",                                                              #
        17:"Pune",                                                                  #
        18:"Chance",                                                                #
        19:"Kanpur",                                                                #
        20:"FREE PARKING",                                                          #
        21:"Chandigarh",                                                            #
        22:"Chance",                                                                #
        23:"Ghaziabad",                                                             #
        24:"Jaipur",                                                                #
        25:"Telecom services",                                                      #
        26:"Ahmedabad",
        27:"Udaipur",
        28:"Electricity services",
        29:"Indore",
        30:"GO TO JAIL!!",
        31:"Kolkata",
        32:"Chennai",
        33:"Chance",
        34:"Hyderabad",
        35:"Railway services",
        36:"Chance",
        37:"Mumbai",
        38:"Banglore",
        39:"Delhi",}

###############################################################################

status={"GO!!"                  :["can't buy"],                                       #first is status, then price, rent, rent after hotel,  price of hotel
        "Chance"                :["can't buy"],
        "Income Tax"            :["can't buy"],
        
        "Patna"                 :["not bought",0.600,0.150,0.450,0.800],              #
        "Bhubhaneshwar"         :["not bought",0.600,0.150,0.450,0.800],              # brown
        "Ranchi"                :["not bought",0.650,0.200,0.500,1.000],              #
            
        "Air transport"         :["not bought",2.000,0.250],                          #            
        "Electricity services"  :["not bought",2.000,0.250],                          #
        "Railway services"      :["not bought",2.000,0.250],                          #
        "Water services"        :["not bought",2.000,0.250],                          # services   
        "Gas services"          :["not bought",2.000,0.250],                          #
        "Telecom services"      :["not bought",2.000,0.250],                          #
        
        "Shimla"                :["not bought",1.000,0.300,0.800,1.200],              #    
        "Lucknow"               :["not bought",1.000,0.300,0.800,1.200],              # light blue
        "Jodhpur"               :["not bought",1.200,0.350,0.900,1.500],              #
        
        "JAIL(Just Visiting)"   :["can't buy"],

        "Bhopal"                :["not bought",1.400,0.450,1.200,1.800],              #
        "Gandhinagar"           :["not bought",1.400,0.450,1.200,1.800],              # magenta
        "Allahbad"              :["not bought",1.600,0.550,1.300,2.000],              #

        "Varanasi"              :["not bought",1.800,0.600,1.500,2.500],              #
        "Pune"                  :["not bought",1.800,0.600,1.500,2.500],              # orange
        "Kanpur"                :["not bought",2.000,0.700,1.700,3.000],              #

        "FREE PARKING"          :["can't buy"],

        "Chandigarh"            :["not bought",2.200,0.800,2.000,3.500],              #
        "Ghaziabad"             :["not bought",2.200,0.800,2.000,3.500],              # red
        "Jaipur"                :["not bought",2.400,0.900,2.200,4.000],              #

        "Ahmedabad"             :["not bought",2.600,1.100,2.400,4.500],              #
        "Udaipur"               :["not bought",2.600,1.100,2.400,4.500],              # yellow
        "Indore"                :["not bought",2.800,1.200,2.600,5.000],              #
        
        "GO TO JAIL!!"          :["can't buy"],

        "Kolkata"               :["not bought",3.000,1.400,2.800,5.500],              #
        "Chennai"               :["not bought",3.000,1.400,2.800,5.500],              # green
        "Hyderabad"             :["not bought",3.200,1.500,3.000,6.000],              #

        "Banglore"              :["not bought",3.500,1.600,3.200,6.500],              #
        "Mumbai"                :["not bought",3.500,1.600,3.200,6.500],              # blue
        "Delhi"                 :["not bought",4.000,1.800,3.500,7.000]               #
        }
###############################################################################

"""You will receive 90% of money of the property you mortgage.
But you won't be able to charge rent from the property"""
def mortgage(i):

    available=[]
    for site in players[i].plist:
        if status[site][0]!="mortgaged":
            available.append(site)
    
    print("Your unmortgaged properties are",",".join(available))
    site=input("Enter the property you want to mortgage : ")

    if (site.capitalize() in players[i].plist) and (status[site.capitalize()][0]=="bought"):
        status[site.capitalize()][0]="mortgaged"
        players[i].money+=(status[site.capitalize()][1]) * (0.9)
        print("Your property",site,"has been mortgaged succesfully")

    elif (site.capitalize() in players[i].plist)and (status[site.capitalize()][0]=="hotel"):
        print("You have a hotel on this site. First sell the hotel then mortgage")
        ask=input("Sell the hotel? ")
        if ask in "yesYES":
            players[i].money+=status[site.capitalize()][4] * (0.9)
            status[site.capitalize()][0]="set"

    elif (site.capitalize() in players[i].plist) and (status[site.capitalize()][0]=="set"):
        status[site.capitalize()][0]="mortgaged"
        players[i].money+=(status[site.capitalize()][1]) * (0.9)
        print("Your property",site,"has been mortgaged succesfully")
    
    elif (site.capitalize() in players[i].plist) and (status[site.capitalize()][0]=="mortgaged"):
        print("This property of yours has already been mortgaged")
    
    else:
        print("Mentioned site not in your property\nPlease enter a valid site")

    print("Updated balance : $%.3f"%players[i].money)
    print()
    

###############################################################################

"""If you are in jail you can pay $1.000 to get out or try to roll doubles. """
def jail(i):


    from random import randint
    print("You are in jail currently")
    print("Roll doubles or pay $1.000 to get out")
    ask=input("Enter your choice(\"pay\" or \"roll\" : ")

    if ask.lower() in "roll":
        die1=randint(1,6)
        die2=randint(1,6)
        print("Dice rolled and the numbers are",die1,die2)
        if die1==die2:
            print("You are now released from jail")
            players[i].in_jail=False
            players[i].position+=die1+die2
            action(players[i].position,i)
        else:
            print("Wait for another chance")

    elif ask.lower() in "pay":
        if players[i].money>=0.500:
            players[i].money-=0.500
            print("Roll the dice")
            input()
            die1=randint(1,6)
            die2=randint(1,6)
            print("Dice rolled and the numbers are",die1,die2)
            players[i].position+=die1+die2
            if players[i].position>39:
                players[i].position-=40
                players[i].money+=2.000
                if players[i].position!=0:
                    print("You recieved $2.000 for passing GO!!")
            print("\nDice rolled and numbers are",die1,die2,end="")
            input()
            action(players[i].position,i)
        else:
            print("You do not have enough money to pay!!")
            print("Mortgage your property or roll for the doubles")
            answer=input("Enter your choice : ")
            if answer in "mortgage":
                mortgage(i)
                jail(i)
            elif answer in "roll":
                die1=randint(1,6)
                die2=randint(1,6)
                print("Dice rolled and the numbers are",die1,die2)
                if die1==die2:
                    print("You are now released from jail")
                    players[i].in_jail=False
                    players[i].position+=die1+die2
                    action(players[i].position,i)
                else:
                    print("Wait for another chance")
                        

###############################################################################

"""You can build hotel on a site if you have the complete set of it.
Hotels will increase the amount of rent charged on a site."""
def hotel(i):


    sites=[]
    for site in players[i].plist:
        if status[site][0]=="set":
            sites.append(site)
    if sites:
        print("You can build hotel on ",",".join(sites))
        site=input("Enter the site you wish to build hotel on ")
        if site in sites:
            if players[i].money>=status[site][4]:
                status[site][0]="hotel"
                players[i].money-=status[site][4]
                print("Successfully built a hotel on",site)
            else:
                print("You do not have enough money to build a hotel on this site")
    else:
        print("You can't build hotel on any of your properties")

###############################################################################

"""To unmortgage a site you must pay exaclty the amount as paid while buying the site.
Rent will again be charged."""
def unmortgage(i):

    sites=[]
    for site in players[i].plist:
        if status[site][0]=="mortgaged":
            sites.append(site)
    if sites:
        print("Mortgaged sites: ",",".join(sites))
        a=input("Enter the property you want to unmortgage: ")
        b=a.capitalize()
        if b in sites:
            if players[i].money>=status[b][1]:
                print("Property unmortgaged successfully")
                players[i].money-=status[b][1]
                print("Updated balance : $"+"%.3f"%players[i].money)
                status[b][0]="bought"
            else:
                print("You do not have enough money to unmortgage")
        else:
            print("Entered site not in your properties")
    else:
        print("You have no mortgaged sites.")

###############################################################################

def chance(i):
    from random import randint
    print("Roll the dice again!! press Enter")
    input()
    die1=randint(1,6)
    die2=randint(1,6)
    print("Dice rolled and the numbers obtained are :",die1,die2)
    input()
    total=die1+die2
    if total==2:
        print("Beauty contest won worth $2.500")
        players[i].money+=2.500
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==3:
        print("Profit in business worth $1.500")
        players[i].money+=1.500
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==4:
        print("Fire in factories. Loss of $2.000")
        players[i].money-=2.000
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==5:
        print("Advance to Delhi")
        players[i].position=39
        action(39,i)
    elif total==6:
        print("Income Tax return $1.000")
        players[i].money+=1.00
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==7:
        print("GO TO JAIL!!")
        players[i].position=10
        players[i].in_jail=True
    elif total==8:
        print("Maintenance fee. For each hotel pay $1.000")
        for prop in players[i].plist:
            if status[prop][0]=="hotel":
                players[i].money-=1.000
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==9:
        print("Pay each player $0.500")
        for player in players:
            if player!=players[i]:
                player.money+=0.500
                players[i].money-=0.500
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==10:
        print("Recieve from each player $0.500")
        for player in players:
            if player!=players[i]:
                player.money-=0.500
                players[i].money+=0.500
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==11:
        print("Investment Loss of $2.000")
        players[i].money-=2.00
        print("Updated Balance : $"+"%.3f"%players[i].money)
    elif total==12:
        print("Investment Profit of $3.000")
        players[i].money+=3.00
        print("Updated Balance : $"+"%.3f"%players[i].money)

###############################################################################

def action(k,i):

    print("\nYou have reached",Place[players[i].position])
    if(status[Place[k]][0]=="not bought"):
        if players[i].money>=status[Place[k]][1]:

            confirm=input("This place is unsold yet. Do you wish to buy it?(if you press enter it is \"Yes\")")

            if confirm in "yesYES":

                status[Place[k]][0]="bought"

                players[i].money-=status[Place[k]][1]
                if k==1 or k==2 or k==3:
                    players[i].properties["Brown"][0]+=1
                    players[i].properties["Brown"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==6 or k==7 or k==9:
                    players[i].properties["LightBlue"][0]+=1
                    players[i].properties["LightBlue"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==11 or k==13 or k==14:
                    players[i].properties["Magenta"][0]+=1
                    players[i].properties["Magenta"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==16 or k==17 or k==19:
                    players[i].properties["Orange"][0]+=1
                    players[i].properties["Orange"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==21 or k==23 or k==24:
                    players[i].properties["Red"][0]+=1
                    players[i].properties["Red"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==26 or k==27 or k==29:
                    players[i].properties["Yellow"][0]+=1
                    players[i].properties["Yellow"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==31 or k==32 or k==34:
                    players[i].properties["Green"][0]+=1
                    players[i].properties["Green"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==37 or k==38 or k==39:
                    players[i].properties["Blue"][0]+=1
                    players[i].properties["Blue"].append(Place[k])
                    players[i].plist.append(Place[k])

                elif k==5 or k==12 or k==15 or k==25 or k==28 or k==35:
                    players[i].properties["Services"][0]+=1
                    players[i].properties["Services"].append(Place[k])
                    players[i].plist.append(Place[k])
 
                print("\nYou have successfully bought",Place[k],"for $","%.3f"%status[Place[k]][1])
                print("\nYour updated balance is $"+"%.3f"%players[i].money)
                print("Your properties contain :",",".join(players[i].plist))
            else:
                print("You will pass by")


    elif status[Place[k]][0]=="bought":
        for player in players:
            if player.plist.count(Place[k])==1 and player!=players[i]:
                if k==5 or k==12 or k==15 or k==25 or k==28 or k==35:
                    rent=(status[Place[k]][2])*(player.properties["Services"][0])               #rent = rent on one service * no of services bought
                    print(players[i].name,"should pay $","%.3f"%rent,"as rent to",player.name)
                    player.money+=rent
                    players[i].money-=rent
                    print("Updated balance :\n",player.name,": $"+"%.3f"%player.money,"\n",players[i].name,": $"+"%.3f"%players[i].money)

                else:
                    rent=(status[Place[k]][2])                                                  #rent = rent as specified on the card
                    print(players[i].name,"should pay $",rent,"as rent to",player.name)
                    player.money+=rent
                    players[i].money-=rent
                    print("Updated balance :\n",player.name,": $","%.3f"%player.money,"\n",players[i].name,": $"+"%.3f"%players[i].money)


    
    elif status[Place[k]][0]=="set":
        for player in players:
            if player.plist.count(Place[k])==1 and player!=players[i]:
                print("Player",player.name,"has completed the set of these properties. Rent charged will be twice.")
                rent=(status[Place[k]][2])*2                                                    #rent = twice as specified on the card
                print(players[i].name,"should pay $","%.3f"%rent,"as rent to",player.name)
                player.money+=rent
                players[i].money-=rent
                print("Updated balance :\n",player.name,": $"+"%.3f"%player.money,"\n",players[i].name,": $"+"%.3f"%players[i].money)


    elif status[Place[k]][0]=="hotel":
        for player in players:
            if player.plist.count(Place[k])==1 and player!=players[i]:
                print("Player",player.name,"has a hotel on this property.")
                rent=status[Place[k]][3]                                                        #rent = as specified for a hotel
                print(players[i].name,"should pay","%.3f"%rent,"as rent to",player.name)
                player.money+=rent
                players[i].money-=rent
                print("Updated balance :\n",player.name,": $"+"%.3f"%player.money,"\n",players[i].name,": $"+"%.3f"%players[i].money)


    elif status[Place[k]][0]=="can't buy":
        if Place[k]=="Chance":
            chance(i)
        elif Place[k]=="Income Tax":
            print("You will be charged $2.000 as Income tax")
            players[i].money-=2.000
            print("Updated balance: $"+"%.3f"%players[i].money)
        elif Place[k]=="GO TO JAIL!!":
            print("You have to go to jail")
            players[i].position=10
            players[i].in_jail=True
        elif Place[k]=="FREE PARKING":
            print("You are awarded $3.000 for reaching FREE PARKING")
            players[i].money+=3.000
            print("Updated balance : $"+"%.3f"%players[i].money)
        elif Place[k]=="GO!!":
            print("You recieved twice the passing money for landing on GO!!")
            players[i].money+=4.000
            print("Updated balance : $"+"%.3f"%players[i].money)

    for key in players[i].properties.keys():
        sets=[]
        if players[i].properties[key][0]==3:
            sets.append(key)
            status[players[i].properties[key][1]][0]="set"
            status[players[i].properties[key][2]][0]="set"
            status[players[i].properties[key][3]][0]="set"
        if sets:
            print("You have the set of "+",".join(sets))



###############################################################################

def turn(i):
    from random import randint
    global no_of_players
    

    print("\n\t\t\t\tCHANCE OF PLAYER",players[i].name)
    
    if not players[i].in_jail and not players[i].bankrupt:
        a=input("Press Enter to roll the dice")                                     
        if a.lower().startswith("go"):                                              #cheats for the game XD                         
            b=a.split(" ")                                                          #write go and number of place you want to go eg. "go 1" will take you to bhuvaneshwar
            players[i].position=int(b[1])
            action(players[i].position,i)
        elif a.lower().startswith("money"):
            b=a.split(" ")
            players[i].money+=int(b[1])
        else:
            die1=randint(1,6)
            die2=randint(1,6)
            players[i].position+=(die1+die2)
            if players[i].position>39:
                players[i].position-=40
                players[i].money+=2.000
                if players[i].position!=0:
                    print("You recieved $2.000 for passing GO!!")
            print("\nDice rolled and numbers are",die1,die2,end="")
            input()
            action(players[i].position,i)


    elif players[i].in_jail:
        players[i].position=10
        jail(i)        


    if players[i].money<0:
        print("You are out of money")
        p=0                                 #a count of worth of properties owned by player(i)
        for site in players[i].plist:
            if status[site][0]=="hotel":
                p+=status[site][1]+status[site][4]
            elif status[site][0]=="bought" or status[site][0]=="set":
                p+=status[site][1]
        if players[i].money+(p*0.9)<0:
            print("You do not have enough properties to clear your debt. You are now bankrupt.")
            players[i].bankrupt=True
            for site in players[i].plist:
                status[site][0]="not bought"
            players.remove(players[i])
            no_of_players-=1
            return i-1
        else:
            while players[i].money<0:
                mortgage(i)
                    
    j="o"
    while j not in "4. finish turn":
        print("\n1.Build hotel\n2.Mortgage\n3.Unmortgage\n4.Finish Turn")
        j=input("Enter your choice : ")
        if not j:
            j="o"
            continue
        elif j.lower() in "1. build hotel":
            hotel(i)
        elif j.lower() in "2. mortgage":
            mortgage(i)
        elif j.lower() in "3. unmortgage":
            unmortgage(i)
    return i
        
###############################################################################

def game():
    global no_of_players
    try:
        no_of_players=int(input("Enter the number of players : "))
    except ValueError:
        print("No integer obtained!!retry.")
        game()
    else:
        if no_of_players<=1:
            print("Try again with more players")
            game()
        j=0
        while j<no_of_players:
            n=input("Enter the player name   : ")
            if not n:
                print("Can't leave blank")
            else:
                players.append(Player(n))
                j+=1
        i=0
        while True:
            if len(players)==1:
                print("Winner is :",players[0].name)
                exit()
            i=turn(i)
            i+=1
            if i>=no_of_players:
                i=0

