# Hibakezeles

- a file olvasassal kez a kezben jar, hiszen tobb hiba is felmerulhet
- ha a program crushol, lathatjuk: exit code: 1
- exit code: 0 a jo, minden mas hibat jelent
- mas nyelvekhez hasonloan try aggal kezdjuk, de throw es catch helyett except
  ```py
  try:
      # megprobal valamit
      # hibat raise-el
      # raise Error: custom hibat tudok raiselni
  except NameError as e:
      # e: alias, elnevezem a NameErrort
      print(e)
      # ha nem sikerul tehat hiba tortenik, akkor ez az ag fut le
  except IndexError:
      # vagy ez
      # listaelem indexelesnel lehet ilyen hiba
  else:
      # akkor fut le, ha a try lefut jol, nem nagyon hasznaljuk
  finally:
      # ezelott barmelyik ag fut le, ez is le fog
      # file bezarasa
      # nem nagyon hasznaljuk
      # popup ablak bezarasa: adatok elmentese vagy sikerul vagy nem, zard be
  ```
- miert jo a try-except?
  ```py
  print(hello)
  print(1 + 2)
  # NameError: name 'hello' is not defined
  # nem fog lefutni a masodik print, megall a programom

  # vs
  try:
      print(hello)
  except Exception as e:
      print(e)

  print (1 + 2)
  # name 'hello' is not defined
  # 3
  # fut tovabb a programom, kezeltem azt az esetet, ha hiba fordulna elo
  ```
- NameError
  - Raised when a local or global name is not found
  ```py
  print(hello)
  # NameError: name 'hello' is not defined
  ```
- IndexError
  - Raised when a sequence subscript is out of range
  ```py
  lista = [1, 2]
  print(lista[5])
  # IndexError: list index out of range
  ```
- ZeroDivisionError
    ```py
  print(1 / 9)
  # ZeroDivisionError: division by zero
  ```
- ha tobb except blokkot is felsorolunk (filenotfound, index, dividebyzero),
  javasolt a legpontosabbtol (az exceptions hierarchiaban legalul) a
  legaltalanosabb fele (hierarchiaban legfelul) haladva soroljuk fel
- ezzel lehet biztositani hogy a kodban levo logikai hibak ne maradjanak rejtve
- [Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

## Melyikbol hany ag lehetseges?

- try: 1
- except: barmennyi
- else: 1
- finally: 1
