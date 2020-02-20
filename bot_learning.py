import discord
import json

with open("pathfinder_2e_conditions.json", "r") as read_file:
    data = json.load(read_file)

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        command = message.content.lstrip('!').lower().split(sep=' ')

        if command[0] == 'roll':
            await message.channel.send('Rolling')
            
        elif command[0] == 'init':
            await message.channel.send('Starting Initiative')

        elif command[0] == 'condition':
            for i in range(len(data)):        
                if data[i]['condition'].lower() == command[1]:
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

                    await message.channel.send(cond + typ + amt + desc)
                    break

                    if i == len(data) - 1:
                        await message.channel.send("No matching condition. Please try again.")

        else:
            await message.channel.send('ERROR: Unrecognized command.')

client.run('<bot token here>')