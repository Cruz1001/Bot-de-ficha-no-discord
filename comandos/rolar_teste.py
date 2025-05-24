import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def rolar_teste(bot, ctx, pericia):
        pericias = json_utils.carregar_pericias()
        dado = random.randint(1, 100)
        valor_pericia = pericias[str(ctx.author.id)][pericia]
        
        if valor_pericia == 0:
            await ctx.send("Essa pericia não existe.")
            return

        classificacao = ""
        if dado >= 96:
                classificacao = "Desastre!"
        elif dado > valor_pericia:
                classificacao = "Falha!"
        elif dado <= valor_pericia and dado > valor_pericia/2:
                classificacao = "Normal"
        elif dado <= valor_pericia/2 and dado > valor_pericia/5:
                classificacao = "Bom!"
        elif dado <= valor_pericia/5:
                classificacao = "Extremo!"
        elif dado == 1:
                classificacao = "Crítico!"
        
        await ctx.send(f"{classificacao}\nRolagem: {dado}\n{pericia}: {valor_pericia}")
        return classificacao