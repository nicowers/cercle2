from typing import Any, List, Dict, Union, Optional  # noqa: F401
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nInvalid Numeric verified\n")
        len_d = len(data)
        total = sum(data)
        avg = total / len_d
        print("\nInitializing Numeric Processor...")
        print(f"Processing data: {data}")
        print("Validation: Numeric data verified")
        return (f"Processed {len_d} numeric values, sum={total}, avg={avg}")

    def process_simultaneously(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nInvalid Numeric verified\n")
        len_d = len(data)
        total = sum(data)
        avg = total / len_d
        return (f"Processed {len_d} numeric values, sum={total}, avg={avg}")

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list)
                and all(isinstance(x, (int, float)) for x in data))

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nInvalid text\n")
        total_len = len(data)
        words = len(data.split())
        print("\nInitializing Text Processor...")
        print("Processing data: \"Hello Nexus World\"")
        print("Validation: Text data verified")
        return (f"Processed text: {total_len} characters, {words} words")

    def process_simultaneously(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nInvalid text\n")
        total_len = len(data)
        words = len(data.split())
        return (f"Processed text: {total_len} characters, {words} words")

    def validate(self, data: Any) -> bool:
        return (isinstance(data, str))

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nLog entry rejected\n")
        level = ""
        if data.startswith("ERROR"):
            level = "ALERT"
        elif data.startswith("INFO"):
            level = "INFO"
        elif data.startswith("WARNING"):
            level = "WARNING"
        else:
            level = "UNKNOWN"
        print("\nInitializing Log Processor...")
        print(f"Processing data: {data}")
        print("Validation: Log entry verified")
        error_lvl = f"[{level}] {data.split(':')[0]}"
        error_lvl += f" level detected:{data.split(':')[1]}\n"
        return (error_lvl)

    def process_simultaneously(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\nLog entry rejected\n")
        level = ""
        if data.startswith("ERROR"):
            level = "ALERT"
        elif data.startswith("INFO"):
            level = "INFO"
        elif data.startswith("WARNING"):
            level = "WARNING"
        else:
            level = "UNKNOWN"
        process = f"[{level}] {data.split(':')[0]}"
        process += f" level detected:{data.split(':')[1]}"
        return (process)

    def validate(self, data: Any) -> bool:
        return (isinstance(data, str) and ":" in data)

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]
    print_all = ""
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')
    try:
        for processor, data in zip(processors, data):
            result = processor.process(data)
            print(processor.format_output(result))
    except ValueError as e:
        print(e)
    print("Processing multiple data types through same interface...")
    try:
        for index, (processor, data) in enumerate(
            zip(
                processors, [[1, 2, 3], "Hello World", "INFO: System ready"]),
                start=1):
            result = processor.process_simultaneously(data)
            print_all = (processor.format_output(result)).split("Output:")
            print(f"Result {index}:{print_all[1]}")
    except ValueError as e:
        print(e)
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
