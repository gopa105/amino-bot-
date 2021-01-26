import amino
email=input("Email:")
password=input("Password:")
client = amino.Client() 
client.login(email=email, password=password)
