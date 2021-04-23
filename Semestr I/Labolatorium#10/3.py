tekst = f"Długo na szturm i szaniec pogłądał w miłczeniu. Na koniec rzekł" \
        f": 'Stracona' ."
print(tekst)

fragment = tekst[:(tekst.find(".", 0,len(tekst)-1))]
print(fragment)

teks_lista = ["Zwinny", 'lis', 'przeskoczył', 'nad',' leniwym', 'psem','.']

tekslista = teks_lista[0:len(teks_lista)-2]
print(tekslista)

listaNaString = ' '.join(map(str, teks_lista))
calytekst = listaNaString

print(calytekst)