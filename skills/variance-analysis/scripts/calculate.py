"""Standard cost variance calculations: material, labor, overhead."""
from __future__ import annotations
from dataclasses import dataclass


def material_price_variance(std_price: float, act_price: float, act_qty: float) -> float:
    """Positive = favorable."""
    return (std_price - act_price) * act_qty


def material_usage_variance(std_qty: float, act_qty: float, std_price: float) -> float:
    """std_qty = standard quantity allowed for ACTUAL output. Positive = favorable."""
    return (std_qty - act_qty) * std_price


def labor_rate_variance(std_rate: float, act_rate: float, act_hours: float) -> float:
    return (std_rate - act_rate) * act_hours


def labor_efficiency_variance(std_hours: float, act_hours: float, std_rate: float) -> float:
    """std_hours = standard hours allowed for ACTUAL output."""
    return (std_hours - act_hours) * std_rate


@dataclass
class FixedOverheadResult:
    spending_variance: float   # budget - actual (positive favorable)
    volume_variance: float     # applied - budget (positive favorable / over-absorbed)
    applied: float


def fixed_overhead_variances(
    budgeted_foh: float, actual_foh: float,
    std_hours_allowed: float, foh_rate: float,
) -> FixedOverheadResult:
    applied = std_hours_allowed * foh_rate
    return FixedOverheadResult(
        spending_variance=budgeted_foh - actual_foh,
        volume_variance=applied - budgeted_foh,
        applied=applied,
    )


def label(v: float) -> str:
    return f"{abs(v):,.2f} {'F' if v >= 0 else 'U'}"


if __name__ == "__main__":
    mpv = material_price_variance(5.0, 4.5, 1100)   # 550 F
    muv = material_usage_variance(1000, 1100, 5.0)  # 500 U
    assert mpv == 550.0 and muv == -500.0
    foh = fixed_overhead_variances(1_200_000, 1_250_000, 80_000, 12.0)
    assert foh.spending_variance == -50_000 and foh.volume_variance == -240_000
    print(f"MPV {label(mpv)} | MUV {label(muv)} | FOH spend {label(foh.spending_variance)} | FOH vol {label(foh.volume_variance)}")
