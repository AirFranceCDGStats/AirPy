<div align="center">
<img src="./assets/banner.png" alt="AirPy Banner"/>
  
# AirPy
AirPy est une librairie Python qui permet de récupérer les vols au départ et à destinations de CDG via l'API officielle d'Air France KML.

</div>
  
# 📖 • Sommaire

- [🚀 • Présentation](#--présentation)
- [⚙️ • Installation](#--installation)
- [📄 • Utilisation](#--utilisation)
- [📃 • Crédits](#--crédits)
- [📝 • License](#--license)

# 🚀 • Présentation

Ce dépôt contient le code source de la librairie AirPy qui permet de récupérer les vols au départ et à destinations de CDG via l'API officielle d'Air France KML.


# ⚙️ • Installation

La librairie n'est pas encore disponible sur PyPi, il faut donc l'installer manuellement en exécutant la commande suivante :
```
pip install git+https://github.com/AirFranceCDGStats/AirPy
```

# 📄 • Utilisation

```python
from AirPy import AirPy


async def main():
    """
    Exemple d'utilisation de la librairie AirPy
    """
    session = ClientSession()

    client = AirPy(
        key="CLE D'API"
        session=session
    )

    # Récupérer les vols
    vols = await client.flights.get(...)

    print(vols)


    await session.close()


if __name__ == "__main__":
    asyncio.run(main())
```

# 📃 • Crédits

- [Paul Bayfield](https://github.com/PaulBayfield)

# 📝 • License

AirPy sous licence [Apache 2.0](LICENSE).

```
Copyright 2024 Paul Bayfield

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
