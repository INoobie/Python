import random, time
def gen():
    print('Card Numbers: ',random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),'-',random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),'-',random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9), ' Date: ',  random.randint(10,12), '/', random.randint(24,26), ' CVC: ', random.randint(1,9),random.randint(1,9),random.randint(1,9))
    time.sleep(0.3)

while True:
    gen()
