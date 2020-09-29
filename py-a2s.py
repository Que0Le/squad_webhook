import a2s
import time
import requests #dependency
import json

webhook1 = "https://discordapp.com/api/webhooks/760569574357205062/WxHcBn5TBalcDGg_VCxJDGZnTOZd8z4RbsRtGq120yB7vEcZimoKlYs0d5pt04qZ9nLj"

address = ("194.26.183.101", 27165)
address = ("145.239.131.137", 27165)    # [FR] Teamwork Francophone [P²]

addresses = [
    ("145.239.131.137", 27165),    # [FR] Teamwork Francophone [P²]
    ("194.26.183.101", 27165), #
    ("46.4.96.25", 27165), #	[PA] Project Awesome #1 | New Player Friendly | ENG
    ("46.4.96.25", 27165), #[PA] Project Awesome #2 | New Player Friendly | ENG
    ("88.99.69.190", 27165), #	[FM] Full Metal | New Players Welcome | Teamwork | ENG/EU
    ("194.26.183.84", 27165), #	We ♥ Squad Germany 1
    ("194.26.183.164", 27165), #	★★★ SQUAD EUROPE ★ Mapvote & Stats ★★★ by JoinSqu
    ("194.26.183.179", 27165), #	[BoB] German Band of Bastards Server
    ("194.26.183.83", 27165), #9	We ♥ Squad Germany 2
    ("148.251.6.84", 27165), #		[SR] SMOKING RIFLES - EU SERVER (ENG)	
    ("194.26.183.101", 27165), #	+++ Deutsche Squad Gemeinschaft +++ DSG | GER
    ("194.26.183.5", 27165), #	[SoS] Squad on Sunday | New Player Friendly | ENG
    ("194.26.183.26", 27165), #	[GER/ENG] Publicserver #1 by Squadified | 3.A, SOE, GTK & GaG
    ("194.26.183.165", 27165), #	★★★ SQUADeinander Germany ★ RAAS & INV ★★★ by FC-
    ("116.202.242.48", 27165), #	[MAD] -Make A Difference- [ENG][EU]#1
    ("217.79.189.180", 27165), #	[GER/EN][2]>>BrC<< Born Rebels Squad Server New Players welcome
    ("178.63.42.181", 27165), #	★★ Squad Skandinavia ★★ [EU/NOR] Powered by the Allianc
    ("116.202.242.48", 27165), #	[MAD] -Make A Difference- [ENG][EU]#2
    ("185.248.141.157", 27165), #	✯ ✯ ✯ [TB] Tactical Battalion ✯ ✯ ✯
    ("185.38.149.109", 27165), # 	[TLR] - The Last Rifles Gaming [EU/ENG]
    ("185.38.149.110", 27165), #	RB | Royal Battalion [ENG] discord: https://discord.gg/zhbMJvc
    ("185.38.149.32", 27165), #	Squad+ | Home of Experienced Players | discord.io/SquadPlus
    ("51.38.76.204", 27165), #	[RIP] Rusty In Places UK/EU [ENG] Sq#3 - 24/7 Fallujah Special
    ("185.38.151.16", 27165), #	Fear and Terror #3 | New Player Friendly | EU
    ("213.32.112.184", 27165), #	[RIP] Rusty In Places UK/EU [ENG] Sq#1
    ("185.38.151.31", 27165), #	[IMC] International Militia Corps UK/EU- Heli Focus - https://d
    # ("", 27165), #
    # ("", 27165), #
    # ("", 27165), #
]
print(a2s.info(address))
with open("log.txt", mode="a", encoding="utf-8") as f:
    while(1):
        for a in addresses:
            try:
                print("Pulling " + str(a))
                print(a2s.players(a), file=f)
            except:
                print("An exception occurred") 
        time.sleep(10)


