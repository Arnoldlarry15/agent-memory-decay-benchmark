from memory_decay_benchmark import AgentMemoryDecayBenchmark, MemoryProbe

def test_memory_decay():
    bench = AgentMemoryDecayBenchmark()
    probes = [MemoryProbe(turn_injected=1, probe_key="k1", expected_value="v1")]
    res = bench.evaluate_retrieval(probes, {"k1": "v1"})
    assert res.fidelity_rate == 1.0
    assert res.successful_recalls == 1
