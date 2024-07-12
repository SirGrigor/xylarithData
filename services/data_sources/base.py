from abc import ABC, abstractmethod
from typing import List, Dict


class DataCollector(ABC):
    @abstractmethod
    def collect_data(self) -> List[Dict]:
        pass
