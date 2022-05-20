import pandas as pd
pd.set_option('display.max_colwidth', None)
Queue = []
db = pd.read_csv("pokemon_data.csv")
menu = "1:View All Pokemon\n" \
       "2:Add Pokemon\n" \
       "3:View current Queue\n" \
       "4:Search\n" \
       "5.Start Queue\n" \
       "6:Quit\n"

# Noramlly this stuff will handle by a db app
def add(pknum):
    search = db.loc[db['dex number'] == int(pknum)]
    if search.empty:
        print("Pokemon Number does not exist")
        return
    Queue.append(search)
def searchPk(pknum):
    print(db.loc[db['dex number'] == int(pknum)])
    
def viewPokemon():
    print(db[["dex number","pokemon"]].to_string(index=False))

def viewQueue():
    print("=====================================")
    print("Number\tPokemon")
    for items in Queue:
        print(items[["dex number",'pokemon']].to_string(index=False,header=False))
    print("=====================================")

def startQueue():

    for pokemon in Queue:
        loop = False;
        while not loop:
            print("===============================")
            print(pokemon[["dex number","pokemon"]].to_string(index=False))
            print(pokemon["Location"].to_string(index=False))
            print("===============================")
            response = input("Hit Any key to go the next pokemon ")
            if response == "":
                loop = True

print(" Welcome to PokeQueue.\nStart out by typing in the dex numbers that you want complete today")
done = True
# Here is where the menu lives
while done:
    answer = input(menu)
    if answer == "6":
        done = False
    if answer == "1":
        viewPokemon()
    if answer == "2":
        add(input("Enter the dex number\n"))
    if answer == "3":
        viewQueue()
    if answer == "4":
        searchPk(input("Enter the dex number\n"))
    if answer == "5":
        startQueue()


# TODO
# ADD pk to queue
# rm pk from queue
# search pk
