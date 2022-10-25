import random, requests, string
checker = True

if checker == True:
    while True:
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if response.status_code == 200:
            print(f"Valid Nitro Code > discord.gift/{code} Made By Noobie#4334")
        else:
            print(f"Invalid Nitro Code > discord.gift/{code} Made By Noobie#4334")
elif checker == False:
    while True:     
            code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            print(f"Nitro Code > discord.gift/{code} Made By Noobie#4334")
