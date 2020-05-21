#Dictionaries
#customer #name, email, phone
customer={
    "name":"NIYATI",
    "age":20,
    "is_verified":True
}
print(customer)
print(customer["name"])
#print(customer["key_that_does_not_Exist"]) #error #KeyError: 'key_that_does_not_Exist'
#KEYS ARE CASE SENSITIVE
print(customer.get("age")) #print(customer["age"])
print(customer.get("birth_date")) #when there is no such key None is returned by the get()
print(customer.get("birth_date","NOV 29 1999")) #when there is no such key the mentioned value is returned by the get()
print(customer.get("name","NIYATI SINHA"))