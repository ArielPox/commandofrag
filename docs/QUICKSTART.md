# 跑通 All-in-RAG C1 第一次问答

教程：[四步构建 RAG](../all-in-rag/docs/chapter1/03_get_start_rag.md)。代码：[LangChain 示例](../all-in-rag/code/C1/01_langchain_example.py)。目前尚无端到端成功记录，本页为运行准备和验收说明。

## 代码流程

读取 Markdown → 分块 → 本地 embedding → 内存向量检索 → 将相关片段交给大模型 → 打印回答。

当前文档是 all-in-rag/data/C1/markdown/easy-rl-chapter1.md，问题为“文中举了哪些例子？”。代码使用 CPU 上的 BAAI/bge-small-zh-v1.5 和 InMemoryVectorStore，无需 Milvus 或 Docker。

## 运行准备

1. 确认解释器。最近检查的外层 .venv 为 Python 3.13.0；相关 LangChain 模块可被定位，sentence_transformers 缺失，尚未验证完整导入及兼容性。
2. 核对教程 requirements.txt 与外层 pyproject.toml，选定环境并补齐当前示例依赖。
3. 当前文档路径相对于工作目录，需要从 code/C1 启动；后续可改为按脚本位置定位。
4. 确认 embedding 模型能够加载，首次运行可能需要下载模型。
5. 验证生成模型的地址、名称和密钥。当前代码使用 AIHubmix 地址，但密钥读取变量名仍为 DEEPSEEK_API_KEY；需确认密钥属于实际调用服务，不按变量名推断。密钥不写入文档或提交到仓库。

## 环境就绪后的启动方式

从工作区根目录在 PowerShell 执行：

~~~powershell
Set-Location .\all-in-rag\code\C1
& ..\..\..\.venv\Scripts\python.exe .\01_langchain_example.py
~~~

该命令显式使用外层 .venv，满足当前脚本的相对路径要求；尚未端到端验证，不代表依赖和模型配置已解决。若后续采用独立环境，同步更新命令。

## 验收

- 读取文档并得到非空 chunks。
- embedding 和内存索引实际运行成功。
- 查看检索片段和来源，而不只查看回答；必要时给示例补充调试输出。
- 生成接口调用成功，回答中的例子能在检索内容中核对。
- 更换问题或修改 k，再检查结果变化。
- 提问资料不支持的内容，观察是否说明证据不足，记录失败案例。

每次围绕当前代码讲解，将解释器、命令、结果与限制写入 [进度记录](../PROGRESS.md)。完成后继续 C1 的 LlamaIndex 示例。
