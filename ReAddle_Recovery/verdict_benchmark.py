# ===============================
# Module: verdict_benchmark.py
# Purpose: Benchmark performance of the verdict engine under
#          varying input types and stress conditions
# Part of: Verdict Engine Performance Suite
# ===============================

import logging
import time
from typing import List
from framework_models import ParsedInput, VerdictContext, EngineOutcome, BenchmarkResult
from verdict_interface import request_verdict

logger = logging.getLogger(__name__)

def benchmark_verdicts(
    samples: List[ParsedInput],
    context: VerdictContext,
    runs_per_sample: int = 3
) -> List[BenchmarkResult]:
    """
    Run benchmark tests across sample inputs.

    Args:
        samples (List[ParsedInput]): Structured inputs to test
        context (VerdictContext): Evaluation context
        runs_per_sample (int): Number of times to run each sample

    Returns:
        List[BenchmarkResult]: Performance results
    """
    results = []

    for i, sample in enumerate(samples):
        logger.info(f"Benchmarking sample {i+1}/{len(samples)}")
        times = []
        success_count = 0

        for _ in range(runs_per_sample):
            start = time.perf_counter()
            outcome: EngineOutcome = request_verdict(sample, context)
            end = time.perf_counter()

            times.append(end - start)
            if outcome.success:
                success_count += 1

        avg_time = sum(times) / len(times)
        result = BenchmarkResult(
            sample_index=i,
            avg_runtime_ms=avg_time * 1000,
            success_rate=success_count / runs_per_sample
        )
        results.append(result)

    return results
