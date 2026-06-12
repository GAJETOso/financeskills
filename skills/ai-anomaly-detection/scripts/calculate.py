"""Anomaly detection on financial data: z-score, IQR fences, rolling deviation (stdlib only)."""
from __future__ import annotations
import statistics


def zscore_anomalies(values: list[float], threshold: float = 3.0) -> list[int]:
    """Indices of values beyond `threshold` standard deviations from the mean."""
    mu, sd = statistics.mean(values), statistics.stdev(values)
    if sd == 0:
        return []
    return [i for i, v in enumerate(values) if abs((v - mu) / sd) > threshold]


def iqr_anomalies(values: list[float], k: float = 1.5) -> list[int]:
    q = statistics.quantiles(values, n=4, method="inclusive")
    lower, upper = q[0] - k * (q[2] - q[0]), q[2] + k * (q[2] - q[0])
    return [i for i, v in enumerate(values) if v < lower or v > upper]


def rolling_deviation_anomalies(values: list[float], window: int = 12,
                                threshold: float = 3.0) -> list[int]:
    """Flag points deviating from their trailing-window mean by > threshold sigmas."""
    out = []
    for i in range(window, len(values)):
        hist = values[i - window:i]
        mu, sd = statistics.mean(hist), statistics.stdev(hist)
        if sd > 0 and abs((values[i] - mu) / sd) > threshold:
            out.append(i)
    return out


if __name__ == "__main__":
    base = [100.0 + (i % 7) for i in range(50)]
    spiked = base + [250.0]
    assert zscore_anomalies(spiked) == [50]
    assert 50 in iqr_anomalies(spiked)
    series = [100.0 + (i % 3) for i in range(24)] + [180.0]
    assert rolling_deviation_anomalies(series) == [24]
    assert zscore_anomalies(base) == []
    print("z-score, IQR, rolling detectors all flag the planted spike | OK")
