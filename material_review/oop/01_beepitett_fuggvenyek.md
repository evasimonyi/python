# Beepitett fuggvenyek

- `abs()`
  - abs(x) Egy szám abszolút értékét adja vissza (0-tol valo tavolsag)
  ```py
  print(abs(-5.3))
  ```
- `enumerate()`
  - ciklusokban hasznaljuk, ha szukseg van indexre
  - a parameter egy iterátor vagy egy sorozat lehet, tehat vegigmeheto tipusok
    (enumerable): lista, tuple, string, range
  - enumerate tipust ad vissza:
    (0, thing[0]), (1, thing[1]), (2, thing[2]), stb...)
    ```py
    napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek"]

    for i in range(len(napok)):
        item = napok[i]
        print(item)
    # eredmeny:
    # hetfo
    # kedd
    # szerda
    # csutortok
    # pentek

    # ehelyett írhatjuk a következőt:

    for i, item in enumerate(napok):
        print(napok[i])
    # ugyanaz az eredmeny

    # nem enumerate, de erdekes, es hasznos:
    # dictionary-kon vegigmenni ciklussal:

    person = {
        "nev": "Anna",
        "kor": 16,
        "address": "Budapest"
    }

    for key, value in person.items():
        print(key, value)

    # nev Anna
    # kor 16
    # address Budapest
    ```
- `isinstance(object, classinfo)`
  - igazzal tér vissza, ha object a classinfo argumentum egy példánya,
  - illetve ha annak egy közvetlen vagy indirekt leszármazottja
  - a classinfo lehet objektumokat tartalmazó tuple is, ebben az esetben igazat
    ad a függvény, ha valamelyik objektumra teljesül az isinstance() reláció
  - type(324) --> int
  - isinstance(324, int) --> true
  - osztalyoknal lehet meg hasznos
- `max()`
  - Egy nem üres szekvencia legnagyobb elemét adja vissza értékül.
    ```py
    print(max(1,2,4))
    print(max([1,2,4]))
    ```
- `min()`
  - min(s) Egy nem üres szekvencia legkisebb elemét adja vissza értékül.
    ```py
    print(min(1,2,4))
    print(min([1,2,4]))
    ```
- `reversed()`
  - visszatér egy fordított bejárású iterátorral
  - parameter: valami, amin vegig lehet menni, lista, string, tuple, ...
  - ugyanaz mint lista[::-1], de a reversed() olvashatobb

- `round()`
    ```py
    print(round(3.422312312, 4))
    # 3.4223
    ```
  - round(x, n=0): x lebegõpontos értékét a tizedes pont után n számjegyre
    kerekítve adja vissza
- `sum()`
  - sum(iterable, start=0)
  - csak szám típusú paramétert lehet neki megadni
  - tehát nem lehet például stringek konkatenálására használni
    ```py
    print(sum(4, 5, 6, 7, 5))
    # TypeError: sum() takes at most 2 arguments (5 given)

    # tuple:
    print(sum((4, 8, 242, 42342, 2)))
    # eredmeny: 42598

    # lista;
    print(sum([3, 4, 5, 5555, 2]))
    # eredmeny: 5569
    ```
- `list.index()`
  - numbers.index(3)
  - olyan, mint az indexOf a JS-ben
  - visszaadja a 3-as szam indexet a listabol (iterable-bol)
    ```py
    napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek"]
    print(napok.index("kedd"))
    # eredmeny: 2
    ```

## Konverziók vagy castolas
  
Adatok tipusanak atalakitasa szamma, szovegge

- `int()`
  - csak egesz szamot tud bevenni string formaban, tehat a "2.3" nem fog menni
- `float()`
  - float("3.412827384632846238")
- `list()`
  - listava alakitja at a parameterben bekapottakat
  - tuple pl: list('alma') --> szetdobja betukre
- `str()`
  - str(2312) --> "2312"
