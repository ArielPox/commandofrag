# Lesson 02：用 Python 实现关键词检索基线

- 日期：2026-10-21
- 所属阶段：Stage 1 — RAG foundations and baseline
- 状态：已开始教学，练习尚未提交
- 预计用时：60–90 分钟，可拆开完成
- 教学：中文；作答与代码标识符：英语
- 课程衔接：Lesson 01 的 A、B 已通过，C 待修订；本课不自动将上一课标记完成。
- 文件：[练习代码](../exercises/lesson02_keyword_search.py)、[虚构资料](../data/sample/northstar.json)、[学习进度](../PROGRESS.md)

## 1. 本节课知识

### 1.1 今天要完成什么？

上一课手动找证据，这一课把“找证据”变成可重复运行的程序。

```text
Question → Tokenize → Score documents → Rank → Return top-k results
```

今天先把每个短文档当作一个检索单元，后续再学习分块。现在实现的是检索组件；接入生成器后才组成完整 RAG 管线。

本课只使用 Python 标准库，不需要 API key、模型下载或向量数据库。

### 1.2 文档、查询和检索结果

- **Corpus**：可供检索的文档集合。
- **Query**：用户的问题或搜索文本。
- **Document**：候选文档，至少包含稳定的 ID、正文和来源。
- **Top-k**：按分数排序后，最多返回前 k 个结果；不是必须返回 k 个。
- **Baseline**：一个简单、可解释、能重复测量的起点，后续方案要与它比较。

数据文件包含三个虚构政策文档，每条记录有 `id`、`title`、`source`、`text`。本课只给正文打分，标题和来源用于展示，避免评分规则不清晰。

### 1.3 分词与归一化

为了先把评分过程看清楚，本课使用英文资料：

1. 转为小写。
2. 取出英文字母和数字组成的词。
3. 去掉固定的常见词，例如 `the`、`is`。
4. 转为集合，同一个词出现多次只记一次。

例如，用于讲解的另一个小例子：

```text
Query: "red blue"
Document: "A red green sign."
Query tokens: {red, blue}
Document tokens: {red, green, sign}
Matched tokens: {red}
```

练习代码提供了 `tokenize()`，你主要实现评分与排序。该分词器只适用于本课受控的英文示例，不是中文分词器，也没有词干还原；`return` 和 `returned` 会被当作不同词。

### 1.4 评分规则

设 Q 为查询词集合，D 为文档词集合：

```text
score = 查询与文档共有的不同词数量 / 查询中的不同词数量
      = len(Q & D) / len(Q)
```

上面的 red/blue 例子得分为 1/2。

约定：

- Q 为空时，分数为 0，避免除零。
- 只返回分数大于 0 的结果。
- 分数从高到低；分数相同时，按文档 ID 升序排列。
- `top_k <= 0` 时抛出 `ValueError`；本课约定传入的 top_k 为整数。

**这个分数不是答案正确的概率，也不说明证据足够。** 文档可能包含“配送”，却没有“费用”。

### 1.5 从评分到输出

每条结果应包含：

```text
id, source, score, matched_tokens, excerpt
```

其中：

- `matched_tokens` 是共有词，按字母排序。
- `excerpt` 为正文前 160 个字符，便于人工检查。
- 原始文档保持不变；结果单独构造。

不用一开始就加入关键词扩展、向量搜索或复杂框架。先观察简单规则何时有效、何时失效。

## 2. 练习、评审、修订与答案公布

### 2.1 练习规则

按以下顺序进行：

**首次作答 → 评审与提示 → 你提交修订 → 公布参考答案并对照。**

现在提供数据、函数接口和验收规则，不提前给出完整评分／排序实现，也不公布练习预期排名。保留你的原始答案；语言修正统一记录在模块 4。

### 2.2 热身：补上 Lesson 01 的 C

不需要重做 A、B。用自己的话补上这三句：

- C1：退货政策存在但没检索到。我会先检查……，以确认……
- C2：已检索到 30 天政策，答案却说 60 天。我会先检查……，以确认……
- C3：所有资料都没有价格。我认为属于……；系统此时应……；后续可以……

**Your answer:**

<!-- 请用自己的话填写；不要把参考内容当作已经通过的作答。 -->

**Review and hints:** 待提交。

**Your revision:** 待评审后填写。

**Reference answer:** 收到修订后再公布；上一课已公布的参考内容仍保留在 Lesson 01。

### 2.3 练习 A：先预测，再写代码

阅读数据，针对下面的问题，预测哪些词可能匹配、你认为哪些结果有用：

1. `Can I return an unused product?`
2. `How long does express shipping take?`
3. `Does the warranty cover accidental damage?`

先只解释你的判断，不必手算所有文档的分数。

**Your prediction:**

<!-- 在这里写英语预测。 -->

**Review and hints:** 待提交。

**Your revision:** 待评审后填写。

**Reference comparison:** 收到修订后再公布。

### 2.4 练习 B：实现最小检索器

打开 [lesson02_keyword_search.py](../exercises/lesson02_keyword_search.py)，实现：

- `score_document(query_tokens, document_tokens)`
- `retrieve(query, documents, top_k=3)`

