import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def ver_magias(bot, ctx):
        magias = json_utils.carregar_magias()
        usuario = str(ctx.author.id)
        if usuario not in magias:
                magias[usuario] = {}
                json_utils.atualizar_magias(magias)
        embed = discord.Embed(title="🔮 Magias do Borim 🔮", color=discord.Color.blue())

        if usuario in magias and len(magias[usuario]) > 0:    
                for magia, dados in magias[usuario].items():
                        embed.add_field(name=f"👉 {magia}", value=f"📝 Custo: {dados['custo']}\n📝 Descrição: {dados['descricao']}\n\n", inline=False)
        else:
                embed.add_field(
                name="🛑 Sem magias",
                value="Você não tem magias ainda. 🏚️",
                inline=False
                )
                await ctx.send(embed=embed)

async def adicionar_magia(bot, ctx, magia, custo, sanidade, descricao):
        magias = json_utils.carregar_magias()
        bot_id = str(ctx.author.id)
        if bot_id not in magias:
                magias[bot_id] = {}
        magias[bot_id][magia] = {"custo": custo, "Sanidade": sanidade,"descricao": descricao}
        json_utils.atualizar_magias(magias)
        await ctx.send(f"Magia {magia} adicionada com sucesso!")

async def remover_magia(bot, ctx, magia):
        magias = json_utils.carregar_magias()
        bot_id = str(ctx.author.id)
        if bot_id not in magias:
                magias[bot_id] = {}
        if magia in magias[bot_id]:
                magias[bot_id].pop(magia)
                json_utils.atualizar_magias(magias)
                await ctx.send(f"Magia {magia} esquecida com sucesso!")
        else:
                await ctx.send(f"Magia {magia} não encontrada.")
