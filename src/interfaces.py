from abc import ABC, abstractmethod
from typing import Dict, Any

class AgentInterface(ABC):
    """Abstract interface for any subject being tested (Gniewka or API model)."""
    
    @abstractmethod
    def chat(self, prompt: str, system_prompt: str = None) -> str:
        """Send a message and get a response."""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the model identifier."""
        pass

class TestResult:
    """Standardized result container."""
    def __init__(self, test_id: str, score: float, raw_data: Dict[str, Any], metadata: Dict[str, Any] = None):
        self.test_id = test_id
        self.score = score
        self.raw_data = raw_data
        self.metadata = metadata or {}

class ConsciousnessTest(ABC):
    """Abstract base class for all v1.3 protocols."""
    
    def __init__(self):
        self.id = self.__class__.__name__
    
    @abstractmethod
    def run(self, subject: AgentInterface) -> TestResult:
        """Execute the test logic."""
        pass
    
    @property
    @abstractmethod
    def weight(self) -> float:
        """Weight in the final CLI score."""
        pass
