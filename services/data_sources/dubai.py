from typing import List, Dict

from services.data_sources.base import DataCollector


class DubaiDataCollector(DataCollector):
    def collect_data(self) -> List[Dict]:
        # Implement data collection logic here
        data = [
            {"id": 1, "name": "Dubai Company 1", "region": "dubai", "additional_info": {"key": "value"}},
            # More data...
        ]
        return data
