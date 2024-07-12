from fastapi import APIRouter, HTTPException

from models.data_model import DataCollectionResponse
from services.data_sources.country_enum import CountryEnum
from services.data_sources.dubai import DubaiDataCollector
from services.data_sources.germany import GermanyDataCollector

router = APIRouter()


@router.post("/{country}", response_model=DataCollectionResponse)
async def collect_data(country: CountryEnum):
    if country == CountryEnum.dubai:
        collector = DubaiDataCollector()
    elif country == CountryEnum.germany:
        collector = GermanyDataCollector()
    else:
        raise HTTPException(status_code=404, detail="Country not supported")

    data = collector.collect_data()

    # Save data to the database (example, adjust as needed)
    # await save_data_to_db(data)

    return {"status": "Data collection initiated", "country": country, "data": data}
