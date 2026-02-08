from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  #noqa: F401

class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self, data):
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data):
        pass
    
class ProcessingStage(ABC):
    @abstractmethod
    def process(self, data) -> None:
        pass

class InputStage(ProcessingStage):
    def process(self, data):
        return data


class TransformStage(ProcessingStage):
    def process(self, data):
        data["status"] = "enriched"
        return data


class OutputStage(ProcessingStage):
    def process(self, data):
        return (
            f"Pipeline type: {data['type']} | "
            f"Status: {data['status']} | "
            f"Payload: {data['payload']}"
        )


class JSONAdapter(ProcessingPipeline):
    def process(self, data):
        prepared_data = {
            "type": "json",
            "payload": data
        }
        return self.run(prepared_data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data):
        prepared_data = {
            "type": "csv",
            "payload": data
        }
        return self.run(prepared_data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data):
        prepared_data = {
            "type": "stream",
            "payload": data
        }
        return self.run(prepared_data)

        

class NexusManager:
    def __init__(self):
        self.pipelines = []

    def add_pipeline(self, pipeline):
        self.pipelines.append(pipeline)

    def run_pipeline(self, pipeline_id, data):
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == pipeline_id:
                return pipeline.process(data)
        raise ValueError("Pipeline not found")

if __name__ == "__main__":

    manager = NexusManager()

    json_pipeline = JSONAdapter("JSON_001")
    csv_pipeline = CSVAdapter("CSV_001")
    stream_pipeline = StreamAdapter("STREAM_001")

    for pipeline in (json_pipeline, csv_pipeline, stream_pipeline):
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        manager.add_pipeline(pipeline)

    result = manager.run_pipeline(
        "JSON_001",
        '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    )
    print(result)