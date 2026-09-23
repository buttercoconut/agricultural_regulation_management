# Regulation service
from typing import List
from ..models.regulation import Regulation

class RegulationService:
    def __init__(self):
        # In-memory store for demo; replace with DB logic
        self._store: List[Regulation] = []
        self._id_counter = 1

    async def create_regulation(self, data: dict) -> Regulation:
        regulation = Regulation(**data)
        regulation.id = self._id_counter
        self._id_counter += 1
        self._store.append(regulation)
        return regulation

    async def list_regulations(self) -> List[Regulation]:
        return self._store
