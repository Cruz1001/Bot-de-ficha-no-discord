import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random
from comandos.criar_ficha import criar_ficha
from comandos.rolar_teste import rolar_teste
import comandos.inventario as inventario
import comandos.magia as magia
import comandos.status as status
import comandos.ataques as ataques
import comandos.pericias as pericias
#Inicialização
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='?', intents=intents)

#comandos
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='criar')
async def criar(ctx):
    await criar_ficha(bot,ctx)
    

@bot.command(name='rolar')
async def rolar(ctx, *,pericia):
    await rolar_teste(bot,ctx,pericia)
    
@bot.command(name='inventario')
async def inventariou(ctx):
    await inventario.ver_inventario(bot, ctx)

@bot.command(name="guardar")
async def guardar(ctx, item, *, descricao):
    await inventario.adicionar_item(bot, ctx, item=item, descricao=descricao)

@bot.command(name='remover')
async def remover(ctx, item):
    await inventario.remover_item(bot, ctx, item=item)

@bot.command(name='addmagia')
async def aprender_magia(ctx, magia, custo, sanidade, *, descricao):
    magia.adicionar_magia(bot, ctx, magia=magia, custo=custo, sanidade=sanidade, descricao=descricao)

@bot.command(name='rmmagia')
async def esquecer_magia(ctx, magia):
    magia.remover_magia(bot, ctx, magia=magia)
    
@bot.command(name="magias")
async def magias(ctx):
    await magia.ver_magias(bot, ctx)

@bot.command(name='status')
async def statuss(ctx):
    await status.ver_status(bot, ctx)
    
@bot.command(name='+pv')
async def aumentarpv(ctx, valor):
    await status.aumentar_pv(bot, ctx, valor=valor)

@bot.command(name='-pv')
async def diminuirpv(ctx, valor):
    await status.diminuir_pv(bot, ctx, valor=valor)   

@bot.command(name='+pm')
async def aumentarpm(ctx, valor):
    await status.aumentar_pm(bot, ctx, valor=valor)

@bot.command(name='-pm')
async def diminuir_pm(ctx, valor):
    await status.diminuir_pm(bot, ctx, valor=valor)

@bot.command(name='+san')
async def aumentarsanidade(ctx, valor):
    await status.aumentar_sanidade(bot, ctx, valor=valor)

@bot.command(name='-san')
async def diminuirsanidade(ctx, valor):
    await status.diminuir_sanidade(bot, ctx, valor=valor)

@bot.command(name="crataque")
async def criar_ataque(ctx,ataque, pericia,dano, municao, *, descricao):
    await ataques.criarataque(ctx, bot, ataque=ataque, pericia=pericia, dano=dano, municao=municao,descricao=descricao)
    

@bot.command(name="rmataque")
async def remover_ataque(ctx, ataque):
    await  ataques.remover_ataque(ctx, bot, ataque)

@bot.command(name="ataques")
async def ver_ataques(ctx):
    await ataques.ver_ataques(ctx, bot)

@bot.command(name="rataque")
async def rolar_ataque(ctx, ataque):
    await ataques.rolar_ataque(ctx, bot, ataque=ataque)

@bot.command(name="recarregar")
async def recarregar(ctx, ataque):
    await ataques.recarregar_ataque(ctx, bot, ataque=ataque)
    
@bot.command(name="pericias")
async def ver_pericias(ctx):
    await pericias.ver_pericias(bot, ctx)

@bot.command(name="adcpericia")
async def adicionarpericia(ctx, *,entrada):
    
    try:
        pericia, valor = entrada.rsplit(" ", 1)
        valor = int(valor)
    except ValueError:
        await ctx.send("Erro: Certifique-se de que o valor da pericia é um número inteiro.")
        return
    await pericias.adicionar_pericia(bot, ctx, pericia=pericia, valor=valor)

@bot.command(name="rmpericia")
async def removerpericia(ctx, pericia):
    await pericias.remover_pericia(bot, ctx, pericia=pericia)

@bot.command(name="altpericia")
async def alterarpericia(ctx, *,entrada):
    try:
        pericia, novo_valor = entrada.rsplit(" ", 1)
        novo_valor = int(novo_valor)
    except ValueError:
        await ctx.send("Erro: Certifique-se de que o valor da pericia é um número inteiro.")
        return
    await pericias.alterar_pericia(bot, ctx, pericia=pericia, novo_valor=novo_valor)
    
@bot.command(name="-sor")
async def diminuirsor(ctx, valor):
    await status.diminuir_sorte(bot, ctx, valor=valor)

@bot.command(name="+sor")
async def aumentarsor(ctx, valor):
    await status.aumentar_sorte(bot, ctx, valor=valor)


@bot.command(name="+sanmax")
async def aumentarsanidademax(ctx, valor):
    await status.aumentar_sanidade_maxima(bot, ctx, valor=valor)

@bot.command(name="-sanmax")
async def diminuirsanidademax(ctx, valor):
    await status.diminuir_sanidade_maxima(bot, ctx, valor=valor)
    
bot.run(TOKEN)