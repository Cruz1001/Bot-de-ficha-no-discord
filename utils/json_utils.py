import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import json
import random

def carregar_tabela_treino():
    try:
        with open("dados/tabela_treino.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tabela de treino não encontrada")
        return {}
def carregar_atributos():
    try:
        with open("dados/atributos.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Ficha não encontrada")
        return {}

def atualizar_atributos(dados):
    with open("dados/atributos.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_pericias():
    try:
        with open("dados/pericias.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Perícias não encontradas")
        return {}

def atualizar_pericias(dados):   
    with open("dados/pericias.json", 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

def carregar_inventario():
    try:
        with open("dados/inventário.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Inventário não encontrado")
        return {}
def atualizar_inventario(dados):
    with open("dados/inventário.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_magias():
    with open("dados/magias.json", 'r') as f:
        return json.load(f)

def atualizar_magias(dados):
    with open("dados/magias.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_status():
    with open("dados/status.json", 'r') as f:
        return json.load(f)

def atualizar_status(dados):
    with open("dados/status.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_ataques():
    with open("dados/ataques.json", 'r') as f:
        return json.load(f)

def atualizar_ataques(dados):
    with open("dados/ataques.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_pericias_base():
        with open("dados/pericias_base.json", 'r', encoding='utf-8') as f:
            return json.load(f)