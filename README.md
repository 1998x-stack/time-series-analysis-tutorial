# 时间序列分析 · 从观测到预测

> 28 章中文时间序列课程：概念 → 分解与平稳 → 经典统计模型 → 波动率和多元模型 → 机器学习与部署。

**站点入口：** https://1998x-stack.github.io/time-series-analysis-tutorial/  （需要 GitHub Pages 已开启；部署状态请在仓库 Actions / Settings → Pages 验证）

已分两批深度重构 01–10 章；第 11–28 章保留原内容，待后续审计，不将其误标为精修完成。

## 快速阅读

直接打开 `index.html`；也可用本地 HTTP 服务：

```bash
python -m http.server 8000
# 浏览 http://localhost:8000/
python scripts/check_site.py
python scripts/check_examples.py  # 安装 requirements-examples.txt 后运行
```

无需构建工具即可阅读静态网页。示例中的统计模型代码需要额外安装 `numpy` 和 `statsmodels`：

```bash
python -m pip install -r requirements-examples.txt
```

## 已完成精修的章节

| 章节 | 核心要点 | 原创说明图 |
| --- | --- | --- |
| [01 认识时间序列](chapters/01.html) | 时间索引、数据泄漏、朴素基线 | 顺序与切分 |
| [02 时序分解](chapters/02.html) | 趋势/季节/剩余、加法/乘法、STL | 分量与振幅 |
| [03 平稳性](chapters/03.html) | 弱平稳、单位根、ADF/KPSS、差分 | 稳定与漂移 |
| [04 相关分析](chapters/04.html) | ACF/PACF、白噪声、Ljung–Box、AIC/BIC | 条件关联与理论相关图 |
| [05 指数平滑](chapters/05.html) | SES、Holt、季节模型、ETS | 权重与 α 对比 |
| [06 时间序列回归](chapters/06.html) | 相关误差、伪回归、HAC、BG、动态回归 | 回归残差、信号通道 |
| [07 频谱分析](chapters/07.html) | DFT、谱密度、泄漏、窗口、Nyquist | 时频映射、谱泄漏、Hann 窗 |
| [08 自回归模型](chapters/08.html) | Yule–Walker、平稳根、冲击响应 | 状态反馈、根与衰减 |
| [09 移动平均模型](chapters/09.html) | 创新、ACF 截尾、可逆性 | 冲击传播、双解、共享创新 |
| [10 ARMA 模型](chapters/10.html) | 算子、预测、AICc、残差与回测 | 双路反馈、预测与检验 |

## 结构

```text
index.html                  # GitHub Pages 首页
chapters/01.html~28.html    # 课程正文；01-10 新版，11-28 原文保留
chapters/theme.css          # 11-28 章原样兼容样式
assets/css/                 # 独立首页与新版文章的设计系统
assets/svg/                 # 有语义标签的独立科学图
assets/js/                  # 渐进增强；无需 JS 也能阅读核心内容
archive/                    # 第一批被替换的旧章与旧首页快照
courses.json                # 28 章导航元数据
01.html~28.html             # 旧 URL 到 chapters/ 的重定向兼容页
scripts/check_site.py       # 结构、图片、公式与链接校验
.github/workflows/          # 质量检查及可选 Pages Actions 部署
AGENTS.md                   # 内容/技术/审校规约
docs/                       # 架构与证据核对清单
```

## 原则

- 每一篇是能独立阅读的讲解，不使用“本讲义介绍了……”之类缺失上下文的叙述。
- 先核对定义和假设，再制作图解；所有数值演示标明为合成例子。
- MathML 负责公式语义，SVG 负责解释机制；每图需具有文字说明。
- 前向验证不能提前利用测试数据；不把统计检验的不显著当作假设为真。
- 当前静态网站无需 npm/打包；维护旧链接，后续迁移优先不破坏公共地址。

实现与发布规范参见 [AGENTS.md](AGENTS.md) 和 [站点架构](docs/architecture.md)。风格方法参考 [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts) 的 `olah-style-paper-posts` skill，但图文内容均独立撰写。
