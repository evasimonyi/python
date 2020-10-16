# Modulok

- minden Python file egy modul is egyben
- a file-ok alapbol nem latjak egymas tartalmat
- ha szeretnem hasznalni egy masik file-ban megirt kodomat, be kell hozza
  importalnom
- a masik file tartalmat nem kell exportalni, ahogy lathattuk mas nyelvben
- ez a classoknal es konyvtaraknal fog jol jonni, az osztalyokat es metodusokat
  ajanlott kulon file-okba szetszedni

```py
import valami as osszeadas
osszeadas()

from copy import deepcopy
# elozo hetrol matrix deepcopyzasa
# mivel komplex tipus, deepcopyzni kell, ha modositjuk a kopit

from add import *
# ez mindent importal az add modul-bol
# nem ajanlott a csillag, eltorheti kesobb a kodot -->
# ha van egy olyan metodus amit importalunk es ugyanolyan nevvel hozunk letre
# egy fv-t ebben a fileban is akkor nem tudja majd hogy melyiket hasznalja,
# felulirja majd
# inkabb felsoroljuk mit importalunk
```

- namespace: x.szin y.szin, mast jelent --> mast takarhat a szin a file-okban
- pip: kulso modulok telepitesehez szukseges installer
- [dokumentacio](https://pypi.org/project/pip/)
- `pip3 --version` --> ha nincs fent, mentor segit majd
- pip help listazza a lehetseges parancsokat --> google, probald ki
- proba modul installalas: `numpy`
  - bonyolultabb matrix szamolos dolgokat is lehet csinalni vele
  - `pip3 install numpy` --> letolti es installalja is
  - dokumentaciobol probakod, matrixot general:
    ```py
    import numpy as np
    print(np.arange(15).reshape(3,5))

    # eredmeny
    # [[ 0  1  2  3  4]
    # [ 5  6  7  8  9]
    # [10 11 12 13 14]]
    ```

- pip nelkul vs code-ban telepiteni package-t hogy lehet? gugli pie charm?
- upgrade
