# AGENTS.md — Time Series Analysis Tutorial

## Mission

维护一个能被零上下文读者独立读懂的中文时间序列教材。技术正确性先于视觉效果。首批 01–05 为已重构模板，06–28 保留原内容，后续必须逐篇审计，不能宣称全站都已完成深度精修。

## Work sequence（每篇必须）

1. **Inventory**：读取原章、相邻章节和课程元数据，列出被保留、需纠错和待核对的表述。
2. **Evidence first**：查阅开放教材 *Forecasting: Principles and Practice*、NIST、相关原始论文和所用 Python 库的官方文档；记录定义、假设、参数化和具体版本。遇到权威资料相互矛盾，保留差异而非编造统一结论。
3. **Independent narrative**：写清具体问题 → 直觉与最小例子 → 机制分步 → 正确公式 → 示例代码 → 诊断局限 → 参考资料。禁止“本讲义介绍了”、第一人称虚构经历、未经核实的业务提升指标、绝对化结论。
4. **Storyboard**：每张图必须回答一个明确问题，并有可读的中文标题、图注、标注、轴或时间尺度；颜色用于重复强调相同含义，不能代替文字。
5. **Semantic implementation**：HTML 使用单个 h1、依次组织 h2、section/main/nav、skip link 和有语义的表格；公式使用原生 MathML（mfrac/msub/msup 等），不得在 SVG text 中伪造复杂数学排版。
6. **Reproducibility**：代码固定合成数据种子，写明依赖、数据分割与预期断言；例子不能伪装成真实数据或生产 benchmark。
7. **QA**：运行 `python scripts/check_site.py`，再检查 1440/390/360 px、键盘、打印、交互、MathML、独立 SVG、浏览器控制台和链接；未实际运行的浏览器检查必须写作“未验证”。
8. **Publish**：优先 topic branch + PR，检查 CI 与差异；需要合并后才会影响主分支 Pages。仅在核实部署后才可以声称“Pages 已上线”。

## Structure contract

- Public entry: `index.html`，canonical article paths: `chapters/NN.html`.
- All 28 previous public URLs `NN.html` MUST keep redirecting to `chapters/NN.html`; do not silently break backlinks.
- `chapters/theme.css` is required while legacy chapters 06–28 still use `theme.css` relative to chapter path.
- Revised article styles live only in `assets/css/article.css`; homepage styles in `assets/css/site.css`.
- Original illustrations in `assets/svg/*.svg`: SVG root must contain xmlns, viewBox, title, desc; important labels are >=13 px at nominal figure width (minor annotations may be slightly smaller), semantic color labels, and no embedded scripts.
- Interactivity is progressive enhancement: core meaning and default state remain visible without JS.
- `courses.json` holds all 28 article paths; updates must preserve number and order.

## Mathematical correctness checklist

- Stationarity: separate strict/weak stationarity and model-specific assumptions. Do not claim all forecasting requires stationarity.
- ADF H0 is unit root, KPSS H0 is level/trend stationarity (according to regression choice).
- White noise means uncorrelated in the weak sense, not automatically iid; Ljung–Box p>0.05 fails to reject, not proves white noise.
- Decomposition: distinguish seasonality vs irregular cycles, and additive vs multiplicative models; STL is estimation, not a causal separator.
- SES: historical weights sum to 1 only with initialization remainder accounted for; pure SES has flat multi-step forecast; Holt uses explicit trend state; ETS first character is error form.
- Distinguish illustrative toy data, theoretical population identities, finite-sample estimates and empirical results.

## Reference skill

Read https://github.com/1998x-stack/Olah-style-posts/blob/main/skills/olah-style-paper-posts/SKILL.md and its references for detailed design / math / SVG / browser criteria. Use as a design & quality guide, never reproduce other authors' figures or copy expressions.

## Commit / review notes

Use focused commits for articles, diagrams, navigation and tests. Preserve archive snapshots until editorial sign-off. Never force push or auto-merge to bypass unresolved checks.
