class Player:

   def __init__(self,name,score):
    
       self.name = name;
       self.score =score;
	


kuda = Player("Kudakwashe Shambare",0);

bot = Player("Cloud Bot",0);

import random;

class Round :

    def __init__(self,opponent1,opponent2,roundNum):

        self.winner=start(opponent1,opponent2,roundNum);
        self.opponent1 = opponent1;
        self.opponent2 = opponent2;
        


def start(player1,player2,roundNum):

    print("Round: ", roundNum , "\n");
    choices = ["R","P","S"];

    botChoice = choices[random.randrange(0,2)];
    
    player1Choice = input("Choose from: Rock (R) or Paper (P) or  Sciccors (S) :\n");

    print("Player 1:" ,player1Choice);
    print("Player 2:" ,botChoice);


    try:
        #same choice is a stalemate
        if(player1Choice == botChoice):

            print("Stalemate");
            return None;

        #different choices

        else:
         
            if(botChoice == "R"):
                 
                 #bot wins with rock
                if(player1Choice == "S"):

                    print(player2.name+" won the round"+ str(roundNum));
                    return player2;
                 #bot looses with rock
                else:

                    print(player1.name+" won the round"+ str(roundNum));
                    return player1;

                
         
            if(botChoice == "P" ):

                #BOT wins with paper
                if(player1Choice == "R"):

                    print(player2.name+" won the round"+ str(roundNum));
                    return player2;

                    #bot looses with paper
                else:
                    print(player1.name+" won the round"+ str(roundNum));
                    return player1;

                
            if(botChoice == "S" ):

                #BOT wins with scissors
                if(player1Choice == "P"):

                    print(player2.name+" won the round"+ str(roundNum));
                    return player2;

                    #bot looses with paper
                else:
                    print(player1.name+" won the round"+ str(roundNum));
                    return player1;

                

    except:

       print("Exception");


wins=[]

for i in range(1,4):
    round= Round(kuda,bot,i);

    if(round.winner==kuda):

        kuda.score+=1;

    elif(round.winner == bot):

        bot.score+=1;


print(kuda.score);
print(bot.score);

            

