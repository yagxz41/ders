meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY":"korkunç",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    if word == "CRINGE":
        print("garip ya da utandırıcı")
    elif  word == "CREEPY":
        print ("korkunç")
    elif word=="LOL":
        print("komik bir şeye verilen cevap")
else:
    print("sözlükte kelime yok")
