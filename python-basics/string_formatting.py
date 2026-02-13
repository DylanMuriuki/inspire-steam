#Name:Dylan Muriuki
#Date:02/12/2026
#String formatting


#Get string length
sentence_1="I watch anime"

string_length=len(sentence_1)

print(f"The length is {string_length}")


#Splitting a string
sentence_2="Mathematics Physics"
split=sentence_2.split(" ")

print(f"The first subject is",split[0])
print(f"The second subject is",split[1])

#Make everything CAPS
mpesa_code="ub12ddsfhg"

capitalised=mpesa_code.upper()

print("New mpesa code",capitalised)


#Make everything to be in lowercase
mpesa_code_2="UB4657DVJ"

lowercased=mpesa_code_2.lower()

print("New mpesa code 2",lowercased)


#Replacing characters in a string

balance="100Kes"
amount_added="50Kes"

cleaned_balance=balance.replace("Kes","")

print("Cleaned balance: ",cleaned_balance)

cleaned_amount_added=amount_added.replace("Kes","")

print("Cleaned amount added:",cleaned_amount_added)


#Dawood's answer

new_balance=int(cleaned_balance)+int(cleaned_amount_added)

print(f"The new balance is:{new_balance}")
#print("The new balance is:",new_balance)
#print(f"The new balance is:",new_balance)


#Assignment1

Qn= "CONFIRMED you have received 40KES from Philip"
split=Qn.split( )  
print(f"The amount received is:",split[4] )

#Assignment2

clean_balance1=split[4].replace("KES","")
print(clean_balance1)

new_mpesa_balance=int(clean_balance1)+int(new_balance)
end=("KES")
print(new_mpesa_balance)
print(f"{new_mpesa_balance}{end}")

print(f"CONFIRMED you have received 40KES from Philip.Your new mpesa balance is {new_mpesa_balance}{end} ")

