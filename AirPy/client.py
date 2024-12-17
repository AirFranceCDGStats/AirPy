from . import __headers__
from .requests import AirPyRequests
from .logger import Logger
from aiohttp import ClientSession
from typing import Literal


class AirPyClient:
    def __init__(self, key: str, session: ClientSession, logs: Logger = None) -> None:
        """
        Initialise la classe AirPyClient

        :param key: Clé API
        :param session: Session
        :param logs: Logs
        """
        self.key = key[:8]

        self.__headers = {
            **__headers__,
            "Api-Key": key
        }

        if not logs:
            logs = Logger("requests")

        self.client = AirPyRequests(headers=self.__headers, session=session, logs=logs)

        self.flights = Flights(self.client)


class Flights:
    def __init__(self, client: AirPyRequests) -> None:
        self.client = client


    async def get(
        self,
        startRange: str = None,
        endRange: str = None,
        departureCity: str = None,
        arrivalCity: str = None,
        carrierCode: str = None,
        timeType: Literal["U", "L"] = "U",
        page: int = 0,
    ) -> tuple[list[dict], dict]:
        """
        Récupère les vols

        :param startRange: Date de début
        :param endRange: Date de fin
        :param departureCity: Ville de départ
        :param arrivalCity: Ville d'arrivée
        :param carrierCode: Code de la compagnie aérienne
        :param timeType: Type de temps
        :param page: Page
        :return: Les vols
        """
        return await self.client.getFlights(
            startRange=startRange,
            endRange=endRange,
            departureCity=departureCity,
            arrivalCity=arrivalCity,
            carrierCode=carrierCode,
            timeType=timeType,
            page=page,
        )
