letters ={"A":"А","a":"а",
          "X":"Х","x":"х",
          "B":"В",
          "C":"C","c":"с",
          "K":"К","k":"к",
          "M":"М","O":"О",
          "E":"Е","P":"Р",
          "T":"Т",
          "o":"о",
          "p":"р",
          "y":"у"}
letters_ru ={"А":"A","а":"a",
             "Х":"X","х":"x",
             "В":"B",
             "С":"C","с":"c",
             "К":"K","к":"k",
             "М":"M",
             "О":"O",
             "Е":"E",
             "Р":"P",
             "Т":"T",
             "о":"o",
             "р":"p",
             "у":"y"}
with open("input.txt", "r", encoding="utf-8") as f:
    txt = f.read()

result=''
for i in txt:
    if i in letters:
        result += letters[i]
    else:
        result += i
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)

with open("output.txt", "r", encoding="utf-8") as s:
    txt_1 = s.read()
decod = ''
for j in txt_1:
    if j in letters_ru:
        decod += letters_ru[j]
    else:
        decod += j
with open("decoder.txt", "w", encoding="utf-8") as s:
    s.write(decod)
