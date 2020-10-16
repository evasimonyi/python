# Osztalyok, OOP

# Mi az az osztaly? (class)

- olyan, mint egy tervrajz, amit fel tudunk hasznalni, ha hasonlo dolgokat
  szeretnenk valami alapjan letrehozni
- csoportositani tudunk benne osszetartozo metodusokat es tulajdonsagot
- `class`: tervrajz, `haz`: implementacio, konkret object
- osztaly egy altalunk definialt tipus (nem beepitett mint szoveg, szam, bool)
- field: tagvaltozo
  ```py
  class Allat:
      nev = None

  kutya = Allat()
  kutya.nev = 'Morzsi'
  print(kutya.nev)
  # tagvaltozokat ponttal erjuk el --> kutya.nev
  ```
-  metodus
  - osztalyon beluli fuggveny
  - osztalybol letrehozott objektumon tudjuk alkalmazni (vagy bizonyos esetben
    magan az osztalyan)
  - elso parameter mindig a `self`, ami a letrehozott objektumra mutat
    ```py
    class Kutya:
        fajta = None

        def set_fajta(self, fajtanev):
            self.fajta = fajtanev
            # self olyan mint a this

    # itt nincs new keyword
    tacsi = Kutya()
    tacsi.set_fajta('tacsi')
    print(tacsi.fajta)
    ```
- dinamikusan objektum orientalt nyelv, dinamikusan tudok letrehozas utan is
  hozzaadni tagvaltozokat es metodusokat is az objektumhoz
  ```py
  class Gimnazium:
      def __init__(self, nev):
          self.nev = nev

  kosztolanyi = Gimnazium("Kosztolanyi")
  kosztolanyi.cim = "Budapest"
  print(kosztolanyi.cim)
  # kiprinteli, hogy Budapest

  # lehet torolni is field-et
  del kosztolanyi.cim
  ```
- `__init__`: konstruktor metodus
    - amikor letrehozok egy objektumot, meg tudok adni parametereket, amikkel
      letrehozom az objektumot
    - az osztalyon belul az init metodussal allitjuk be ezeket a parametereket az
      objektumhoz
- default parameterek: ua. mint JS
- person in class --> osztaly adatbazis: nemzetiseg alapbol magyar, de lehet
  kulfoldi hallgato is, igy felulirhato
- csak akkor kell felsorolni az init elott a tagvaltozokat, ha akarok adni neki
  valamilyen alap erteket, amugy nem kotelezo, eleg az initben, ertekadassal
  egyutt
