meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/sinirlenmek"
            "Bro": "Kardeş"
            "Skill": "Yetenek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Böyle bir kelime bulunamadı.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
