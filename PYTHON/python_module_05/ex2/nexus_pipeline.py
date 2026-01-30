from abc import ABC, abstractmethod

class ProcessingPipeline(ABC):
    
    @abstractmethod
    def :
    
class  InputStage():
    def process(self, data: Any) -> Any:


class TransformStage():
    def process(self, data: Any) -> Any:


class  OutputStage():
    def process(self, data: Any) -> Any:

class JSONAdapter(ProcessingPipeline):

class CSVAdapter(ProcessingPipeline):

class StreamAdapter(ProcessingPipeline):

class NexusManager():