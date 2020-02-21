import discord
import json

#Discord uses their own version of Markdown. 
    #Any text that is prefaced with 3 ` and followed by 3 ` (backticks) is used as a codeblock
        #Example  ``` This is considered to be a code block ```
    #Any text that is prefaced with 3 > is a block quote and will produce a standout block
        #Example  >>> This is considered to be a block quote
#Discord has an embeded class option for output that has a bit nicer of a format.
#Will potentially look into switching to this in the future.


#JSON file that holds Conditions Data
#Currently just a file, haven't decided if I will house in an actual DB yet.
with open("pathfinder_2e_conditions.json", "r") as read_file:
    data = json.load(read_file)

#Actual Discord Client
client = discord.Client()

#Bot Logs in
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


#Bot is reading messages passed through channel.
@client.event
async def on_message(message):
    #Bot ignores own messages.
    if message.author == client.user:
        return

    #Bot looks for a ! to know it should act.
        #The word following the instantiator indicates the command to run.
        #groups of words after the command are all attempted to be ran with the responses sent back accordingly.
    if message.content.startswith('!'):
        command = message.content.lstrip('!').lower().split(sep=' ')

        if command[0] == 'roll':
            await message.channel.send('Rolling')
            
        elif command[0] == 'init':
            for i in range(len(command)-1):
                await message.channel.send(initiativeTracker(command[i+1]))

        elif command[0] == 'condition':
            for i in range(len(command)-1):
                await message.channel.send(conditionPull(command[i+1]))

        else:
            await message.channel.send('ERROR: Unrecognized command.')



#
def diceRoller(rollCommand):
    return 'ERROR'



#Implements an Initiative System
def initiativeTracker(arg):
    return 'ERROR 404: Initiative Tracker Not Yet Implemented.'



#Pulls the conditions from the above specified JSON file
def conditionPull(suppliedCondition):
    for i in range(len(data)):        
        if data[i]['condition'].lower() == suppliedCondition:
            cond = 'Condition: ' + data[i]['condition'].title() + '\n\n'
                    
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
                    amt += '\n\n' 
                else:        
                    amt = data[i]['amount'].title() + '\n\n'
            except:
                amt = ''

            if type(data[i]['description']) == list:
                desc = 'Description: '
                for pos in range(len(data[i]['description'])):
                    desc += data[i]['description'][pos] + '\n\n'
            else:
                desc = 'Description: ' + data[i]['description']

            return f"``` {cond} {typ} {amt} {desc} ```"
            break

        if i == len(data) - 1:
            return f'```ERROR: Condition {suppliedCondition} was not found. Please try again.```'

client.run('<bot token here>')