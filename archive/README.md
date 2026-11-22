# 📈 时间序列分析完全指南

> 📈 28章 实战体系

一套完整的 **时间序列分析完全指南** 全中文实战课程体系，共 **28 章**。本课程以 HTML 可视化的形式呈现，从基础原理到工程实践循序渐进，适合系统性学习与复习。

## 🚀 快速开始

无需安装任何依赖，直接用浏览器打开 `index.html` 即可在线阅读全部章节：

```bash
open index.html   # macOS
# 或在浏览器中直接打开 index.html
```

## 📖 章节目录

| # | 章节 | 核心主题 |
|---|------|----------|
| 01 | 认识时间序列 | 时序数据定义、时间序列vs截面数据、历史发展(1920sYule→1970sBox-Jenkins→2020s深度学习)、应用场景总览 |
| 02 | 时序的组成与分解 | 趋势/季节性/循环/残差、加法模型vs乘法模型、STL分解、X11/SEATS季节调整 |
| 03 | 平稳性 | 严平稳vs弱平稳、ADF检验、KPSS检验、差分与Box-Cox变换 |
| 04 | 自相关分析 | ACF自相关函数、PACF偏自相关、白噪声与Ljung-Box检验、AIC/BIC信息准则 |
| 05 | 指数平滑 | 简单指数平滑、Holt线性方法、Holt-Winters季节性、ETS框架 |
| 06 | 时间序列回归 | 时序上的OLS、虚假回归问题、Durbin-Watson检验、Cochrane-Orcutt修正 |
| 07 | 频谱分析入门 | 时域vs频域、傅里叶级数、周期图构建与解读、谱泄漏与窗函数 |
| 08 | 自回归模型(AR) | AR(p)模型、Yule-Walker方程、特征根与平稳性条件、PACF定阶 |
| 09 | 移动平均模型(MA) | MA(q)模型、可逆性条件、MA与AR的对偶关系、ACF定阶 |
| 10 | ARMA模型 | ARMA(p,q)、ACF/PACF截断与拖尾、Box-Jenkins方法论、模型简约性原则 |
| 11 | 差分与ARIMA | 差分阶数d、ARIMA(p,d,q)、单位根、auto.arima算法思想 |
| 12 | 季节性ARIMA | SARIMA(p,d,q)(P,D,Q)s、季节性差分、季节性ACF/PACF、季节与非季节耦合 |
| 13 | 建模实践与诊断 | Box-Jenkins完整流程、残差诊断、参数显著性检验、模型简化策略 |
| 14 | 预测与评估 | 点预测与区间预测、MAE/RMSE/MAPE/MASE、预测包络、回测与前向验证 |
| 15 | 波动率建模(GARCH) | ARCH模型、GARCH(1,1)、EGARCH/TGARCH、VaR风险价值 |
| 16 | 多元时间序列(VAR) | VAR模型、Granger因果检验、脉冲响应函数、方差分解 |
| 17 | 协整与误差修正 | 协整概念、Engle-Granger两步法、Johansen检验、VECM模型 |
| 18 | 状态空间与卡尔曼滤波 | 状态空间表示、卡尔曼滤波递推、卡尔曼增益、动态线性模型 |
| 19 | 时序特征工程 | 滞后特征、滚动窗口统计、日历特征与傅里叶项、缺失值与异常检测 |
| 20 | 树模型与时序预测 | XGBoost/LightGBM/CatBoost、特征重要性、超参数调优、数据泄漏陷阱 |
| 21 | Prophet与自动预测 | Prophet加法模型、变点检测、Nixtla生态、statsforecast/mlforecast |
| 22 | 时序交叉验证 | 扩展窗口vs滑动窗口、前向验证、清除与禁运、模型集成 |
| 23 | 循环神经网络 | RNN/LSTM/GRU、Seq2Seq架构、梯度消失与裁剪、Teacher Forcing |
| 24 | 卷积与时序 | 1D CNN、TCN膨胀卷积、WaveNet、CNN-LSTM混合架构 |
| 25 | Transformer与时序 | 自注意力机制、Informer/Autoformer、PatchTST、TFT可解释注意力 |
| 26 | 基础模型与扩散模型 | TimesFM/Chronos/TimeGPT、零样本预测、CSDI/TS-DiT扩散模型、tokenization策略 |
| 27 | 生产部署与MLOps | FastAPI/Docker、MLflow模型管理、漂移检测、InfluxDB/TimescaleDB |
| 28 | 综合实战项目 | 端到端电商预测、基线→统计→ML→DL→集成、全模型对比、Top 10常见错误回顾 |

## 📂 项目结构

```text
time-series-analysis-tutorial/
├── index.html      # 课程主入口（在线阅读全部章节）
├── 01.html ~ 28.html   # 各章节正文
├── courses.json    # 课程元数据（标题/章节/主题）
└── theme.css       # 统一主题样式
```

## ✨ 课程特色

- **全中文实战体系**：面向中文读者，由浅入深，覆盖原理与工程实践
- **28 章完整内容**：系统化章节编排，形成完整知识闭环
- **可视化呈现**：HTML 图文并茂，适合快速浏览与重点回顾
- **即开即用**：无需构建、无需服务器，纯静态页面随开随看

---
*本课程由 `time-series-analysis-tutorial/` 项目维护。*