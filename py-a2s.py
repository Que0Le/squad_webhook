import a2s
import time
import requests #dependency
import json
import sqlite3
from datetime import datetime
import requests #dependency
import json
import os
from dotenv import load_dotenv
import json

### Get list of members
members = []
with open("member_list.json", "r", encoding="utf8") as f:
    data=f.read()
    obj = json.loads(data)
    for mem in obj["members"]:
        members.append(mem['nick_name'])
print(members)

### Get discord token:
load_dotenv()
url = os.getenv('DISCORD_WEBHOOK_URL')

addresses = [
    ("145.239.131.137", 27165),    # [FR] Teamwork Francophone [P²]
    ("46.4.96.25", 27165), #	[PA] Project Awesome #1 | New Player Friendly | ENG
    ("88.99.69.190", 27165), #	[FM] Full Metal | New Players Welcome | Teamwork | ENG/EU
    ("194.26.183.84", 27020 ), #	We ♥ Squad Germany 1
    ("194.26.183.83", 27020 ), #	We ♥ Squad Germany 2
    ("194.26.183.164", 27165), #	★★★ SQUAD EUROPE ★ Mapvote & Stats ★★★ by JoinSqu
    ("194.26.183.179", 27165), #	[BoB] German Band of Bastards Server
    ("148.251.6.84", 27165), #		[SR] SMOKING RIFLES - EU SERVER (ENG)	
    ("194.26.183.101", 27165), #	+++ Deutsche Squad Gemeinschaft +++ DSG | GER
    ("194.26.183.5", 27165), #	[SoS] Squad on Sunday | New Player Friendly | ENG
    ("194.26.183.26", 27165), #	[GER/ENG] Publicserver #1 by Squadified | 3.A, SOE, GTK & GaG
    ("194.26.183.165", 27167), #	★★★ SQUADeinander Germany ★ RAAS & INV ★★★ by FC-
    ("116.202.242.48", 27165), #	[MAD] -Make A Difference- [ENG][EU]#1
    ("217.79.189.180", 27165), #	[GER/EN][2]>>BrC<< Born Rebels Squad Server New Players welcome
    ("178.63.42.181", 27022 ), #	★★ Squad Skandinavia ★★ [EU/NOR] Powered by the Allianc
    ("116.202.242.48", 27165), #	[MAD] -Make A Difference- [ENG][EU]#2
    ("185.248.141.157", 27023 ), #	✯ ✯ ✯ [TB] Tactical Battalion ✯ ✯ ✯
    ("185.38.149.109", 27022 ), # 	[TLR] - The Last Rifles Gaming [EU/ENG]
    ("185.38.149.110", 27062 ), #	RB | Royal Battalion [ENG] discord: https://discord.gg/zhbMJvc
    ("185.38.149.32", 27032 ), #	Squad+ | Home of Experienced Players | discord.io/SquadPlus
    ("185.38.151.16", 27165), #	Fear and Terror #3 | New Player Friendly | EU
    ("213.32.112.184", 27165), #	[RIP] Rusty In Places UK/EU [ENG] Sq#1
    ("185.38.151.31", 27042 ), #	[IMC] International Militia Corps UK/EU- Heli Focus - https://d
    # ("", 27165), #
    # ("", 27165), #
]

# print(a2s.info(("185.38.149.109", 27022 )))
# print(a2s.players(("145.239.131.137", 27165)))
# exit()

tablename = "playerserverdata"
con = sqlite3.connect("test.db")
con.execute(f"CREATE TABLE IF NOT EXISTS {tablename}(\
    w_id integer PRIMARY KEY AUTOINCREMENT,\
    server_name TEXT, \
    map_name TEXT, \
    player_count INTEGER, \
    max_players INTEGER, \
    player_name TEXT, \
    score INTEGER,\
    play_duration REAL,\
    query_time timestamp)")

with open("log.txt", mode="a", encoding="utf-8") as f:
    bot = 0
    while(1):
        bot += 1
        ser_infs = []
        for a in addresses:
            try:
                print("Pulling " + str(a))
                #print(a2s.players(a), file=f)
                players = a2s.players(a)
                server_infor = a2s.info(a)#.server_name
                now = datetime.now()
                data = []
                our_players_in_server = []
                for player in players:
                    data.append((None, server_infor.server_name, server_infor.map_name, server_infor.player_count, server_infor.max_players, player.name, player.score, player.duration, now))
                    if player.name in members:
                        our_players_in_server.append((player.name, player.duration))

                query = f"insert into {tablename}\
                    (w_id, server_name, map_name, player_count, max_players, player_name, score, play_duration, query_time) \
                    values (?,?,?,?,?,?,?,?,?)"
                con.executemany(query, data)
                con.commit()

                ser_infs.append((server_infor.server_name, a[0], server_infor.port, server_infor.map_name, server_infor.player_count, server_infor.max_players, our_players_in_server))
                #break
            except:
                print("An exception occurred")
                # raise

            # print(ser_infs)
            # exit()

        # Preparing data to send to Discord
        data = {}
        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data["username"] = "__EU_Bot_" + str(bot%2)

        #leave this out if you dont want an embed
        # data["embeds"] = []
        # embed = {}
        #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
        # embed["title"] = "Server name, IP, Port, Map, Player/Slot, Members in server"

        # Text coloring: https://www.writebots.com/discord-text-formatting/
        desc = "\n\n#######################################################################################\nFetching data from EU server:\n"
        data["content"] = desc
        result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        time.sleep(2)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
        # Sending for each server
        for si in ser_infs:
            desc = ""
            desc += "-----------------------------------------------------------------------------------------------\n"
            desc += f"__**{si[0]}**__ *({si[1]}:{si[2]})* playing **'{si[3]}'** ({si[4]}/{si[5]}): \n"
            for player in si[6]:
                desc += f"                  - ***{player[0]}*** played {player[1]} sec;\t\n"
            data["content"] = desc
            result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print("Payload delivered successfully, code {}.".format(result.status_code))
            time.sleep(5)
        print("Sleeping ...")
        # exit()
        time.sleep(30)


