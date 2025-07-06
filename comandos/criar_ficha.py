import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils

async def criar_ficha(bot, ctx):
        
    conta_id= str(ctx.author.id)
    
    await ctx.send("Qual o nome do seu personagem?")
    nome = (await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)).content
    
    await ctx.send("Qual a idade do seu personagem?")
    idade = (await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)).content
    
    await ctx.send("Qual a ocupação do seu personagem?")
    ocupacao = (await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)).content
    
    await ctx.send("Digite seus atributos na ordem (Separados por espaços): FOR, DES, POD, CON, APA, EDU, TAM, INT, SOR")

    msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    atributos = msg.content.split()

    try:
        forca, destreza, poder, constituicao, aparencia, educacao, tamanho, inteligencia, sorte = map(int, atributos)
    except ValueError:
        await ctx.send("Certifique-se de digitar apenas números separados por espaços.")
        return
    
    atributos = json_utils.carregar_atributos()
    
    
    atributos[conta_id] = {
        "pv": (tamanho + constituicao)//10,
        "pm": poder//5,
        "sanidade": poder,
        "ocupação": ocupacao,
        "força": forca,
        "destreza": destreza,
        "constituição": constituicao,
        "inteligência": inteligencia,
        "poder": poder,
        "aparência": aparencia,
        "tamanho": tamanho,
        "sorte": sorte,
        "educação": educacao,
        "nome": nome,
        "idade": idade
    }
    json_utils.atualizar_atributos(atributos)
    pericias = json_utils.carregar_pericias()
    pericias[conta_id] = json_utils.carregar_pericias_base()
    json_utils.atualizar_pericias(pericias)
    await ctx.send("Quantos pontos de pericia você tem?")
    pontos = (await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)).content
    
    pontos = int(pontos)
    
    if pontos != 0:
        while pontos != 0:
            lista_pericias = "\n".join([f"• {nome}: {valor}" for nome, valor in pericias[conta_id].items()])
            await ctx.send(f"**Perícias disponíveis:**\n{lista_pericias}")
            await ctx.send("Digite o nome da perícia e quanto você quer adicionar à ela (Separados por espaço):")
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            pericia, valor = msg.content.split()
            try:
                valor = int(valor)
            except ValueError:
                await ctx.send("Certifique-se de digitar apenas números separados por espaços.")
                return
            if pericia in pericias[conta_id]:
                if valor > pontos:
                    await ctx.send(f"Você não pode adicionar mais de {pontos} pontos.")
                    continue
                if conta_id not in pericias:
                    pericias[conta_id] = {}
                if pericia not in pericias[conta_id]:
                    pericias[conta_id][pericia] = 1
                pericias[conta_id][pericia] += valor
                pontos -= int(valor)
                await ctx.send(f"Você adicionou {valor} pontos à perícia {pericia}. Você ainda tem {pontos} pontos.")
            else:
                await ctx.send(f"A perícia {pericia} não existe.")
    
    
    json_utils.atualizar_pericias(pericias)
    await ctx.send("Ficha criada com sucesso!")