import discord
from discord.ext import commands
import asyncio


client = commands.Bot(command_prefix=".", intents=discord.Intents.all(),activity=discord.Game('nothing'),help_command=None)


@client.event
async def on_ready():
    print("bot ready")
    await client.change_presence(status=discord.Status.idle)
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
    




class tts_funtion(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.count = 0
        self.ground = ['.0','.1','.2',
                       '.3','.4','.5',
                       '.6','.7','.8']

    async def winner(self,p):
        print(self.ground)
        if (self.ground[0] == self.ground[1] == self.ground[2]) or (self.ground[3] == self.ground[4] == self.ground[5]) or (self.ground[6] == self.ground[7] == self.ground[8]):
            print("w")
            self.ground = ['.0','.1','.2','.3','.4','.5','.6','.7','.8']
            print(self.ground)
            return p
        elif (self.ground[0] == self.ground[4] == self.ground[8]) or (self.ground[2] == self.ground[4] == self.ground[6]):
            print("w")
            self.ground = ['.0','.1','.2','.3','.4','.5','.6','.7','.8']
            print(self.ground)
            return p
        elif (self.ground[0] == self.ground[3] == self.ground[6]) or (self.ground[1] == self.ground[4] == self.ground[7]) or (self.ground[2] == self.ground[5] == self.ground[8]):
            print("w") 
            self.ground = ['.0','.1','.2','.3','.4','.5','.6','.7','.8']  
            print(self.ground)
            return p
        elif (all(isinstance(x, int) for x in self.ground)) == True:
            return -1
        else:
            return 0
        
    async def check(self,f):
        if f % 2 == 0:
            self.count = self.count + 1
            return 1    
        else:
            self.count = self.count + 1
            return 0
        

    async def disable_all_btn(self,interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True 
        await interaction.response.edit_message(view=self)

    async def btn_style(self,Button):
        global current_player,can_be_winner,p,new_content
        if await self.check(self.count) == 1:
            Button.style = discord.ButtonStyle.primary
            Button.label = "x"
            p = 1
            current_player = player2
            can_be_winner = player1
        else:
            Button.style = discord.ButtonStyle.red
            Button.label = "0"
            p = 2
            current_player = player1
            can_be_winner = player2
        new_content = f"🎯  **{player1.name}**  🆚  **{player2.name}**\n\n{current_player.mention}, your move 🎲"
    
    async def win_text(self):
        return f"> 🎉 {can_be_winner.mention} **winner** 🎊"
    
    @discord.ui.button(label="-", custom_id="button-1", style=discord.ButtonStyle.green) 
    async def bt1(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[1-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())
            else:
                print(winner_check)  
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)

    @discord.ui.button(label="-", custom_id="button-2", style=discord.ButtonStyle.green)
    async def bt2(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[2-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        

            else:
                print(winner_check) 
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-3", style=discord.ButtonStyle.green)
    async def bt3(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[3-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
                
            else:
                print(winner_check)
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-4", style=discord.ButtonStyle.green,row=2)
    async def bt4(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[4-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
                
            else:
                print(winner_check)   
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-5", style=discord.ButtonStyle.green,row=2)
    async def bt5(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[5-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
                
            else:
                print(winner_check)  
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-6", style=discord.ButtonStyle.green,row=2)
    async def bt6(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[6-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
                
            else:
                print(winner_check)      
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-7", style=discord.ButtonStyle.green,row=3)
    async def bt7(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[7-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())                        
            else:
                print(winner_check)      
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)
    @discord.ui.button(label="-", custom_id="button-8", style=discord.ButtonStyle.green,row=3)
    async def bt8(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[8-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
                
            else:
                print(winner_check)     
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)    
    @discord.ui.button(label="-", custom_id="button-9", style=discord.ButtonStyle.green,row=3)
    async def bt9(self,interaction:discord.Interaction,Button: discord.ui.Button):
        await self.btn_style(Button)
        if can_be_winner.id == interaction.user.id:
            self.ground[9-1] = p
            winner_check = await self.winner(p)
            if winner_check != 0:
                await self.disable_all_btn(interaction)
                await interaction.followup.send(await self.win_text())        
            else:
                print(winner_check)    
                Button.disabled = True
                await interaction.response.edit_message(view=self,content=new_content)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} not your move",delete_after=2)



@client.command()
async def t(ctx,p1: discord.Member,p2: discord.Member):
    global player1,player2
    player1 = p1
    player2 = p2   
    await ctx.send(f"🎯  **`{p1.name}`**  **VS**  **`{p2.name}`**\n\n{p1.mention}, your move",view=tts_funtion())
    
    









client.run("TOKEN")



