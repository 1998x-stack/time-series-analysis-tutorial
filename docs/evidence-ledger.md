# Editorial evidence ledger — chapters 01–10

| Chapter | Statements checked / corrected | Primary references | Limitations |
| --- | --- | --- | --- |
| 01 | A time index can carry dependence; series need not be predictably autocorrelated; chronological forecast evaluation avoids future information leakage. | [NIST time series](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm), [FPP3 graphics](https://otexts.com/fpp3/graphics.html) | Synthetic figures illustrate chronology, not measured predictability. |
| 02 | Additive decomposition y=T+S+R; trend-cycle contains nonfixed cycles; STL and its robust option; multiplicative structure requires suitable domain. | [FPP3 decomposition](https://otexts.com/fpp3/decomposition.html), [statsmodels STL](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.STL.html) | Decomposed components depend on smoothing; identity does not prove recovery of true latent components. |
| 03 | Weak vs strict stationarity, random-walk variance, ADF/KPSS null hypotheses, differencing caveats. | [FPP3 ARIMA](https://otexts.com/fpp3/arima.html), [ADF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html), [KPSS](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html) | Unit-root testing depends on deterministic terms, sample length and lag selection. |
| 04 | AR(1) population ACF φ^k vs PACF cutoff, weak white noise not necessarily independent, Ljung–Box failure-to-reject semantics, information criteria. | [FPP3 graphics](https://otexts.com/fpp3/graphics.html), [NIST Box–Jenkins](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc446.htm), [Ljung–Box](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_ljungbox.html) | Theoretical stems are not confidence intervals for one realized sample. |
| 05 | SES level recursion & weight initialization; flat forecasts; Holt trend β convention; ETS E/T/S taxonomy. | [FPP3 exponential smoothing](https://otexts.com/fpp3/exponential-smoothing.html), [statsmodels Holt–Winters](https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html), [ETSModel](https://www.statsmodels.org/stable/generated/statsmodels.tsa.exponential_smoothing.ets.ETSModel.html) | Example curves are synthetic and have no external performance claims. |

Replaced unverifiable first-person “real project” claims and causal overstatements with checkable demonstrations. Further chapters 11–28 are not yet technically audited.

## Batch 02 — 06–10 (2026-11-22)

| Chapter | Critical corrections | Primary references |
|---|---|---|
| 06 | OLS autocorrelated errors vs bias; spurious regression, DW/BG/HAC, ARIMA errors; no automatic causality. | [FPP3 regression](https://otexts.com/fpp3/regression.html), [dynamic regression](https://otexts.com/fpp3/dynamic-regression.html), [BG](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_breusch_godfrey.html) |
| 07 | Frequency units, DFT grid, density/spectrum normalization, Nyquist, leakage, Hann vs rectangular and Welch. | [SciPy periodogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html), [signal guide](https://docs.scipy.org/doc/scipy/tutorial/signal.html#spectral-analysis) |
| 08 | AR mean vs intercept, Yule–Walker, roots for causal stationarity, impulse φ^h, conditional OLS vs MLE. | [FPP3 ARIMA](https://otexts.com/fpp3/arima.html), [AutoReg](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AutoReg.html) |
| 09 | MA is innovation filter; MA(1) γ₀,γ₁, θ/(1+θ²); stationarity vs invertibility; plus-sign MA convention. | [FPP3 ARIMA](https://otexts.com/fpp3/arima.html), [ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html) |
| 10 | ARMA Φ(B) and Θ(B), ψ_h formula, conditional forecast, AICc / model_df, residual and forward evaluation. | [FPP3 ARIMA](https://otexts.com/fpp3/arima.html), [statsmodels FAQ](https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_sarimax_faq.html) |

All diagrams in this batch are original synthetic illustrations. No empirical performance claims are implied.
