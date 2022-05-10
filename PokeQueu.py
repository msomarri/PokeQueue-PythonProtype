import pandas as pd

Queue = []
db = pd.read_csv("pokemon_data.csv")
print( " Welcome to PokeQueue.\nStart out by typing in the dex numbers that you want complete today")
print("Hit . to quit ")
done = True

while done:
    if input() == ".":
        done = False
    # otherwise we got our function here . First starting out by add
# TODO
# ADD pk to queue
# rm pk from queue
# search pk

def add( pknum ):
    db["dex number"].where()
print(db)