import pandas as pd

Queue = []
db = pd.read_csv("pokemon_data.csv")

menu = "1: View All Pokemon\n" \
       "2:Add Pokemon\n" \
       "3:View current Queue\n" \
       "4:Search\n" \
       "5:Quit\n"

# Noramlly this stuff will handle by a db app
def add(pknum):
    search = db.loc[db['dex number'] == int(pknum)]
    if search.empty:
        print("Pokemon Number does not exist")
        return
    Queue.append(search)
def searchPk(pknum):
    print(db.loc[db['dex number']] == int(pknum))
    
def viewPokemon():
    print(db[["dex number","pokemon"]].to_string(index=False))

def viewQueue():
    print("=====================================")
    for items in Queue:
        print(items['pokemon'].to_string())
    print("=====================================")
print(" Welcome to PokeQueue.\nStart out by typing in the dex numbers that you want complete today")
done = True

while done:
    answer = input(menu)
    if answer == "5":
        done = False
    if answer == "1":
        viewPokemon()
    if answer == "2":
        add(input("Enter the dex number\n"))
    if answer == "3":
        viewQueue()
    if answer == "4":
        searchPk(input("Enter the dex number\n"))

# TODO
# ADD pk to queue
# rm pk from queue
# search pk
