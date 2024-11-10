from datetime import datetime
owca = {"wiek" :17,
        "voucher daja": ["radwan","maja","filip","janek","kuba","mateusz","iwo","pola"],
        "branzoletke zrobiona przez": "Polka i Iwo (PIwo)",
        "dzien urodzin": 10,
        "zyczenia": "w imieniu wymienionych w liscie, z okazji urodzin, chcialbym zyczyc ci wszystkiego co najlepsze, czyli tego abys byla szczesliwa i miala czas na to na co masz ochote oraz oczywiscie pieniadze..."
}
        
dzisiaj = datetime.now()

if dzisiaj.day == owca["dzien urodzin"] and dzisiaj.month == 11:
    print(owca["zyczenia"],"prezent od:",owca["voucher daja"])
    owca["wiek"] = 18
else:
    print("mloda :p")
print("chujowo wyszlo z tym serduszkiem")
print("____*##########",
"__*##############",
"__################",
"_##################_________*####*",
"__##################_____*##########",
"__##################___*#############",
"___#################*_###############*",
"____#################################*",
"______###############################",
"_______#############################",
"________=##########################",
"__________########################",
"___________*#####################",
"____________*##################",
"_____________*###############",
"_______________#############",
"________________##########",
"________________=#######*",
"_________________######",
"__________________####",
"__________________###",
"___________________#",
)