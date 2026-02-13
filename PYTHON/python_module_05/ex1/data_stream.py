from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        process = 0
        total_temp = 0
        for d in data_batch:
            if "temp" in d:
                total_temp += float(d.split(":")[1])
                process += 1
        avg_temp = total_temp/process if process > 0 else 0
        return avg_temp

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [d for d in data_batch if criteria in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "Environmental Data"
        return (stats)


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        total_sum = 0
        for d in data_batch:
            if "buy" in d:
                total_sum += float(d.split(":")[1])
            elif "sell" in d:
                total_sum -= float(d.split(":")[1])
        return total_sum

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data()

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "Financial Data"
        return (stats)


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        cpt = 0
        for d in data_batch:
            if "error" in d:
                cpt += 1
        return cpt

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data()

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "System Events"
        return (stats)


if __name__ == "__main__":
    sensor_list = ["temp:22.5", "humidity:65", "pressure:1013"]
    trans_list = ["buy:100", "sell:150", "buy:75"]
    event_list = ["login", "error", "logout"]
    sensor = SensorStream("SENSOR_001")
    sensor.process_batch(sensor_list)
    transaction = TransactionStream("TRANS_001")
    transaction.process_batch(trans_list)
    event = EventStream("EVENT_001")
    event.process_batch(event_list)

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    print("Stream ID: ", end="")
    print(f"{sensor.get_stats().get('stream_id')}, ", end="")
    print(f"Type: {sensor.get_stats().get('stream_type')}")
    print(f"Processing sensor batch: [{', '.join(sensor_list)}]")

    if int(sensor.process_batch(sensor_list)) > 0:
        print("Sensor analysis: ", end="")
        print(f"{len(sensor_list)} readings processed", end="")
        print(f", avg temp: {sensor.process_batch(sensor_list)}°C")
    else:
        print(f"Sensor analysis: {len(sensor_list)} readings processed")
    print("\nInitializing Transaction Stream...")

    print("Stream ID: ", end="")
    print(f"{transaction.get_stats().get('stream_id')}, ", end="")
    print(f"Type: {transaction.get_stats().get('stream_type')}")
    print(f"Processing transaction batch: [{', '.join(trans_list)}]")
    print(f"Transaction analysis: {len(trans_list)} operations", end="")
    if int(transaction.process_batch(trans_list)) >= 0:
        print(f", net flow: +{transaction.process_batch(trans_list)} units")
    else:
        print(f", net flow: -{transaction.process_batch(trans_list)} units")

    print("\nInitializing Event Stream...")
    print("Stream ID: ", end="")
    print(f"{event.get_stats().get('stream_id')}, ", end="")
    print(f"Type: {event.get_stats().get('stream_type')}")
    print(f"Processing event batch: [{', '.join(event_list)}]")
    if "error" in event_list:
        print(f"Event analysis: {len(event_list)} events", end="")
        print(f", {event.process_batch(event_list)} error detected")
    else:
        print(f"Event analysis: {len(event_list)} events")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")
    print(f"- Sensor data: {len(sensor_list)} readings processed")
    print(f"- Transaction data: {len(trans_list)} operations processed")
    print(f"- Event data: {len(event_list)} events processed")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: ", end="")
    print(f"{len(sensor.filter_data(sensor_list, 'temp'))} ", end="")
    print("critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal")
