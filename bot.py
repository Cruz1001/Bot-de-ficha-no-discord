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

def carregar_inventario():
    try:
        with open("inventário.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Inventário não encontrado")
        return {}
def atualizar_inventario(dados):
    with open("inventário.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_poderes_e_habilidades():
    try:
        with open("habilidadesEPoderes.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Poderes e habilidades não encontrados")
        return {}

def atualizar_poderes_e_habilidades(dados):
    with open("habilidadesEPoderes.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_magias():
    with open("magias.json", 'r') as f:
        return json.load(f)

def atualizar_magias(dados):
    with open("magias.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_status():
    with open("status.json", 'r') as f:
        return json.load(f)

def atualizar_status(dados):
    with open("status.json", 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_xpPorNivel():
    with open("xpPorNivel.json", 'r') as f:
        return json.load(f)

def carregar_ataques():
    with open("ataques.json", 'r') as f:
        return json.load(f)

def atualizar_ataques(dados):
    with open("ataques.json", 'w') as f:
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

@bot.command(name="guardar")
@commands.has_permissions(administrator=True) 
async def guardar_item(ctx, item, *, descricao):
    inventario = carregar_inventario()

    bot_id = str(bot.user.id)  

    if bot_id not in inventario:
        inventario[bot_id] = {}

    inventario[bot_id][item] = descricao  

    atualizar_inventario(inventario)
    await ctx.send(f"Item '{item}' guardado com sucesso!")

@bot.command(name='remover')
@commands.has_permissions(administrator=True) 
async def remover_item(ctx, item):
    inventario = carregar_inventario()
    if bot.user.id not in inventario:
        inventario[bot.user.id] = []
    if item in inventario[str(bot.user.id)]:
        inventario[str(bot.user.id)].pop(item)
        atualizar_inventario(inventario)
        await ctx.send(f"{item} removido com sucesso!")

@bot.command(name='npoder')
@commands.has_permissions(administrator=True) 
async def novo_poder(ctx, poder, *, descricao):
    poderes = carregar_poderes_e_habilidades()
    bot_id = str(bot.user.id)
    if bot_id not in poderes:
        poderes[bot_id] = {}
    poderes[bot_id][poder] = descricao
    atualizar_poderes_e_habilidades(poderes)
    await ctx.send(f"Poder {poder} adicionado com sucesso!")

@bot.command(name='rpoder')
@commands.has_permissions(administrator=True) 
async def remover_poder(ctx, poder):
    poderes = carregar_poderes_e_habilidades()
    bot_id = str(bot.user.id)
    if bot_id not in poderes:
        poderes[bot_id] = {}
    if poder in poderes[bot_id]:
        poderes[bot_id].pop(poder)
        atualizar_poderes_e_habilidades(poderes)
        await ctx.send(f"Poder {poder} removido com sucesso!")

@bot.command(name='amagia')
@commands.has_permissions(administrator=True) 
async def aprender_magia(ctx, magia, custo, *, descricao):
    magias = carregar_magias()
    bot_id = str(bot.user.id)
    if bot_id not in magias:
        magias[bot_id] = {}
    magias[bot_id][magia] = {"custo": custo, "descricao": descricao}
    atualizar_magias(magias)
    await ctx.send(f"Magia {magia} adicionada com sucesso!")

@bot.command(name='esquecermagia')
@commands.has_permissions(administrator=True) 
async def esquecer_magia(ctx, magia):
    magias = carregar_magias()
    bot_id = str(bot.user.id)
    if bot_id not in magias:
        magias[bot_id] = {}
    if magia in magias[bot_id]:
        magias[bot_id].pop(magia)
        atualizar_magias(magias)
        await ctx.send(f"Magia {magia} esquecida com sucesso!")

@bot.command(name='inventario')
async def ver_inventario(ctx):
    inventario = carregar_inventario()
    usuario = str(bot.user.id)
    if usuario not in inventario:
        inventario[usuario] = {}
    embed = discord.Embed(title="🧳 Inventário do Borim 🧳", color=discord.Color.blue())

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


@bot.command(name='status')
async def status(ctx):
    status = carregar_status()
    user_id = str(bot.user.id)
    
    vidaMaxima = status[user_id]["pvMax"]
    manaMaxima = status[user_id]["pmMax"]
    vidaAtual = status[user_id]["pv"]
    manaAtual = status[user_id]["pm"]

    if user_id not in status:
        await ctx.send("Você não tem status registrado!")
        return

    
    dados_usuario = status[user_id]
    xp_atual = dados_usuario['xp']
    nivel_atual = dados_usuario['nivel']
    xp_por_nivel = carregar_xpPorNivel()
    xp_por_nivel = {int(k): v for k, v in xp_por_nivel.items()}
    # Determina o XP necessário para o próximo nível
    xp_para_proximo_nivel = xp_por_nivel.get(nivel_atual + 1)
    
    if xp_para_proximo_nivel is None:
        await ctx.send("Você já atingiu o nível máximo!")
        return

    
    progresso = (xp_atual - xp_por_nivel[nivel_atual]) / (xp_para_proximo_nivel - xp_por_nivel[nivel_atual]) * 100
    progresso = round(progresso)

   
    blocos_cheios = int(progresso / 10)
    blocos_vazios = 10 - blocos_cheios
    barra_xp = "🟩" * blocos_cheios + "⬛" * blocos_vazios
     # Barra de Vida
    vida_porcentagem = (vidaAtual / vidaMaxima) * 100
    blocos_cheios_vida = int(vida_porcentagem / 10)
    blocos_vazios_vida = 10 - blocos_cheios_vida
    barra_vida = "🟥" * blocos_cheios_vida + "⬛" * blocos_vazios_vida

    # Barra de Mana
    mana_porcentagem = (manaAtual / manaMaxima) * 100
    blocos_cheios_mana = int(mana_porcentagem / 10)
    blocos_vazios_mana = 10 - blocos_cheios_mana
    barra_mana = "🟦" * blocos_cheios_mana + "⬛" * blocos_vazios_mana

    embed = discord.Embed(title="📊 Estatísticas do Borim 📊", color=discord.Color.blue())
   
    embed.add_field(
    name="❤️ Vida",
    value=f"{barra_vida} {vidaAtual}/{vidaMaxima} HP\n\n"  
    )

    embed.add_field(
    name="🔵 Mana",
    value=f"{barra_mana} {manaAtual}/{manaMaxima} MP\n\n"  
    )

    embed.add_field(
    name="📈 Progresso de XP",
    value=f"{barra_xp} {progresso}%\nXP Atual: {xp_atual}/{xp_para_proximo_nivel}\nPróximo Nível: {nivel_atual + 1}\n\n"  
    )
    await ctx.send(embed=embed)

@bot.command(name='+pv')

async def aumentar_pv(ctx, valor):
    status = carregar_status()
    user_id = str(bot.user.id)
    if user_id not in status:
        status[user_id] = {}
    status[user_id]["pv"] += int(valor)
    atualizar_status(status)
    await ctx.send(f"Vida aumentada em {valor} pontos!")

@bot.command(name='-pv')
async def diminuir_pv(ctx, valor):
    status = carregar_status()
    user_id = str(bot.user.id)
    if user_id not in status:
        status[user_id] = {}
    status[user_id]["pv"] -= int(valor)
    atualizar_status(status)
    await ctx.send(f"Vida diminuída em {valor} pontos!")

@bot.command(name='+pm')
async def aumentar_pm(ctx, valor):
    status = carregar_status()
    user_id = str(bot.user.id)
    if user_id not in status:
        status[user_id] = {}
    status[user_id]["pm"] += int(valor)
    atualizar_status(status)
    await ctx.send(f"Mana aumentada em {valor} pontos!")

@bot.command(name='-pm')
async def diminuir_pm(ctx, valor):
    status = carregar_status()
    user_id = str(bot.user.id)
    if user_id not in status:
        status[user_id] = {}
    status[user_id]["pm"] -= int(valor)
    atualizar_status(status)
    await ctx.send(f"Mana diminuída em {valor} pontos!")

@bot.command(name="+xp")
async def adicionar_xp(ctx, valor):
    status = carregar_status()
    user_id = str(bot.user.id)
    if user_id not in status:
        status[user_id] = {}
    status[user_id]["xp"] += int(valor)
    atualizar_status(status)
    await ctx.send(f"XP aumentado em {valor} pontos!")

@bot.command(name="poderes")

async def ver_poderes(ctx):
    poderes = carregar_poderes_e_habilidades()
    usuario = str(bot.user.id)
    if usuario not in poderes:
        poderes[usuario] = {}
    embed = discord.Embed(title="🔮 Poderes e Habilidades do Borim 🔮", color=discord.Color.blue())

    if usuario in poderes and len(poderes[usuario]) > 0:    
        for poder, descricao in poderes[usuario].items():
            embed.add_field(name=f"👉 {poder}", value=f"📝 Descrição: {descricao}\n\n", inline=False)
    else:
         embed.add_field(
            name="🛑 Sem poderes",
            value="Você não tem poderes e habilidades ainda. 🏚️",
            inline=False
        )
    await ctx.send(embed=embed)

@bot.command(name="magias")
async def ver_magias(ctx):
    magias = carregar_magias()
    usuario = str(bot.user.id)
    if usuario not in magias:
        magias[usuario] = {}
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

@bot.command(name="cataque")
@commands.has_permissions(administrator=True) 
async def criar_ataque(ctx,ataque, modificador, dano, *, descricao):
    ataques = carregar_ataques()
    bot_id = str(bot.user.id)
    if bot_id not in ataques:
        ataques[bot_id] = {}
    ataques[bot_id][ataque] = {"modificador": modificador, "descricao": descricao, "dano": dano}
    atualizar_ataques(ataques)
    await ctx.send(f"Ataque {ataque} adicionado com sucesso!")

@bot.command(name="remataque")
@commands.has_permissions(administrator=True) 
async def remover_ataque(ctx, ataque):
    ataques = carregar_ataques()
    bot_id = str(bot.user.id)
    if bot_id not in ataques:
        ataques[bot_id] = {}
    if ataque in ataques[bot_id]:
        ataques[bot_id].pop(ataque)
        atualizar_ataques(ataques)
        await ctx.send(f"Ataque {ataque} removido com sucesso!")

@bot.command(name="ataques")
async def ver_ataques(ctx):
    ataques = carregar_ataques()
    usuario = str(bot.user.id)
    if usuario not in ataques:
        ataques[usuario] = {}
    embed = discord.Embed(title="⚔️ Ataques do Borim ⚔️", color=discord.Color.blue())

    if usuario in ataques and len(ataques[usuario]) > 0:    
        for ataque, dados in ataques[usuario].items():
            embed.add_field(name=f"👉 {ataque}", value=f"📝 Modificador: {dados['modificador']} \n 📝 Dano: {dados['dano']}\n 📝 Descrição: {dados['descricao']}\\n\n", inline=False)
    else:
         embed.add_field(
            name="🛑 Sem ataques",
            value="Você não tem ataques ainda. 🏚️",
            inline=False
        )
    await ctx.send(embed=embed)

@bot.command(name="rataque")
async def rolar_ataque(ctx, ataque):
    ataques = carregar_ataques()
    dados = ataques[str(bot.user.id)][ataque]
    dado = random.randint(1, 20)
    resultado =  dado + int(dados["modificador"])
    await ctx.send(f"Resultado: {resultado} \nRolagem -> {dado} + Modificador -> {dados['modificador']}")

    
bot.run(TOKEN)