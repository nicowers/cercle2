from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass
    
class ProcessingStage():
    ...

class  InputStage:
    def process(self, data: Any) -> Any:


class TransformStage:
    def process(self, data: Any) -> Any:


class  OutputStage:
    def process(self, data: Any) -> Any:

class JSONAdapter(ProcessingPipeline):

class CSVAdapter(ProcessingPipeline):

class StreamAdapter(ProcessingPipeline):

class NexusManager():