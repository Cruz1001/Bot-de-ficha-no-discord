import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random

#Inicialização
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='?', intents=intents)
atributos = "atributos.json"
pericias = "pericias.json"

def carregar_tabela_treino():
    try:
        with open("tabela_treino.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tabela de treino não encontrada")
        return {}
def carregar_atributos():
    try:
        with open(atributos, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Ficha não encontrada")
        return {}

def atualizar_atributos(dados):
    with open(atributos, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_pericias():
    try:
        with open(pericias, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Perícias não encontradas")
        return {}

def atualizar_pericias(dados):   
    with open(pericias, 'w') as f:
        json.dump(dados, f, indent=4)

#comandos

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='criar')
@commands.has_permissions(administrator=True) 
async def criar_ficha(ctx):
    print("criando...")
    bot_id= str(bot.user.id)
    atributos = carregar_atributos()
    atributos[bot_id] = {
        "pv": 16,
        "pm": 7,
        "defesa": 18,
        "tamanho": "médio",
        "nivel": 1,
        "xp": 625,
        "classe": "clérigo",
        "raça": "osteon",
        "força": -1,
        "destreza": 4,
        "constituição": 0,
        "inteligência": 2,
        "sabedoria": 2,
        "carisma": 2,
        "divindade": "Vahzir",
    }
    atualizar_atributos(atributos)
    
    força = atributos[bot_id]["força"]
    destreza = atributos[bot_id]["destreza"]
    constituição = atributos[bot_id]["constituição"]
    inteligência = atributos[bot_id]["inteligência"]
    sabedoria = atributos[bot_id]["sabedoria"]
    carisma = atributos[bot_id]["carisma"]
    nivel = atributos[bot_id]["nivel"]
    tabelaTreino = carregar_tabela_treino()
    treino = int(tabelaTreino[str(nivel)])
    pericias = carregar_pericias()
    pericias[bot_id] = {
        "Acrobacia": destreza + nivel//2 + treino,
        "Adestramento": carisma + nivel//2 + treino,
        "Atletismo": força + nivel//2 + treino,
        "Atuação": carisma + nivel//2 + treino,
        "Cavalgar": destreza + nivel//2 + treino,
        "Conhecimento": inteligência + nivel//2 + treino,
        "Cura": sabedoria + nivel//2 + treino,
        "Diplomacia": carisma + nivel//2 + treino,
        "Enganação": carisma + nivel//2 + treino,
        "Fortitude": constituição + nivel//2 + treino,
        "Furtividade": destreza + nivel//2 + treino,
        "Guerra": inteligência + nivel//2 + treino,
        "Iniciativa": destreza + nivel//2 + treino,
        "Intimidação": carisma + nivel//2 + treino,
        "Intuição": sabedoria + nivel//2 + treino,
        "Investigação": inteligência + nivel//2 + treino,
        "Jogatina": carisma + nivel//2 + treino,
        "Ladinagem": destreza + nivel//2 + treino,
        "Luta": força + nivel//2 + treino,
        "Misticismo": inteligência + nivel//2 + treino,
        "Nobreza": inteligência + nivel//2 + treino,
        "Ofício": inteligência + nivel//2 + treino,
        "Percepção": sabedoria + nivel//2 + treino,
        "Pilotagem": destreza + nivel//2 + treino,
        "Pontaria": destreza + nivel//2 + treino,
        "Reflexos": destreza + nivel//2 + treino,
        "Religião": sabedoria + nivel//2 + treino,
        "Sobrevivência": sabedoria + nivel//2 + treino,
        "Vontade": sabedoria + nivel//2 + treino,
    }
    atualizar_pericias(pericias)
    await ctx.send("Ficha criada com sucesso!")
@bot.command(name='rolar')
async def rolar_pericia(ctx, pericia):
    pericias = carregar_pericias()
    dado = random.randint(1, 20)
    resultado =  dado + pericias[str(bot.user.id)][pericia]
    await ctx.send(f"Resultado: {resultado} \nRolagem -> {dado} + Bônus -> {pericias[str(bot.user.id)][pericia]}")

bot.run(TOKEN)