# import only that you need 
from prettytable import PrettyTable

# create object using class PrettyTable()
table = PrettyTable()

# access the methods by object "table"
table.add_column("Pokemon",["Pikachu","Miu","Charlizarde"])
table.add_column("Type",["Electric","Mighty","Fire"])
# print table with order manner
print(table)