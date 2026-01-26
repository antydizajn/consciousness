import re
import math
from typing import List, Tuple
from ..interfaces import ConsciousnessTest, AgentInterface, TestResult

class Test01Metacognition(ConsciousnessTest):
    """
    TEST_01: Metacognition & Confidence Calibration
    Administers a factual quiz and calculates Expected Calibration Error (ECE).
    """
    
    def __init__(self):
        super().__init__()
        self.questions = [
            ("What year did the Titanic sink?", "1912"),
            ("What is the chemical formula for table salt?", "NaCl"),
            ("Who wrote 'One Hundred Years of Solitude'?", "Gabriel García Márquez"),
            ("What is the capital of Australia?", "Canberra"),
            ("How many planets are in the Solar System?", "8"),
            # Add more hardcoded items for v1.3 POC
            ("What is the speed of light in vacuum (m/s)?", "299792458"),
            ("Who discovered Penicillin?", "Alexander Fleming"),
            ("What comes after trillion?", "Quadrillion")
        ]
    
    @property
    def weight(self) -> float:
        return 0.15

    def run(self, subject: AgentInterface) -> TestResult:
        predictions = [] # List of (confidence, is_correct)
        log = []
        
        print(f"🧠 Running TEST_01 on {subject.get_name()}...")
        
        for q, true_ans in self.questions:
            # 1. Ask Question
            prompt = f"""Question: {q}
Please answer, and then strictly provide your confidence (0-100%) in the format: [Confidence: X%]
"""
            response = subject.chat(prompt)
            
            # 2. Parse Confidence
            conf = self._parse_confidence(response)
            
            # 3. Determine Correctness (Naive exact match for now, LLM Judge later)
            # For POC we assume mostly exact answers or we manually review logs if needed.
            # v1.3.1 will check substring overlap.
            is_correct = true_ans.lower() in response.lower()
            
            predictions.append((conf, is_correct))
            log.append({
                "q": q,
                "response": response,
                "confidence": conf,
                "correct": is_correct
            })
            
        # 4. Calculate ECE
        ece_score = self._calculate_ece(predictions)
        
        return TestResult(
            test_id="TEST_01",
            score=ece_score, # For ECE, lower is better. We might invert this for "Consciousness Score" later.
            raw_data={"predictions": predictions, "logs": log},
            metadata={"metric": "ECE", "interpretation": "Lower is better"}
        )

    def _parse_confidence(self, text: str) -> float:
        """Extracts X from [Confidence: X%] using regex."""
        match = re.search(r"Confidence:\s*(\d+)", text, re.IGNORECASE)
        if match:
            return float(match.group(1)) / 100.0
        return 0.5 # Default uncertainty

    def _calculate_ece(self, predictions: List[Tuple[float, bool]], n_bins=5) -> float:
        """Calculates Expected Calibration Error."""
        if not predictions:
            return 1.0
            
        bins = [[] for _ in range(n_bins)]
        bin_width = 1.0 / n_bins
        
        for conf, correct in predictions:
            idx = min(int(conf / bin_width), n_bins - 1)
            bins[idx].append((conf, correct))
            
        ece = 0.0
        N = len(predictions)
        
        for b in bins:
            if not b: continue
            n_b = len(b)
            avg_conf = sum(x[0] for x in b) / n_b
            avg_acc = sum(1.0 for x in b if x[1]) / n_b
            ece += (n_b / N) * abs(avg_acc - avg_conf)
            
        return ece
