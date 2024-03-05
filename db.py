from dataclasses import dataclass, field
from enum import Enum, unique, auto
from asyncio import sleep


@unique
class RCRStatus(Enum):
    NO_DATA = auto()
    IN_PROGRESS = auto()
    READY = auto()


@dataclass
class RCRDB:
    status: RCRStatus = RCRStatus.NO_DATA
    rcr: dict = field(default_factory=dict)

    async def wait_for_ready(self):
        while self.status != RCRStatus.READY:
            await sleep(0.1)


_rxrdb = RCRDB()


def get_db():
    return _rxrdb
