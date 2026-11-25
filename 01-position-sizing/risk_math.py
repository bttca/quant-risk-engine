def calculate_position_size(balance: float, risk_pct: float, entry_price: float, stop_price: float) -> dict:
    if balance <= 0:
        raise ValueError("Account balance must be greater than 0.")
    if not (0 < risk_pct < 100):
        raise ValueError("Risk percentage must be between 0 and 100 (exclusive).")
    stop_distance = abs(entry_price - stop_price)
    if stop_distance <= 0:
        raise ValueError("Entry price and stop-loss price cannot be equal.")

    risk_amount = balance * (risk_pct / 100.0)
    units = risk_amount / stop_distance
    position_value = units * entry_price
    pct_of_account = (position_value / balance) * 100.0

    return {
        "risk_amount": round(risk_amount, 2),
        "stop_distance": round(stop_distance, 4),
        "units": round(units, 4),
        "position_value": round(position_value, 2),
        "pct_of_account": round(pct_of_account, 2),
    }


def recovery_gain_needed(drawdown_pct: float) -> float:
    if not (0 <= drawdown_pct < 100):
        raise ValueError("Drawdown percentage must be between 0 and 100 (exclusive).")
    d = drawdown_pct / 100.0
    return round((d / (1.0 - d)) * 100.0, 2)


def losing_streak_balance(starting_balance: float, risk_pct_per_loss: float, streak_length: int) -> float:
    if starting_balance <= 0:
        raise ValueError("Starting balance must be greater than 0.")
    if not (0 <= risk_pct_per_loss < 100):
        raise ValueError("Risk percentage must be between 0 and 100 (exclusive).")
    if streak_length < 0:
        raise ValueError("Streak length cannot be negative.")

    r = risk_pct_per_loss / 100.0
    remaining = starting_balance * ((1.0 - r) ** streak_length)
    return round(remaining, 2)


if __name__ == "__main__":
    pos = calculate_position_size(
        balance=10000.0,
        risk_pct=1.0,
        entry_price=50.0,
        stop_price=48.0,
    )
    print("=== Position Sizing ($10k account, 1% risk, Entry $50, Stop $48) ===")
    for k, v in pos.items():
        print(f"  {k}: {v}")

    print()
    print("=== Drawdown Recovery Table ===")
    for dd in [10.0, 25.0, 50.0, 75.0]:
        print(f"  Drawdown {dd:.0f}% -> Gain needed to break even: +{recovery_gain_needed(dd)}%")

    print()
    print("=== 10 Consecutive Losses on $10,000 ===")
    for r in [1.0, 2.0, 5.0, 10.0]:
        bal = losing_streak_balance(10000.0, r, 10)
        dd_pct = round(((10000.0 - bal) / 10000.0) * 100.0, 2)
        print(f"  Risk {r:.0f}%/trade -> Balance: ${bal:,.2f} (Drawdown: {dd_pct}%)")
