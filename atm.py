#ATM machine in python
def ATM_withdraw():
    name=input("Please enter your name")
    pin_num=5678
    pin_entered=int(input("please enter your pin"))
    Total_account_amount=500000
    
   
    if pin_entered != pin_num:
       
       print("input correct pin")
       
    
    
    if  pin_entered==pin_num:
        amount_entered=int(input("please enter withdraw amount"))
        
        
        balance=Total_account_amount-amount_entered
        if  amount_entered>Total_account_amount:
            print("Please you have insufficient balance")
        

        if  amount_entered<=Total_account_amount:
            print("you have successfully withdrawn",amount_entered,"shillings","and your new balance is",balance,"shillings")
            
    

ATM_withdraw()









    