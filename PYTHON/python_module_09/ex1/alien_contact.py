from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=100.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(min_length=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_validation_rules(self) -> "AlienContact":

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        telepathic = ContactType.telepathic
        if self.contact_type == telepathic and self.witness_count < 3:
            error_message = "Telepathic contact requires at least 3 witnesses"
            raise ValueError(error_message)

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")

        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        alien_contact_info = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-03-10T12:00:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli'
        )

        print(f"ID: {alien_contact_info.contact_id}")
        print(f"Type: {alien_contact_info.contact_type}")
        print(f"Location: {alien_contact_info.location}")
        print(f"Signal: {alien_contact_info.signal_strength}/10")
        print(f"Duration: {alien_contact_info.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact_info.witness_count}")
        print(f"Message: \'{alien_contact_info.message_received}\'\n")
        print("======================================")
    except ValueError as e:
        err = e.errors()[0]
        print(err["msg"])
    try:
        print("Expected validation error:")
        alien_contact_info = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-03-10T12:00:00",
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=4,
            message_received=''
        )
    except ValueError as e:
        err = e.errors()[0]
        print(err["msg"])


if __name__ == "__main__":
    main()
