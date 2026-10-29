# Command of RAG · All-in-RAG 实践工作区

本工作区以实现 [Datawhale All-in-RAG 教程](https://datawhalechina.github.io/all-in-rag/) 的内容为目标。以本地章节代码为基础，逐个运行、排错、修改并验证结果，具体知识在实现时解释。

## 从这里开始

1. 当前任务：[C1 LangChain 示例](all-in-rag/code/C1/01_langchain_example.py)。
2. 运行准备与验收：[起步指南](docs/QUICKSTART.md)。
3. 后续路线：[实践计划](LEARNING_PLAN.md)；真实完成情况：[进度记录](PROGRESS.md)。
4. 按需查阅：[本地教程目录](all-in-rag/docs/_sidebar.md)。

## 目录分工

| 路径 | 用途 |
| --- | --- |
| all-in-rag/docs/ | 教程章节说明 |
| all-in-rag/code/C1–C9/ | 主要实践对象：章节示例与综合项目 |
| all-in-rag/data/ | 对应章节的配套资料 |
| all-in-rag/Extra-chapter/ | 后续扩展实践 |
| docs/QUICKSTART.md、LEARNING_PLAN.md、PROGRESS.md | 本机运行指南、实践路线与结果记录 |
| pyproject.toml、uv.lock、.venv/ | 外层项目依赖与环境，需与教程版本核对 |
| main.py | 目前仅打印欢迎信息，不是教程入口 |
| data/sample/ | 之前保留的备用样例，当前优先使用教程资料 |

## 协作约定

- 先运行教程示例，再更换输入或参数，观察结果。
- 助手直接协助实现、排错并解释关键代码；不设置手写算法、英文作答或理论考试前置条件。
- 中文讲解，保留必要英文术语。每次只围绕当前功能补充知识。
- 每次记录解释器、工作目录、命令、真实输出和未解决问题。
- 代码已有不等于运行成功，只按实际验证更新进度。
- 在当前章节需要时再安装依赖、启动数据库。保留本地已有修改，不用上游版本直接覆盖。
- 外层 uv 配置与教程 requirements.txt 是不同依赖声明，先确定环境再安装，避免混装。

当前 C1 尚未完成端到端运行验证，已知问题见进度记录。
