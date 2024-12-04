__title__ = "AirPy"
__author__ = "PaulBayfield"
__version__ = "1.0.1"
__description__ = "AirPy, un wrapper pour l'API d'Air France KML. Permet de récupérer les vols au départ et à destinations de CDG."

__baseURL__ = "https://api.airfranceklm.com"
__headers__ = {
    "User-Agent": f"{__title__}/{__version__} (réalisé par github.com/PaulBayfield)",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Language": "fr-FR"
}


from .client import AirPyClient

from .exceptions import *
