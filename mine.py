# -*- coding: cp1251 -*-

import discord

from discord.ext import commands

import requests,json

import time # By Titan4IK

import random # By Titan4IK

bot = commands.Bot(command_prefix = ['lx/'])

bot.remove_command('help')

points = 0

@bot.event # By Titan4IK

async def on_ready():

    activity = discord.Game(name="lx/help", type=4)

    await bot.change_presence(status=discord.Status.online, activity=activity)

    print('Бот: {0.user} успешно дрочит!' .format(bot),"[Время:", time.strftime('%H:%M]') )

@bot.command() # By Titan4IK

async def ping(ctx):

    await ctx.send(f"Нет блядь, понг")

    print('[{}] - Написал: lx/ping'.format(ctx.message.author.name), "[Время:", time.strftime('%H:%M:%S]') )

@bot.command() # By Titan4IK

async def help(ctx):

    embed = discord.Embed(color = 282828, title = 'Список кмд:', description = 'lx/stat - Статистика бота\nlx/ping - Да \nlx/say - Повторялка\nlx/weather - Проверить погоду\nlx/mcping - Пинг майнкрафт серверов\nlx/picture - Спиздить картинку с принтскрина\nlx/infoip - Информация о айпишке')

    await ctx.send(embed = embed)

    print('[{}] - Написал: lx/help'.format(ctx.message.author.name), "[Время:", time.strftime('%H:%M:%S]') )

@bot.command()

async def say(ctx, *, bibi: str):

    baba = bibi

    await ctx.send(bibi)

    print('[{}] - Написал: lx/say'.format(ctx.message.author.name), baba, "[Время:", time.strftime('%H:%M:%S]') )

@bot.command(pass_context=True)

async def stat(ctx):

    embed = discord.Embed(color = 282828, title = 'Статистика:', description = "Серверов: " + str(len(bot.guilds)) + "\nПинг: " + str(round(bot.latency * 1000))  )

    embed.set_footer(text="Bot by Titan4IK")

    await ctx.send(embed = embed)

    print('[{}] - Написал: lx/stat'.format(ctx.message.author.name), "[Время:", time.strftime('%H:%M:%S]') )

@bot.command()

async def testovik(ctx):

    await ctx.send('боба')

@bot.command()

async def weather(ctx, *, city: str):

    api_key = "7f1e23163b47cbf21184f339f5c8eaf9&lang=ru"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

        

    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        async with ctx.typing():

            y = x["main"]

            q = x["wind"]

            current_temperature = y["temp"]

            current_temperature_celsiuis = str(round(current_temperature - 273.15))

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            klushe = q["speed"]

            galovka = y["feels_like"]

            z = x["weather"]

            weather_description = z[0]["description"]

            embed = discord.Embed(color = 282828, title = 'Погода в ' + str(city_name), description = 'Температура: ' + str(current_temperature_celsiuis) + '°C' + '\nОщущаеться как: ' + str(round(galovka -273.15)) + '°C' + '\nСкорость ветра: ' + str(round(klushe)) + 'м/с' + '\nВлажность: ' + str(current_humidity) + '%\nОписание: ' + '\n' + str(weather_description))

            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")

            await ctx.send(embed=embed)

            print('[{}] - Написал: lx/weather' .format(ctx.message.author.name), city_name, "[Время:", time.strftime('%H:%M:%S]') )

    else:

        print('error')

@bot.command()

async def mcping(ctx, *, hd: str):

    xd = hd

    jopa = "https://apiv2.spapi.ga/mc/java?"

    compl_url = jopa + "host=" + xd

    response = requests.get(compl_url)

    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 282828, title = 'Ping system', description = 'Айпи ' + json_data['ip'] + '\nПорт: ' + str(json_data['port']) + '\nБуквенный айпи: ' + str(json_data['hostname']) + '\nОнлайн: ' + str(json_data['players']['online']) + '/' + str(json_data['players']['max']) + '\nВерсия: ' + str(json_data['version']) + '\nМотд:\n' + str(json_data['motd']['clean'][0]) )

    embed.set_thumbnail(url="" + json_data['icon'])

    await ctx.send(embed = embed)

    print('[{}] - Написал: lx/mcping' .format(ctx.message.author.name), xd, "[Время:", time.strftime('%H:%M:%S]') )

@bot.command()

async def picture(ctx):

    result_str = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(6)))

    await ctx.send("https://prnt.sc/" + result_str)

    print('[{}] - Написал: lx/picture'.format(ctx.message.author.name), "[Время:", time.strftime('%H:%M:%S]') )

@bot.command()

async def infoip(ctx, *, ip: str):

    hk = ip

    silka = "http://ip-api.com/json/"

    comp_rl = silka + hk + "?lang=ru"

    response = requests.get(comp_rl)

    jso_dat = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 282828, title = 'Информация о: ' + str(jso_dat['query']), description = 'Страна: ' + str(jso_dat['country']) + '\nГород: ' + str(jso_dat['city']))

    embed.set_thumbnail(url="")

    await ctx.send(embed = embed)

    print('[{}] - Написал: lx/infoip' .format(ctx.message.author.name), hk, "[Время:", time.strftime('%H:%M:%S]') )

#При вводе !command происходит нужное вам действие

@bot.command()

@commands.has_permissions(administrator = True) #Тут мы делаем так, что пользоваться командой могут только администраторы

async def command(ctx):

    #Получаем нужный канал по его ID

    channel = bot.get_channel(996839423067029534)

    #Создаем бесконечный цикл в котором каждые 10 секунд в определенный канал посылаем нужное нам сообщение

    while True:

        time.sleep(2)

        neh = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(6)))

        await channel.send("https://prnt.sc/" + neh)

bot.run('Токен нада тут да')
