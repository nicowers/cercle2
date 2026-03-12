from enum import Enum
from pydantic import Basemodel, Field ,model_validator
from datetime import datetime

class Rank(Enum):
    cadet= "cadet"
    officer= "officer"
    lieutenant= "lieutenant"
    captain= "captain"
    commander= "commander"

class CrewMember(Basemodel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(ge=3, le=30)
    years_experience:int = Field(ge=0, le=50)
    is_active: bool = True

class SpaceMission(Basemodel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3 , max_length=50)
    launch_date: datetime
    duration_days: int = Field(min_length=1, max_length=3650)
    crew: list[CrewMember] = Field(max_length=12)
    mission_status: str= "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator('after')
    def mission_validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Contact ID must start with 'AC'")
        if not self
        return self