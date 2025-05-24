import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
import utils.json_utils as json_utils
import comandos.rolar_teste as rolar_teste
import re

async def criarataque(ctx,bot,ataque, pericia, dano, municao, *, descricao):
        ataques = json_utils.carregar_ataques()
        bot_id = str(ctx.author.id)
        if bot_id not in ataques:
                ataques[bot_id] = {}
        ataques[bot_id][ataque] = {"arma":ataque,"pericia": pericia, "descricao": descricao, "dano": dano, "municao": municao, "municao_atual": municao}
        
        json_utils.atualizar_ataques(ataques)
        await ctx.send(f"Ataque {ataque} adicionado com sucesso!")

async def ver_ataques(ctx, bot):
        ataques = json_utils.carregar_ataques()
        usuario = str(ctx.author.id)
        if usuario not in ataques:
                ataques[usuario] = {}
        embed = discord.Embed(title="⚔️ Ataques ⚔️", color=discord.Color.blue())

        if usuario in ataques and len(ataques[usuario]) > 0:    
                for ataque, dados in ataques[usuario].items():
                        embed.add_field(name=f"👉 {ataque}", value=f"📝 Pericia: {dados['pericia']} \n 📝 Dano: {dados['dano']}\n 📝 Descrição: {dados['descricao']}\n 📝Munição: {dados['municao_atual']}/{dados['municao']}\n\n", inline=False)
        else:
                embed.add_field(
                name="🛑 Sem ataques",
                value="Você não tem ataques ainda. 🏚️",
                inline=False
                )
        await ctx.send(embed=embed)

async def remover_ataque(ctx, bot, ataque):
        ataques = json_utils.carregar_ataques()
        bot_id = str(ctx.author.id)
        if bot_id not in ataques:
                ataques[bot_id] = {}
        if ataque in ataques[bot_id]:
                ataques[bot_id].pop(ataque)
                json_utils.atualizar_ataques(ataques)
                await ctx.send(f"Ataque {ataque} removido com sucesso!")
        else:
                await ctx.send(f"Ataque {ataque} não encontrado.")

async def rolar_ataque(ctx, bot, ataque):
        ataques = json_utils.carregar_ataques()
        ataque = ataques[str(ctx.author.id)][ataque]
        resultado = await rolar_teste.rolar_teste(bot, ctx, ataque['pericia'])
        if resultado != "Desastre!" and resultado != "Falha!":
                dano = ataque['dano']
                municao = ataque['municao']
                arma = ataque['arma']
                municao = int(municao)
                municao_atual = ataque['municao_atual']
                municao_atual = int(municao_atual)
                if municao != 0:
                        if municao_atual == 0:
                                await ctx.send(f"Você não tem munição para usar {ataque['arma']}!")
                                return
                        else:
                                municao_atual -= 1
                                ataques[str(ctx.author.id)][arma]['municao_atual'] = municao_atual
                                json_utils.atualizar_ataques(ataques)
                                padrao = r"((\d+)d(\d+)([+-]\d+)?)"
                                match =  re.match(padrao, dano)
                                qntd = int(match.group(2))
                                lados = int(match.group(3))
                                modificador = int(match.group(4)) if match.group(4) else 0
                                
                                resultado = [random.randint(1, lados) for n in range(qntd)]
                                        
                                total = sum(resultado) + modificador
                                if resultado == "Extremo!":
                                        total += qntd*lados + modificador
                                if resultado == "Crítico!":
                                        total += qntd*lados + modificador
                                
                                await ctx.send(f"Você atacou com {ataque['arma']} e causou {total} de dano!")

async def recarregar_ataque(ctx, bot, ataque):
        ataques = json_utils.carregar_ataques()
        bot_id = str(ctx.author.id)
        if bot_id not in ataques:
                ataques[bot_id] = {}
        if ataque in ataques[bot_id]:
                arma = ataques[bot_id][ataque]['arma']
                municao = ataques[bot_id][arma]['municao']
                municao_atual = municao
                ataques[str(ctx.author.id)][arma]['municao_atual'] = municao_atual
                await ctx.send(f"{ataque} recarregado com sucesso!")
                json_utils.atualizar_ataques(ataques)
                
        else:
                await ctx.send(f"Ataque {ataque} não encontrado.")
        
        