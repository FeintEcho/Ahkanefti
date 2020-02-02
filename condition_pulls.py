import json

with open("pathfinder_2e_conditions.json", "r") as read_file:
    data = json.load(read_file)

search = input("Which condition would you like to search for?\n").lower()

while search != "exit":
    for i in range(len(data)):        
        if data[i]['condition'].lower() == search:
            cond = 'Condition: ' + data[i]['condition'].title() + '\n'
            
            try:
                typ = 'Modifier: ' + data[i]['type'].title() + ' '
            except:
                typ = ''

            try:
                if type(data[i]['amount']) == list:
                    amt = ''
                    for pos in range(len(data[i]['amount'])):
                        amt += data[i]['amount'][pos] + ' | '
                    amt = amt[0:len(amt)-3]
                    amt += '\n' 
                else:        
                    amt = data[i]['amount'].title() + '\n'
            except:
                amt = ''

            if type(data[i]['description']) == list:
                desc = 'Description: '
                for pos in range(len(data[i]['description'])):
                    desc += data[i]['description'][pos] + "\n\n"
            else:
                desc = 'Description: ' + data[i]['description']

            print(f'\n{cond}{typ}{amt}{desc}')
            break

    if i == len(data) - 1:
        print("\nNo matching condition. Please try again.")

    search = input("\nWhich condition would you like to search for?\n").lower()



