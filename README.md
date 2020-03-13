Python virtuaaliympäristön luonti:

Teoriaa/Ohje_virtuaaliympäristö.pdf

Tässä projektissa TeollinenInternet/Python/

Tietokantaa ei ole tähän projektiin erikseen lisätty, kun koulun ja omassa käytössä olevien possujen versioero on liian suuri.
Joten:

-asenna postgresql, jos ei ole jo

-luo schema raspi

-luo käyttäjä raspi salasanalla raspi ja aseta se tämän scheman omistajaksi

-luo taulu nimeltä raspi seuraavilla tietueilla:

		-int_id (type serial tai serialize, niin se tekee primääriavaimen autoincrementiksi

		-temperature (variable character)

		-timestamp (variable character)


Postgresql testi:

-PC:llä asenna python virtuaaliympäristö ja aja sieltä 'code .' (TeollinenInternet/Python/)

-Raspissa aja 'python3 cputemp.py'

-Avaa VS Codessa terminaali ja aja siellä python.exe .\tietokanta.py


Ja sitten se tallentaa x-intervallin aikana pilveen lähetettyä dataa possuun.

