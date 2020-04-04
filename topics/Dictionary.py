# A Dictionary is a type of array that contains two parts:
#    key: Unique way to identify the member of the Dictionary and must be unique
#    value: A value that corresponds to the key valu

# My simple Dictionary
ChicagoSports = {
    "baseball": "Cubs",
    "football": "Bears",
    "basketball": "Bulls"
}

# Create a simple Dictionary using the dict() Constructor
my_name = dict(first_name = "Craig",last_name="Bell")

# Print all tuples int the dictionaries
print("Print the tuples of the Dictionaries:")
print(my_name)
print(ChicagoSports)

# Add line to script
print("\n")

# Get the value of a tuple by passing a key
print("Get one tuple by it's key:")
my_basketball_team = ChicagoSports["basketball"]
print (my_basketball_team)

# Add line to script
print("\n")

# Use the get() method to retreive the value of a tuple by passing the key
print("Retrieve and print one tuple using get() method:")
not_my_baseball_team = ChicagoSports.get("baseball")
print (not_my_baseball_team)

# Add line to script
print("\n")

# Change the value of a tuple
print("Change a value for a tuple:")
ChicagoSports["baseball"] = "White Sox"
my_baseball_team = ChicagoSports.get("baseball")
print (my_baseball_team)

# Add line to script
print("\n")

# Add a tuple to the Dictionary using the update() method
print("Add a tuple to the Dictionary using the update() method:")
ChicagoSports.update({"soccer": "Chicago Fire FC"})
print(ChicagoSports)

# Add line to script
print("\n")

# For loop to print keys for the Dictionary
print("Use a loop to print the keys for the Dictionary:")
for team in ChicagoSports:
    print(team, end=" ")

# Add line to script
print("\n")

# For loop to print values for the Dictionary
print("Use a loop to print the values for the Dictionary:")
for team in ChicagoSports:
    print(ChicagoSports[team], end=" ")

# Add line to script
print("\n")

# Use values() method to loop through Dictionary
print("Use a loop to print the values for the Dictionary using the values() method:")
for team in ChicagoSports.values():
    print(team, end=" ")

# Add line to script
print("\n")

# Use values() method to loop through Dictionary
print("Use a loop to print the keys for the Dictionary using the keys() method:")
for team in ChicagoSports.keys():
    print(team, end=" ")

# Add line to script
print("\n")

# Look through and print the tuple's keys and values using "items" method
print("Use a loop to print the keys and values for the Dictionary using the items() method:")
for team, team_name in ChicagoSports.items():
    print(team, team_name, end=" ")

# Add line to script
print("\n")

# Use "in" to locates a tuple in the Dictionary
print("Find a tuple in the Dictionary using a key:")
if "baseball" in ChicagoSports:
    print("The White Sox are my favorite baseball team")
  
# Add line to script
print("\n")
  
# Get the length for a Dictionary using the len() method
print("Get and print the length of the Dictionary:")
my_dict_len = len(ChicagoSports)
print (my_dict_len)

# Add line to script
print("\n")

# Copy a Dictionary to another Dictionary using the copy() method
print("Copy a Dictionary using the copy() method:")
NewChicagoSports = ChicagoSports.copy()
print(NewChicagoSports)

# Add line to script
print("\n")

# Copy a Dictionary to another Dictionary using the dict() constructor
print("Copy a Dictionary using the dict() constructor:")
NewChicagoSports2 = dict(ChicagoSports)
print(NewChicagoSports2)

# Add line to script
print("\n")

# Add a tuple to the Dictionarry
print("Add a tuple to the Dictionary:")
ChicagoSports["hockey"] = "Blackhawks"
print(ChicagoSports)

# Add line to script
print("\n")

# The pop() method removes a tuple from the Dictionary
print("Remove a tuple from the Dictionary using the pop() method:")
ChicagoSports.pop("hockey")
print(ChicagoSports)

# Add line to script
print("\n")

# The del command can also be used to remove a tuple from the Dictionary
print("Remove a tuple from the Dictionary using the del command:")
del ChicagoSports["basketball"]
print(ChicagoSports)

# Add line to script
print("\n")

# Use the setdefault() method to return the key for a tuple in the Dictionary
print("Use the setdefault() method to return a key for a tuple in the Dictionary:")
my_baseball_team = ChicagoSports.setdefault("baseball","White Sox")
print(my_baseball_team)
print(ChicagoSports)

# Add line to script
print("\n")

# Use the setdefault() method to add a tuple to the Dictionarythat does not exist
print("Use the setdefault() method to add a tuple to the Dictionary that does not already exist:")
my_basketball_team = ChicagoSports.setdefault("basketball","Bulls")
print(my_basketball_team)
print(ChicagoSports)

# Add line to script
print("\n")

# Someone asked if I could embed a List in a Dictionary
# Here is an example
print("A Python List created as values for a Dictionary:")
ChicagoBearsList= ["Bulls","White Sox","Bears","Blackhawks"]
ChicagoSportsDict = dict(allsports = ChicagoBearsList)
print(ChicagoSportsDict.keys())
for teams in ChicagoSportsDict.values():
    my_team_list = list(teams)
    for my_team in my_team_list:
        print (my_team, end= ' ')

# Add line to script
print("\n")

# Clear (remove all tuples) from a Dictionary using the clear() method
print("Remove all tuples from the Dictionary using the clear() method:")
ChicagoSports.clear()
print(ChicagoSports)


    


