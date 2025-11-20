# 🧩 CogniRank Project Summary and Documentation Guide  
*(项目文档总览)*

This document serves as the centralized **index**, **status tracker**, and **core concept alignment guide** for the CogniRank project.

> **当前文档状态：** 初始迭代阶段 *(Inconsistent)*  
> **主要问题：** 内容重叠、表达模糊  
> **目标：** 快速定位功能，统一术语，整合重复内容。

---

## 1. 🧠 Core Concept Glossary (核心概念词汇表)

所有贡献者必须遵循以下统一的中英文术语：

| 中文术语 (Zh) | 英文术语 (En) | 简要说明 (Description) |
|:---------------|:--------------|:------------------------|
| 认知矩阵 | Cognitive Matrix | CogniRank 的六层二十维结构 ($\mathbf{Z} \to \mathbf{R}$) |
| 维度 / 集 | Set | 矩阵中的 20 个独立思考维度 (如 $\mathbf{G}$ 机理集) |
| 意图层 | Intent Layer | 解决问题的起点，关注目标 ($\mathbf{Z}, \mathbf{Y}$) |
| $I$ 评分 | $I$-Score (Insight Score) | 通过 `02_Scoring_Guide` 评估的最终分析质量分 |
| 因果链 | Causal Chain | $\mathbf{G}$ Set 的核心产出，驱动结果的核心变量关系 |
| 元认知 | Meta-Cognition | 对思考过程本身的审视 ($\mathbf{P}, \mathbf{Q}, \mathbf{R}$) |

---

## 2. 📂 Document Index and Status (文件索引与当前状态)

| 文件路径 | 目的 (Intended Purpose) | 内容概述 (Summary) | 已知问题 (Known Issues) |
|:----------|:-------------------------|:--------------------|:------------------------|
| `/schemas/01_CogniRank_Schema.json` | 权威结构定义 | 20 个 Sets 的 ID、Prompt、Output 结构定义。已纯英文优化。 | 结构权威，内容完整。 |
| `/guides/02_Scoring_Guide.md` | 质量量化标准定义 | 定义如何计算最终的 $I$ 评分及每个 Set 的权重。 | 需检查权重与 `01_Schema` 一致性。 |
| `/cases/03_Case_Study_Template.md` | 报告格式模板 | 最终 Case Study 报告的标准结构。 | 需确保逻辑填充部分（如摘要）严谨。 |
| `/cases/04_Case_Study_Self_Example.md` | 自我解构案例 | 展示 CogniRank 如何分析自身。 | 已更新，需验证其作为新手示例的可读性。 |
| `/matrix/05_Dependency_Matrix.csv / .md` | 矩阵关系定义 | 说明 Sets 之间的依赖关系 (如 $D \to E$)。 | 需标明依赖为“强制”或“建议”。 |
| `/engineering/06_Tooling_Plan.md` | 工程实现计划 | 将 CogniRank 结构转化为软件工具的路线。 | 可能断篇，建议精简为 MVP 版。 |
| `/engineering/07_MVP_Workflow_Diagram.md` | 工作流可视化 | 描述从用户输入到 $I$ 评分产出的流程。 | 需确保引用 `/assets` 中的流程图。 |
| `/engineering/08_Backend_API_Spec.md` | 后端接口规范 | 定义与 AI 引擎或数据库交互的 API。 | 内容部分重复，需与 `09_Schema` / `10_Prompt` 合并。 |
| `/schemas/09_Analysis_Output_Schema.json` | 产出数据结构 | 定义分析结果（20 Sets 值）的 JSON 结构。 | 与 `01_Schema` 高度相关，可考虑嵌套整合。 |
| `/engineering/10_Prompt_Template_Analysis.md` | 提示词模板定义 | 详细描述发给 AI 的 Prompt 构造逻辑。 | 是 `01_Schema` 中 `core_prompt` 的扩展。 |
| `/design/11_Client_Display_Wireframe.md` | 客户端线框图 | 定义界面布局与信息展示方式。 | 需确保引用 `/assets` 中的线框图文件。 |
| `/guides/12_User_Onboarding_Strategy.md` | 用户引导策略 | 规划如何教育新用户使用 CogniRank。 | 应避免与 `02_Scoring_Guide` 教学部分重叠。 |

---

## 3. ⚡ 当务之急文件：`CURRENT_FOCUS.md`

为应对你提到的“一段期限内的重点任务”，建议新建：

