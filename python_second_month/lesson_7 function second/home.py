facts = {
    2012: "Rossia va AQsh-da prezident saylovlari bolib otdi",
    2013: "Ukrainada siyosiy inqiroz",
    2014: "“Soyuz TMA-10M” kosmik kemasi Qozog‘istonga qo‘ndi",
    2015: "Litva yevroni qabul qilib, evrozonaning 19-a'zosiga aylandi",
    2016: "Rossiya Suriyadan harbiy guruhini olib chiqishni boshladi",
    2017: "AQSh va Isroil YUNESKOdan chiqish rejalarini e'lon qildi",
    2018: "The Game Awards 2018 bolib o'tdi",
    2019: "covid-19 kasalligi paydo boldi",
    2020: "AQsh va Eron orasida ziddiyat",
    2021: "Rossiadan kop kompaniyalar chiqib ketishi",
    2022: "Ukraina va Rossia orasida ziddiyat",
    2023: "Gamescom 2023 bolib otdi"
}

year = input('Yilni kiriting: ')
def vaqt_mashinasi(yil):
    if yil in facts:
        return f'{yil}-yilda {facts[yil]} bo\'lgan'
    else:
        return "Bu yil haqida ma'lumot yo'q"

result = vaqt_mashinasi(year)
print(result)