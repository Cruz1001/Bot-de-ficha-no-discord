import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def ver_status(bot, ctx):
    status = json_utils.carregar_status()
    atributos = json_utils.carregar_atributos()
    user_id = str(ctx.author.id)

    if user_id not in atributos:
        await ctx.send("⚠️ Seus atributos não foram definidos ainda. Use um comando para criar sua ficha.")
        return

    # Obtém os atributos máximos do JSON de atributos
    vidaMaxima = status[user_id].get("pv", 1)
    manaMaxima = status[user_id].get("pm", 1)
    sanidadeMaxima = status[user_id].get("sanidade", 1)
    print(sanidadeMaxima)
    sorteMaxima = status[user_id].get("sorte", 100)

    # Se o status ainda não existir, inicializa com os valores máximos
    if user_id not in status:
        status[user_id] = {
                "pv": vidaMaxima,
                "pm": manaMaxima,
                "sanidade": sanidadeMaxima,
                "sorte": sorteMaxima, 
            "pvAtual": vidaMaxima,
            "pmAtual": manaMaxima,
            "sanidadeAtual": sanidadeMaxima,
            "sorteAtual": sorteMaxima
        }
        json_utils.atualizar_status(status)

    # Obtém os valores atuais do JSON de status
    vidaAtual = status[user_id].get("pvAtual", vidaMaxima)
    manaAtual = status[user_id].get("pmAtual", manaMaxima)
    
    sanidadeAtual = status[user_id].get("sanidadeAtual", sanidadeMaxima)
    print(sanidadeAtual)
    sorteAtual = status[user_id].get("sorteAtual", sorteMaxima)

    # Função para gerar barras de status
    def barra(atual, maximo, emoji):
        porcentagem = (atual / maximo) * 100 if maximo else 0
        blocos_cheios = int(porcentagem / 10)
        blocos_vazios = 10 - blocos_cheios
        return emoji * blocos_cheios + "⬛" * blocos_vazios

    # Gera cada barra
    barra_vida = barra(vidaAtual, vidaMaxima, "🟥")
    barra_mana = barra(manaAtual, manaMaxima, "🟪")
    barra_sanidade = barra(sanidadeAtual, sanidadeMaxima, "🟦")
    barra_sorte = barra(sorteAtual, sorteMaxima, "🟩")

    # Embed com os dados
    embed = discord.Embed(title="📊 Estatísticas 📊", color=discord.Color.blue())

    embed.add_field(name="❤️ Vida", value=f"{barra_vida} {vidaAtual}/{vidaMaxima} HP\n\n")
    embed.add_field(name="🟣 Pontos de Magia", value=f"{barra_mana} {manaAtual}/{manaMaxima} MP\n\n")

    insanidade_msg = ""
    if sanidadeAtual < (sanidadeMaxima * 0.8):
        insanidade_msg = "\n🧠 *Insanidade indefinida!*"
    embed.add_field(name="🔵 Sanidade", value=f"{barra_sanidade} {sanidadeAtual}/{sanidadeMaxima} Sanidade\n\n" + insanidade_msg)

    embed.add_field(name="🟢 Sorte", value=f"{barra_sorte} {sorteAtual}/{sorteMaxima} Sorte\n\n")

    await ctx.send(embed=embed)

async def aumentar_pv(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["pvAtual"] += int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Vida aumentada em {valor} pontos!")

async def diminuir_pv(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["pvAtual"] -= int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Vida diminuída em {valor} pontos!")

async def aumentar_pm(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["pmAtual"] += int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Pontos de magia aumentados em {valor} pontos!")

async def diminuir_pm(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["pmAtual"] -= int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Pontos de magia diminuídos em {valor} pontos!")

async def aumentar_sanidade(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sanidadeAtual"] += int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sanidade aumentada em {valor} pontos!")

async def diminuir_sanidade(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sanidadeAtual"] -= int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sanidade diminuída em {valor} pontos!")

async def aumentar_sorte(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sorteAtual"] += int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sorte aumentada em {valor} pontos!")

async def diminuir_sorte(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sorteAtual"] -= int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sorte diminuída em {valor} pontos!")

async def aumentar_sanidade_maxima(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sanidade"] += int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sanidade máxima aumentada em {valor} pontos!")

async def diminuir_sanidade_maxima(bot, ctx, valor):
        status = json_utils.carregar_status()
        user_id = str(ctx.author.id)
        if user_id not in status:
                status[user_id] = {}
        status[user_id]["sanidade"] -= int(valor)
        json_utils.atualizar_status(status)
        await ctx.send(f"Sanidade máxima diminuída em {valor} pontos!")
        
