from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=None, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> "SpaceMission":
        capt_or_comm = 0
        crew_experience = 0
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for crewmbr in self.crew:
            if crewmbr.rank == Rank.commander or crewmbr.rank == Rank.captain:
                capt_or_comm += 1
        if capt_or_comm == 0:
            error_message = "Mission must have at least one "
            error_message += "Commander or Captain"
            raise ValueError(error_message)
        for crewmbr in self.crew:
            if crewmbr.years_experience >= 5:
                crew_experience += 1
        if self.duration_days > 365 and crew_experience / len(self.crew) < 0.5:
            error_message = "Mission must have at least half of the crew,"
            error_message += "with 5+ years experience for long mission"
            error_message += "(365 days or more)"
            raise ValueError(error_message)
        for crewmbr in self.crew:
            if crewmbr.is_active is False:
                raise ValueError("All crewmembers must be active")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        crewmember1 = CrewMember(
            member_id="641298",
            name="Sarah Connor",
            rank="commander",
            age=23,
            specialization="Mission Command",
            years_experience=2
        )

        crewmember2 = CrewMember(
            member_id="043907",
            name="John Smith",
            rank="lieutenant",
            age=42,
            specialization="Navigation",
            years_experience=12
        )

        crewmember3 = CrewMember(
            member_id="294988",
            name="Alice Johnson",
            rank="officer",
            age=74,
            specialization="Engineering",
            years_experience=32
        )

        crew_team = [crewmember1, crewmember2, crewmember3]

        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-03-10T12:00:00",
            duration_days=900,
            crew=crew_team,
            mission_status="in progress",
            budget_millions=2500.0
        )

        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}M")
        print(f"Crew size: {len(space_mission.crew)}")
        print("Crew members:")
        for crew_members in crew_team:
            print(f"- {crew_members.name} ({crew_members.rank}) - ", end=")")
            print(f"{crew_members.specialization}")
        print("\n=========================================")
    except Exception as e:
        err = e.errors()[0]
        print(err['msg'])
    try:
        print("Expected validation error:")
        crewmember1 = CrewMember(
            member_id="641298",
            name="Sarah Connor",
            rank="officer",
            age=23,
            specialization="Mission Command",
            years_experience=2
        )

        crewmember2 = CrewMember(
            member_id="043907",
            name="John Smith",
            rank="lieutenant",
            age=42,
            specialization="Navigation",
            years_experience=12
        )

        crewmember3 = CrewMember(
            member_id="294988",
            name="Alice Johnson",
            rank="officer",
            age=74,
            specialization="Engineering",
            years_experience=32
        )

        crew_team = [crewmember1, crewmember2, crewmember3]

        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-03-10T12:00:00",
            duration_days=900,
            crew=crew_team,
            mission_status="in progress",
            budget_millions=2500.0
        )
    except Exception as e:
        err = e.errors()[0]
        print(err['msg'])


if __name__ == "__main__":
    main()
