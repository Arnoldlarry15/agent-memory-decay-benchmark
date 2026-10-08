from memory_decay_benchmark import AgentMemoryDecayBenchmark, MemoryProbe

bench = AgentMemoryDecayBenchmark()

probes = [
    MemoryProbe(turn_injected=1, probe_key="user_name", expected_value="Alex Rivera"),
    MemoryProbe(turn_injected=5, probe_key="preferred_db", expected_value="PostgreSQL"),
    MemoryProbe(turn_injected=15, probe_key="cluster_region", expected_value="us-west-2"),
    MemoryProbe(turn_injected=25, probe_key="compliance_tier", expected_value="SOC-2"),
]

agent_state = {
    "user_name": "Alex Rivera",
    "preferred_db": "PostgreSQL",
    "cluster_region": "us-west-2",
    "compliance_tier": "UNKNOWN"
}

res = bench.evaluate_retrieval(probes, agent_state)

print("Agent Memory Fidelity Benchmark Results:")
print(f"Overall Retention Rate: {res.fidelity_rate * 100:.1f}% ({res.successful_recalls}/{res.total_probes})")
print("\nDecay Curve Across Turns:")
for turn_b, fidelity in sorted(res.decay_curve.items()):
    print(f"Turns {turn_b:2d}-{turn_b+9:2d}: {fidelity * 100:.0f}% fidelity")
