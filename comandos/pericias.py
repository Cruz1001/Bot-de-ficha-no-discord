import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def ver_pericias(bot, ctx):
    pericias = json_utils.carregar_pericias()
    usuario = str(ctx.author.id)
    if usuario not in pericias:
        pericias[usuario] = {}
        json_utils.atualizar_pericias(pericias)

    if usuario in pericias and len(pericias[usuario]) > 0:
        pericias_usuario = list(pericias[usuario].items())
        chunk_size = 25  # máximo de campos por embed
        # Quebra a lista de perícias em pedaços de 25
        for i in range(0, len(pericias_usuario), chunk_size):
            embed = discord.Embed(title="🧪 Perícias 🧪", color=discord.Color.blue())
            chunk = pericias_usuario[i:i + chunk_size]
            for pericia, valor in chunk:
                embed.add_field(name=f"👉 {pericia}", value=f"📝 Valor: {valor}\n\n", inline=False)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="🧪 Perícias 🧪", color=discord.Color.blue())
        embed.add_field(
            name="🛑 Sem perícias",
            value="Você não tem perícias ainda. 🏚️",
            inline=False
        )
        await ctx.send(embed=embed)

async def adicionar_pericia(bot, ctx, pericia, valor):
        pericias = json_utils.carregar_pericias()
        bot_id = str(ctx.author.id)
        if bot_id not in pericias:
                pericias[bot_id] = {}
        pericias[bot_id][pericia] = int(valor)
        json_utils.atualizar_pericias(pericias)
        await ctx.send(f"Perícia {pericia} adicionada com sucesso!")

async def remover_pericia(bot, ctx, pericia):
        pericias = json_utils.carregar_pericias()
        bot_id = str(ctx.author.id)
        if bot_id not in pericias:
                pericias[bot_id] = {}
        if pericia in pericias[bot_id]:
                pericias[bot_id].pop(pericia)
                json_utils.atualizar_pericias(pericias)
                await ctx.send(f"Perícia {pericia} removida com sucesso!")
        else:
                await ctx.send(f"Perícia {pericia} não encontrada.")

async def alterar_pericia(bot, ctx, pericia, novo_valor):
        pericias = json_utils.carregar_pericias()
        bot_id = str(ctx.author.id)
        if bot_id not in pericias:
                pericias[bot_id] = {}
        if pericia in pericias[bot_id]:
                pericias[bot_id][pericia] = int(novo_valor)
                
                json_utils.atualizar_pericias(pericias)
                await ctx.send(f"Perícia {pericia} alterada para {novo_valor} com sucesso!")
        else:
                await ctx.send(f"Perícia {pericia} não encontrada.")