#Name:Dylan Muriuki
#Date:12/02/2026
#String formatting

balance="100Kes"
amount_added="50Kes"

cleaned_balance=balance.replace("Kes","")

print("Cleaned balance: ",cleaned_balance)

cleaned_amount_added=amount_added.replace("Kes","")

print("Cleaned amount added:",cleaned_amount_added)

new_balance=int(cleaned_balance)+int(cleaned_amount_added)

print(f"The new balance is:{new_balance}")
#print("The new balance is:",new_balance)
#print(f"The new balance is:",new_balance)

Qn= "CONFIRMED you have received 40KES from Philip"
split=Qn.split( )  
print(f"The amount received is:",split[4] )

clean_balance1=split[4].replace("KES","")
print(clean_balance1)

new_mpesa_balance=int(clean_balance1)+int(new_balance)
end=("KES")
print(new_mpesa_balance)
print(f"{new_mpesa_balance}{end}")

print(f"CONFIRMED you have received 40KES from Philip.Your new mpesa balance is {new_mpesa_balance}{end} ")

