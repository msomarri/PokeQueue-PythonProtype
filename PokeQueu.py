import pandas as pd

Queue = []
db = pd.read_csv("pokemon_data.csv")
print(db)


# Noramlly this stuff will handle by a db app
def add(pknum):
    search = db.loc[db['dex number'] == int(pknum)]
    print(search)
    Queue.append(search)

def remove(pknum):
    

print(" Welcome to PokeQueue.\nStart out by typing in the dex numbers that you want complete today")
print("Hit . to quit ")
done = True

while done:
    answer = input()
    if answer == ".":
        done = False
    # otherwise we got our function here . First starting out by add
    add(answer)
# TODO
# ADD pk to queue
# rm pk from queue
# search pk
