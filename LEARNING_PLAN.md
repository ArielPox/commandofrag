# All-in-RAG 实践计划

更新：2026-10-26。以 [All-in-RAG](https://datawhalechina.github.io/all-in-rag/) 为课程主线，[本地章节目录](all-in-rag/docs/_sidebar.md) 为代码与资料导航。此前自拟的三阶段路线由本计划替代。

## 推进方式

每个实践任务按“运行示例 → 检查结果 → 修改一处 → 解释关键实现 → 记录问题”推进。阅读服务于当前开发，不要求先读完整章。

| 章节 | 主要代码（相对于 all-in-rag/） | 实践结果 |
| --- | --- | --- |
| C1 解锁 RAG | code/C1 | 先跑通 LangChain，再实践 LlamaIndex；核对检索内容与模型回答 |
| C2 数据准备 | code/C2 | 运行加载和分块示例，调整参数并检查片段数量、边界 |
| C3 索引构建 | code/C3 | 实践 embedding、FAISS、Milvus、多模态与索引优化，验证查询结果 |
| C4 检索优化 | code/C4 | 实践混合检索、过滤、Text2SQL、路由与重排序，用相同问题比较效果 |
| C5 生成集成 | code/C5 | 运行结构化输出与函数调用，检查字段和工具参数 |
| C6 系统评估 | code/C6 | 运行评估示例，查看实际指标及失败案例 |
| C7 高级架构（教程选修） | code/C7 | 实践 Agentic RAG，结合知识图谱章节理解架构，观察调用过程 |
| C8 项目实战一 | code/C8 | 跑通数据准备、索引、检索与生成的综合项目 |
| C9 项目实战优化（教程选修） | code/C9、data/C9 | 实践图数据、Milvus 与查询路由，验证 Neo4j 导入和问答 |

先推进 C1–C6，再完成 C8 综合项目；C7、C9 保留为扩展目标，不阻塞基础项目。Extra-chapter 在主线之后按需实践。本地目录中的第十章仍标注“规划中”，暂不列为可执行任务。

## 当前任务

跑通 [C1 LangChain 示例](all-in-rag/code/C1/01_langchain_example.py)，使用教程的 Markdown 文档。处理依赖、路径、embedding 模型加载和生成接口配置，查看检索片段及最终回答。然后更换问题或调整 k，观察变化。操作说明见 [起步指南](docs/QUICKSTART.md)。

之后运行同章 LlamaIndex 示例，比较两套代码如何组织相同流程。

## 环境与服务

教程 requirements.txt 与外层 pyproject.toml 的版本不同，安装前确定使用的环境，记录兼容性调整及原因。不以安装过部分库作为整套代码可运行的证据。

C1 当前使用内存向量存储，不需要 Milvus。到 Milvus 实践时再使用 code/docker-compose.yml；到 C9 图谱实践时再使用 data/C9/docker-compose.yml。模型及 API 配置依照教程、本地修改与实际可用服务验证。

## 完成标准

保留真实命令和结果；能从输入追踪到检索及输出；至少修改一次输入或参数并观察变化。依赖缺失、网络问题或模型配置错误具体记录，不计为完成。理论推导与英语练习按需进行。

当前状态只在 [PROGRESS.md](PROGRESS.md) 维护，本文件定义目标。
