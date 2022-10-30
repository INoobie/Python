import random, string, threading, requests

def main():
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if response.status_code == 200:
        print(f"discord.gift/{code}")

while True:
    threads = []

    for i in range(50):
        t = threading.Thread(target=main)
        t.daemon = True
        threads.append(t)

    for i in range(50):
        threads[i].start()

    for i in range(50):
        threads[i].join()
