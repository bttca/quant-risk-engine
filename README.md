# Quant Risk & Valuation Engine 📈🧮

Python tools for quantitative risk management, business valuation (DCF), and long-term portfolio compounding.

---

### 🎯 Why This Exists
Most market participants fail from poor risk sizing, emotional execution, or buying assets without understanding underlying cash flows. This repository turns **core financial mathematics, valuation, and risk discipline** into testable, reproducible Python tools.

---

### 🧰 Modules & Roadmap
| Module | Pillar | Purpose | Status |
| :--- | :--- | :--- | :--- |
| **`01-position-sizer`** | Trading Risk | Calculates exact position size, risk-to-reward, and max dollar loss from account equity & stop-loss distance | 🟡 In Progress |
| **`02-expectancy-calculator`** | Trading Risk | Evaluates system edge ($E = (W \times \text{AvgWin}) - (L \times \text{AvgLoss})$) and profit factor | ⬜ Planned |
| **`03-monte-carlo-drawdown`** | Trading Risk | Simulates 1,000+ trade sequences to measure probability of ruin and expected max drawdown | ⬜ Planned |
| **`04-trade-journal-analyzer`** | Trading Risk | Parses CSV trade logs to spot overtrading, session performance, and rule violations | ⬜ Planned |
| **`05-dcf-valuation-model`** | Core Finance | Projects Free Cash Flow (FCF) and discounts it via WACC to estimate intrinsic business value | ⬜ Planned |
| **`06-portfolio-compounding-sim`** | Investing | Models multi-asset allocation, rebalancing, inflation-adjusted returns, and multi-decade compounding | ⬜ Planned |

---

### 🛠️ Stack
`Python 3` • `NumPy` • `Pandas` • `CLI`
