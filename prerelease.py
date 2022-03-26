###TASK 1
import datetime
x = datetime.datetime.now()
TicketType = ["1.one adult","2.one child","3.one senior", "4.family ticket","5.group ticket per person"]
Costfor1day = [20.00,12.00,16.00,60.00,15.00]
ExtraAttraction = ["1.lion feeding","2.penguin feeding","3.evening bbq"]
AttractionCost = [2.50,2.00,5.00]
Costfor2days = [30.00,18.00,24.00,90.00,22.50]
for count in range (5):
    print ("Ticket type =",TicketType[count])
    print ("Cost for a day =",Costfor1day[count],)
    print ("Cost for two days =",Costfor2days[count])
    print ("--------------------")
for count in range (3):
 print ("Extra Attraction", ExtraAttraction[count], "=", AttractionCost[count])
 print ("--------------------")
next
print ("You can book for the following days:")
for count in range (7):
    bookingdays = x.day + count + 1 
    if bookingdays > 31:
        bookingdays = bookingdays - 31
    print (bookingdays)

###TASK 2
tickettype = int(0)
totalcost = int(0)
bookingid = int(0)
addedcost = int(0)
tickettype = int(input("Please input the ticket that you want to buy(1 to 5 or -1 to end booking):")) 
while tickettype > 5 or tickettype < -1 or tickettype == 0:
     tickettype = int(input("Please enter a valid ticket type:"))
notickets = int(input("Please enter the number of tickets you wish to buy:"))
while tickettype == 5 and notickets < 6:
     print ("A group ticket has to be bought for atleast 6 people")
     tickettype = int(input("Please input the ticket that you want to buy(1 to 5):"))
bookingday = int(input("Confirm booking for 1= 1 Day or 2= 2 Days:"))
if bookingday > 2 or bookingday < 1:
     bookingday = int(input("Please enter a valid booking day:"))
if bookingday == 1:
    totalcost = notickets * Costfor1day[tickettype - 1]
elif bookingday == 2:
    totalcost = notickets * Costfor2days[tickettype - 1] 
attractionchoice = int(input("Would you like an extra attraction?1 for yes,2 for no:"))
if attractionchoice == 1:
    extraattraction = int(input("Please input the attraction you want to add (1 to 3):"))
    ch = int(input("Would you like to add another attraction?1 for yes, 2 for no:"))                      
    while ch != 2:
            extraattraction = int(input("Please input the attraction you want to add (1 to 3):"))                        
    if bookingday == 1 and extraattraction == 3:
            print ("BBQ is reserved for 2 day bookings only")
if attractionchoice == 1:
        addedcost = totalcost + AttractionCost[extraattraction - 1]
elif attractionchoice == 2:
        addedcost = totalcost
bookingid = bookingid + 1
print ("Your bookingid: ", bookingid)
print ("Your ticket type =",TicketType[tickettype - 1])
print ("Number of tickets bought =",notickets)
print ("Total cost =", addedcost)

###TASK 3
count = int(0)
altprice = int(0)
altticket = int(0)
adults = int(0)
seniors = int(0)
children = int(0)
if tickettype == 1 or tickettype == 3 and notickets >= 6:
    print ("Please consider getting group tickets for best value")
while (tickettype == 1 or tickettype == 3) > 1 and (tickettype == 2) >= 3:
    if (tickettype == 1) >= 2:
        (tickettype == 1) == (tickettype == 1) - 2
    elif (tickettype == 3) >= 2:
        (tickettype == 3) == (tickettype == 3)-2
    (tickettype == 2) == (tickettype == 2) - 3
    count = count + 1
if (tickettype == 5 and bookingday == 1) or (tickettype == 5 and bookingday == 2):
     while notickets != adults + children + seniors:
          adults = int(input("Please input number of adults"))
          children = int(input("Please input number of children"))
          seniors = int(input("Please input the number of seniors"))
     if adults > 0:
          notickets = adults + seniors + children
     elif seniors > 0:
          notickets = adults + seniors + children
     elif children > 0:
          notickets = adults + seniors + children
     elif adults == 0 and children == 0 and seniors == 0:
          notickets == notickets
     if bookingday == 1:
          altprice = (adults * Costfor1day[0]) + (children * Costfor1day[1]) + (seniors * Costfor1day[2])
     elif bookingday == 2:
          (adults * Costfor2days[0]) + (children * Costfor2days[1]) + (seniors * Costfor2days[2])
     print ("An alternative route would have costed you ",altprice)
     if altprice > addedcost:
          print ("You have the best value")


    


    








              
              
