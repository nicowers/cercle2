from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    try:
        station_info = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-10T12:00:00"
        )
        print(f"ID: {station_info.station_id}")
        print(f"Name: {station_info.name}")
        print(f"Crew: {station_info.crew_size} people")
        print(f"Power: {station_info.power_level}%")
        print(f"Oxygen: {station_info.oxygen_level}%")
        if station_info.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: Non Operational")

        print("\n========================================")
        print("Expected validation error:")
    except Exception as e:
        print(e.errors()[0]['msg'])
    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-10T12:00:00"
        )
    except Exception as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
