# File kezelés

- open()
  - ketfelekeppen tudunk file-t megnyitni
  ```py
  file = open('iras.txt', 'w', encoding='utf-8')
  # vagy
  with open('iras.txt', 'w', encoding='utf-8') as file:
    szoveg = 'python'
    file.write(szoveg)
  ```
  - a with kulcsszoval megnyitva :-ot kell hasznalni
  - kulonbseg: amint kilepunk a with "testebol" (indentacio), magatol bezarja a
    megnyitott filet, az elso megoldassal magunknak kell lezarni: `file.close()`
- read, write és append mód: olvasas, iras, hozzafuzes
  - ha nem letezik a file, akkor letrehozza
  - ha letezik a file, felulirja:
    - az elso output.write fogja uriteni a file-t
    - strip: ignoralja az uj sor karaktert, ami miatt egy felesleges uj sort printel
    ```py
    for line in fromroot:
        print(line.strip())
    ```
- file.readline()
  - egyesevel olvassa be a file tartalmat
  - ciklussal hasznaljuk
  - memoriakimelo
  ```py
  #for ciklussal
  for line in fromroot:
      print(line)

  # vagy while ciklussal

  line = file.readline()
  while line:
      print(line.strip())
      line = file.readline()
  file.close()
  ```
- file.close()
  - ha nem a `with` kontext managerrel nyitunk meg file-t, manualisan be kell
    zarnunk miutan vegeztunk vele
- file.read()
  - az egesz file tartalmat egyszerre olvassa ki, nem szokas hasznalni (memoria)
  - egy listaval ter vissza, egy sor egy elem a listaban
  - az elemek (sorok) vegere tesz egy uj sor karaktert (\n)
- file.write()
- UTF-8
  - karakterkodolas
  - mar nem szukseges megadni file manipulacio soran, mert mar ez az alap

## egyik filebol a masikba iras

```py
with open('text.txt', 'r', encoding='utf-8') as inputfile:
    with open('iras.txt', 'w', encoding='utf-8') as outputfile:
        line = inputfile.readline()
        while line:
            outputfile.write(line)
            line = inputfile.readline()
```

- ez miert irja bele a teljes tartalmat?
- a with open write utani tartalommal irja felul a futtatas elotti allapotot
  de a cikluson beluli write mar append-del
- write helyett append: a futtatas elotti tartalmat megtartja, es hozzafuz

- file elerese:
  - ROOT FOLDERBOL
    - alapvetoen a root folderbol olvassa a fileokat, ami most nekem a python
    - ilyenkor eleg csak a filenevet beilleszteni
    ```py 
    fromroot = open('text.txt', 'r', encoding='utf-8')
    print(fromroot.readlines())
    ```
  - ABSZOLUT ELERESI UTTAL
    - de adhatunk neki abszolut eleresi utvonalat is, ezt itt erjuk el:
    ```py
    import os
    print(os.path.dirname(os.path.abspath(__file__)))
    file = open('/Users/simonyieva/Documents/greenfox/python/material_review/Evi/oop/szoveg.txt', 'r', encoding='utf-8')
    ```
