from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class MemoryProbe:
    turn_injected: int
    probe_key: str
    expected_value: str

@dataclass
class MemoryDecayResult:
    total_probes: int
    successful_recalls: int
    fidelity_rate: float
    decay_curve: Dict[int, float]

class AgentMemoryDecayBenchmark:
    """Evaluates how effectively an agent retains key state variables across extended multi-turn sessions."""

    def evaluate_retrieval(self, probes: List[MemoryProbe], simulated_state: Dict[str, str]) -> MemoryDecayResult:
        success = 0
        turn_success: Dict[int, List[bool]] = {}

        for p in probes:
            retrieved = simulated_state.get(p.probe_key, "")
            is_match = retrieved.strip().lower() == p.expected_value.strip().lower()
            if is_match:
                success += 1

            turn_bucket = (p.turn_injected // 10) * 10
            if turn_bucket not in turn_success:
                turn_success[turn_bucket] = []
            turn_success[turn_bucket].append(is_match)

        tot = len(probes)
        rate = success / tot if tot else 0.0

        decay = {}
        for b, results in turn_success.items():
            decay[b] = sum(results) / len(results) if results else 0.0

        return MemoryDecayResult(
            total_probes=tot,
            successful_recalls=success,
            fidelity_rate=rate,
            decay_curve=decay
        )
