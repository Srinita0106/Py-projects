# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import webbrowser
countries=['Australia','USA','France','South Africa','UK']
mydict={'Australia':['Sydney','Canberra','Melbourne','Brisbane','Albany'],
        'USA':['New York','California','San Francisco','Chicago','Las Vegas'],
        'France':['Paris','Cannes','Marseille','Lyon'],
        'South Africa':['Cape Town','Bloemfontein','Durban','East London','Johannesburg'],
        'UK':['London','Brighton','Edinburgh','Belfast','York']}
print("                                   *************************")
print("                                           WELCOME TO ")
print("                                         HOLIDAY PLANET ")
print("                                   *************************\n")
name=input('Hello there! What is your name? ')
print('\nOh hey,',name,'.','Nice to meet you!')
email=input('Please enter your e-mail id: ')
print("Let's get started, shall we?")
print('\nOur services extend to various countries. Right now, we can offer you a quality time in one of the following places:\n')
i=1
for a in mydict.keys():
    print(str(i)+'.'+str(a))
    i+=1
print()
country=int(input('So, which country are you interested in? Type the index number: '))
mycountry=countries[country-1]
print()
print(mycountry,'is an amazing choice!','In',mycountry,',','we offer a tour in one of the following places:\n')
i=1
for b in mydict[mycountry]:
    print(str(i)+'.'+str(b))
    i+=1
print()
city=int(input('Which city do you plan to go to? Type the index number: '))
mycity=mydict[mycountry][city-1]
print()
print(mycity,'is an awesome choice!')
print('Do you want to know more about',mycity,'?')
data=input('(Y/N): ')
if data=='y' or data=='Y':
    url_mycity="https://en.wikipedia.org/wiki/"+mycity
    webbrowser.open_new_tab(url_mycity)
else:
    print('It seems like you already know about',mycity+'. Awesome!')
print("How many people are you taking with you?")
child=int(input("Enter numeber of children:"))
adult=int(input("Enter number of adults(includes you):"))
ch=print("so",child ,"children and",adult,"adult are travelling including you right?")
if adult==1 and child==0:
    print("\nSo, it's a solo trip. We'll make sure that you have a wonderful time!")
else:
    print("We'll make sure that you have a wonderful time!")
print('\nWhen would you like to travel?')
while True:
    date=input('Enter the date (dd/mm/yyyy): ')
    dd,mm,yy=date.split('/')
    d,m,y=int(dd),int(mm),int(yy)
    if d>31 or m>12 or y<2020:
       print('The date you have entered is invalid! Please enter it again.')
    else:
       print("Now, the next step.")
       break
print('\nWhen will you check out of the hotel?')
while True:
    cdate=input('Enter the date (dd/mm/yyyy): ')
    dd,mm,yy=cdate.split('/')
    ddd,mmm,yyy=int(dd),int(mm),int(yy)
    if ddd>31 or mmm>12 or yyy<2020:
       print('The date you have entered is invalid! Please enter it again.')
    else:
       print("Great, let's move on!")
       break
days=int(input('So, '+name+'. How many days will you be staying? '))
packs=['Silver Package','Gold Package','Platinum Package']
print('\nThe following are the available packages. \n')
i=1
for e in packs:
    print(str(i)+'.'+packs[i-1])
    i+=1
silver=['3 star hotel','Complementary breakfast','Luxury rooms','Free Wi-Fi','Rs.4000 per day']
gold=['4 star hotel','Complementary breakfast','Free spa coupon','Luxury rooms','Free Wi-Fi','Rs.7000 per day']
platinum=['5 star hotel (Individual villa available)','Complementary breakfast','Exclusive tour of the city','Luxury rooms','Free Wi-Fi','Rs.9000 per day']
def pack():
 pack=int(input('Which package would you like to view? Type the index number: '))
 print()
 i=1
 if pack==1:
     for f in silver:
         print(str(i)+'.'+silver[i-1])
         i+=1
 elif pack==2:
     for g in gold:
         print(str(i)+'.'+gold[i-1])
         i+=1
 else: 
     for h in platinum:
         print(str(i)+'.'+platinum[i-1])
         i+=1
pack()
while True:
    aa=input('Would you like to view another package? (Y/N): ')
    if aa=='y' or aa=='Y':
         pack()
    else:
         cc=int(input('Enter the index number of the package you chose: '))
         bb=input('Would you like to confirm this package? (Y/N): ')
         if bb=='y' or bb=='Y':
             print("Great! Let's move on.")
             break
         else:
             pack()
room=int(input('How many rooms would you like to book? '))
print("\nLet's book your flight tickets, shall we?")
def book_flight():
    print("\nWhich of the following sites do you prefer?")
    site=int(input("1.Clear Trip\n2.Goibibo\n3.Yatra.com\nType the index number: ")) 
    if(site==1):
        url="https://www.cleartrip.com/"
    elif(site==2):
        url= "https://www.goibibo.com/"
    else:
        url="https://www.yatra.com/flights"
    webbrowser.open_new_tab(url)
    book=input("\nDid you find your desired seat? (Y/N): ") 
    if (book=='n' or book=='N'):            
          book_flight()
    else:             
          print("\nOkay, that's great!")
book_flight() 
print('More details will be provided to you via e-mail.')
print("\nPlease confirm your booking -")
print(mycity,',',mycountry)
ch=print("so",child ,"children and",adult,"adult are travelling including you right?")
print('You will leave on',date,'to',mycity,'.')
print('You will check out on',cdate,'from the hotel.')
print('You have choosen the',packs[cc-1],'.')   
print('\n********')
print('PAYMENT')
print('********')
tot=child+adult
if pack==1:
    cost=(tot)*days*4000
elif pack==2:
    cost=(tot)*days*7000
else:
    cost=(tot)*days*9000
print('The cost is',cost,'rupees.')
tax=15/100*cost
print('Your final bill (inclusive of all taxes) is',tax+cost,'rupees.')
pay=input('How would you like to pay? (Cash/Card): ')
if pay=='card' or pay=='Card':
    cname=input("Enter card holder's name: ")
    cno=int(input('Enter card number: '))
    cvv=int(input('Enter CVV: '))
    print('Your payment has been received.')
else:
    print('Your mode of payment is accepted. More details will be provided to you via e-mail.')
print('\nWe genuinely hope that you have an amazing trip and return home with plenty of unforgettable memories. We hope that you will think of us the next time you wish to travel. See you later,',name,'!')

   




    


       
       
 
    
 

        
        








        




















    
    
        























































































































































































































































































































































































































































































































    



    

      
      

































































































































































































































































































































  