import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def ver_inventario(bot, ctx):
        inventario = json_utils.carregar_inventario()
        usuario = str(ctx.author.id)
        if usuario not in inventario:
                inventario[usuario] = {}
                json_utils.atualizar_inventario(inventario)
        embed = discord.Embed(title="🧳 Inventário 🧳", color=discord.Color.blue())

        if usuario in inventario and len(inventario[usuario]) > 0:    
                for item, descricao in inventario[usuario].items():
                        embed.add_field(name=f"👉 {item}", value=f"📝 Descrição: {descricao}\n\n", inline=False)
        else:
                embed.add_field(
                name="🛑 Sem itens",
                value="Você não tem itens no inventário ainda. 🏚️",
                inline=False
                )
        await ctx.send(embed=embed)

async def adicionar_item(bot, ctx, item, descricao):
        inventario = json_utils.carregar_inventario()

        usuario = str(ctx.author.id)  

        if usuario not in inventario:
                inventario[usuario] = {}

        inventario[usuario][item] = descricao  

        json_utils.atualizar_inventario(inventario)
        await ctx.send(f"Item '{item}' guardado com sucesso!")

async def remover_item(bot, ctx, item):
        inventario = json_utils.carregar_inventario()
        if ctx.author.id not in inventario:
                inventario[ctx.author.id] = []
        if item in inventario[str(ctx.author.id)]:
                inventario[str(ctx.author.id)].pop(item)
                json_utils.atualizar_inventario(inventario)
                await ctx.send(f"{item} removido com sucesso!")