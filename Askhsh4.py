import random
play_1=0
play_2=0
drw_=0

for s in range(0,100):
 xartia = []
 figures = ["J", "Q", "K"]
 xarti = [i for i in range(1, 11)] + figures
 color = ["H", "S", "C", "D"]

 for i in xarti:
     for j in color:
         xartia.append([i,j])
 random.shuffle(xartia)
 player1=[]
 sum1=0

 while sum1<16:
     sum1=0
     player1.append(xartia.pop())
     # print (player1)
     for card in player1:
         if card[0] in figures:
             sum1=sum1+10
         else:
             sum1=sum1+card[0]
     print(sum1)
 if sum1>21:
     print("P2 wins!")
     play_2+=1
 else:
     '''
     sxolia pollwn
     grammwn
     '''

     print("P2 joins the game") #let me add one more player
     player2=[]
     sum2=0
     while sum2<16:
         sum2=0
         player2.append(xartia.pop())
         # print (player2)
         for card in player2:
             if card[0] in figures:
                 sum2=sum2+10
             else:
                 sum2=sum2+card[0]
         print(sum2)
     if sum2>21:
         sum2=0
     if sum1>sum2:
         print("P1 wins!")
         play_1+=1
     elif sum2>sum1:
         print("P2 wins!")
         play_2+=1
     else:
         print("draw!")
         drw_+=1


print("*********************************************************************************************")

play1=0
play2=0
drw=0

for s in range(0,100):
 xart = []
 xart2=[]
 xart3=[]
 figures = ["J", "Q", "K"]
 ola = [i for i in range(1, 11)] + figures
 xarti2=[i for i in range(1, 9)]
 color = ["H", "S", "C", "D"]

#ftiaxnei mia stiva apo 10aria kai figoures
 for j in color:
    xart.append([10, j])

 for i in figures:
     for j in color:
         xart.append([i,j])

#ftiaxnei mia stiva pou ta exei ola
 for i in ola:
     for j in color:
         xart2.append([i,j])

#ftiaxnei mia stiva apo ta noumera 1 eos 9
 for i in xarti2:
     for j in color:
         xart3.append([i, j])

 random.shuffle(xart)
 random.shuffle(xart2)
 random.shuffle(xart3)
 player1=[]
 sum1=0
 k=0
 while sum1<16:
     sum1=0
     if k==0:
         #dinei panta thn proth fora 10 h figoura
      d=xart.pop()
      player1.append(d)
         #kai auto pou evgale apo thn stiva ton 10ariwn kai ton figourwn to afairei kai apo ti stiva pou ta exei ola
      xart2.remove(d)
     else:
         #edo pairnei opoio filo na ne ektos apo auto pou travixthke proto
      l=xart2.pop()
      player1.append(l)
      if l in xart:
          xart.remove(l)
      elif l in xart3:
          xart3.remove(l)



     # print (player1)
     for card in player1:
         if card[0] in figures:
             sum1=sum1+10
         else:
             sum1=sum1+card[0]
     print(sum1)
     k+=1
 if sum1>21:
     print("P2 wins!")
     play2+=1
 else:
     '''
     sxolia pollwn
     grammwn
     '''

     print("P2 joins the game") #let me add one more player
     player2=[]
     sum2=0
     x=0
     while sum2<16:
         sum2=0
         if x==0:
          j=xart3.pop()
          player2.append(j)
          xart2.remove(j)
         else:
            p=xart2.pop()
            player2.append(p)
            if p in xart:
                xart.remove(p)
            elif p in xart3:
                xart3.remove(p)


         # print (player2)
         for card in player2:
             if card[0] in figures:
                 sum2=sum2+10
             else:
                 sum2=sum2+card[0]
         print(sum2)
         x+=1
     if sum2>21:
         sum2=0
     if sum1>sum2:
         print("P1 wins!")
         play1+=1
     elif sum2>sum1:
         print("P2 wins!")
         play2+=1
     else:
         print("draw!")
         drw+=1


print("Player1 won ",play_1," times")
print("Player2 won ",play_2," times")
print("Draw ",drw_," times")

print("Ta apotelesmata me to peiragma einai :")
print("Player1 won ",play1," times")
print("Player2 won ",play2," times")
print("Draw ",drw," times")