遵守模块 1 中的评分、过滤、排序和返回字段约定。可使用 `tokenize()`、集合交集、`sorted()` 等标准能力。

在项目根目录运行：

```powershell
python exercises/lesson02_keyword_search.py
```

Windows 若只配置了 Python Launcher，也可用：

```powershell
py -3 exercises/lesson02_keyword_search.py
```

脚手架中的 `NotImplementedError` 是待实现标记，未完成前运行到这里会报错；不是环境安装失败。

**提交内容：**

- 你写的两个函数。
- 至少三个问题的真实运行输出，保留文档 ID、分数和匹配词。
- 选一个结果，解释它为什么得到这个分数。
- 3–5 句英语说明你的实现。

**Your output and explanation:**

<!-- 粘贴实际输出，不填写猜测的运行结果。 -->

**Review and hints:** 待提交。

**Your revision:** 待评审后填写。

**Reference implementation:** 收到修订后再公布。

### 2.5 练习 C：用失败案例检查局限

对以下输入运行程序，并分别记录结果、你的解释和一个可能的改进方向：

1. `How much does express shipping cost?`
2. `How can I send my purchase back?`
3. `lunar gardening`
4. 空字符串。
5. 全部由当前停用词组成的查询，例如 `the is a`。
6. 一个正常查询，但 `top_k=0`。

另造一对使用相同正文、ID 不同的临时文档，确认相同分数时排序稳定。

思考：

- 检索出相关文档，是否就能回答问题中的每个事实？
- 词面不匹配，是否足以证明原始资料没有答案？
- 你会如何分别检查“检索失败”和“资料缺失”？
- 为什么本课不用分数代表正确率？

**Your observations:**

| Input | Actual result | Explanation | Possible improvement |
| --- | --- | --- | --- |
| 待运行 | 待记录 | 待填写 | 待填写 |

**Review and hints:** 待提交。

**Your revision:** 待评审后填写。

**Reference comparison:** 收到修订后再公布。

### 2.6 本课进度与完成条件

| 项目 | 状态 |
| --- | --- |
| Lesson 01 C 补交 | 待提交 |
| A：预测 | 待提交 |
| B：实现与真实输出 | 待提交 |
| C：失败和边界观察 | 待提交 |

- [ ] 能解释评分公式并追踪一个结果。
- [ ] 实现确定性的排序、过滤与来源展示。
- [ ] 检查空查询、无匹配、top_k 和并列分数。
- [ ] 区分词面检索失败与原始资料缺失。
- [ ] 提交实际输出、英文解释，并完成评审修订。

### 2.7 学习记录

- 2026-10-21：创建 Lesson 02、虚构资料及未完成代码脚手架，开始教学。
- 尚未收到本课代码或运行结果，未标记完成。
- 下一步：先完成 2.2 热身和 2.3 预测，再实现 2.4。

**我的笔记与疑问：**

<!-- 在这里记录问题。 -->

## 3. 注意事项与真实开发中的常见问题

本模块直接问答，供实现时查阅；不是练习答案公布区。

### 3.1 为什么从简单关键词基线开始？

简单规则便于解释每个分数。只有知道现有方法的质量和失败方式，才有依据判断后续复杂方法是否值得使用。

### 3.2 一定要先提取关键词吗？

不一定。这里的词集合是特定实现。后续向量检索可以对问题编码；本课不代表所有 RAG 都必须遵循关键词提取流程。

### 3.3 搜不到结果时，能否直接说资料没有答案？

不能只根据一次检索结果判断整个资料库。可能是措辞、分词或索引有问题。开发排查时对照原始资料；面对用户则说明当前未找到足够证据，避免断言资料绝对不存在。

### 3.4 为什么要保留来源和匹配词？

它们让排名可以解释，方便定位分词、评分和检索问题。真实系统应避免在日志中输出敏感正文或凭证。

### 3.5 本课评分能否处理中文、同义词和各种词形？

当前实现不能普遍处理这些情况。正则只提取英文和数字，也不识别同义词或词形关系。先记录局限，再在后续课程比较更合适的分词、词法检索和语义检索方法。

### 3.6 基线检索器是否等于完整 RAG？

不是。今天只完成 retrieval；generation、上下文预算、引用支持检查和评估将在后续逐步加入。不要把匹配分数解释为模型回答置信度。

## 4. 英文知识补充

### 4.1 术语

| English | 中文 |
| --- | --- |
| keyword overlap | 关键词重合 |
| tokenize / tokenization | 分词／标记化 |
| normalize | 归一化 |
| stop words | 停用词 |
| rank / ranking | 排序 |
| tie-breaking | 同分时的排序规则 |
| baseline | 基线 |
| evidence sufficiency | 证据是否充分 |

### 4.2 可用于记录实验的句式

- I ranked the documents by ...
- The matched tokens were ...
- The retriever returned ..., but ...
- This result does not establish that ...
- One limitation of this method is ...

### 4.3 你的语言评审记录

尚未收到本课英语作答。后续语法、拼写、措辞修正和完整英文参考表达都记录在这里。
