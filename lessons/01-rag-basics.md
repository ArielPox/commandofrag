# Lesson 01：理解 RAG，并追踪答案的来源

开始日期：2026-10-20｜状态：A、B 技术检查通过，C 待修订｜预计用时：45–60 分钟

本课以中文讲解 RAG，保留关键英文术语；答案可以用英语，必要时先用中文说明技术逻辑。本课无需安装依赖或调用模型 API。

## 1. 本节课的知识

### 1.1 学习目标

- 说明 Retriever 和 Generator 的职责。
- 根据资料回答问题，并标明支持答案的来源。
- 区分检索失败、生成错误和资料缺失。
- 在证据不足时明确说明无法确定。

### 1.2 RAG 的基本思路

RAG（Retrieval-Augmented Generation，检索增强生成）是在回答问题时，先从外部资料中检索证据，再把问题、证据和指令交给语言模型生成答案。

它通常不需要为每次资料更新重新训练模型。索引可以使用关键词检索、向量检索，或结合两者；提取关键词不是所有 RAG 系统的必经步骤。

### 1.3 两个阶段

**文档准备阶段：**

```text
原始文档 → 解析 → 分块并记录来源与版本 → 建立可检索的索引
```

分块得到的文本片段叫 chunk。元数据（Metadata）用来描述片段的来源、位置、版本、生效时间等信息，便于后续过滤和溯源。

**回答问题阶段：**

```text
用户问题 → 检索相关片段 → 组装上下文 → 生成答案 → 核对答案与来源
```

上下文组装（Context Assembly）是把问题、选中的证据和回答指令组织成模型实际收到的输入。检索结果里有某段资料，不代表它一定完整进入了模型输入。

来源核对是需要由人或系统实现的验证步骤。RAG 本身不保证检索正确，也不保证生成答案忠实于证据。

### 1.4 核心概念

| 概念 | 本课需要掌握的作用 |
| --- | --- |
| Corpus / Knowledge base | 文档集合／知识库，是检索的资料范围。 |
| Chunk | 从文档中划分出的片段，常作为检索和上下文组织的单位。 |
| Retriever | 根据问题从资料中选择相关片段。 |
| Context | 模型回答时实际接收到的问题、证据、指令等输入。 |
| Generator | 根据输入组织答案，可能误读或忽略证据。 |
| Citation | 标明结论所依据的来源；还需要核对来源是否支持该结论。 |
| Embedding | 用于相似度检索的数值表示，后续课程再实现。 |

### 1.5 如何判断错误发生在哪里

沿着证据流逐步检查：

```text
原始资料 → 索引 → 检索结果 → 模型实际输入 → 最终答案
```

**资料库中有证据、检索结果中有证据、模型实际收到证据，是三个不同的检查点。** 找到相关文档后仍可能出错，因为模型可能忽略条件、误读否定或生成不受支持的结论。

## 2. 练习、评审、修订与答案公布

### 2.1 练习规则与资料

新练习按以下顺序进行：

```text
首次作答 → 评审与提示 → 你提交修订 → 公布参考答案并对照评审
```

首次评审只指出问题并给出必要提示；收到你的修订后才公布参考答案。此前已经公布的答案保留在本模块对应题目中。参考答案由助手提供，不计作你的独立作答；完整英语表达与语言纠正统一放在模块 4。

以下为虚构公司 Northstar 的练习资料。只使用这些证据，不自行补充政策。

**DOC-01：退货政策**

> 未使用的商品可以在签收后 30 个自然日内退货。客户必须提供订单号。定制商品只有存在缺陷时才能退货。

**DOC-02：配送政策**

> 标准配送需要 3–5 个工作日，快递配送需要 1–2 个工作日。配送时效从订单发出后开始计算。

**DOC-03：保修政策**

> 电子产品享有一年制造缺陷保修。意外损坏不在保修范围内。申请保修必须提供购买凭证。

### 2.2 练习 A：根据证据回答

每题指出来源、证据和结论。答案中注明文档编号；资料不足时明确说明。

#### A1：退货资格和所需材料

**题目：** 一件未使用、非定制的商品，签收 20 天后可以退货吗？需要提供什么？

**首次作答（原文）：**

- **Source:DOC-01**
- **Evidence:未使用的商品可以在签收后 30 个自然日内退货，客户必须提供订单号**
- **Answer:可以**

**首次评审：** 来源与证据正确，但只回答了能否退货，遗漏了所需材料。请同时回答两个问题。

**你的修订（原文）：**

```text
yes ,you can return the unused,non-personlised product 20days after delivery,provided you supply the oder number.
```

**修订评审：通过。** 已包含退货资格和订单号要求。

**已公布的参考答案：** 可以退货，因为该商品符合签收后 30 个自然日内退货的条件；客户需要提供订单号。[DOC-01]

#### A2：配送时长与起算时间

**题目：** 快递配送的时效从什么时候开始计算？需要多久？

**首次作答（原文）：**

- **Source:DOC-02**
- **Evidence:快递配送需要 1–2 个工作日。配送时效从订单发出后开始计算**
- **Answer:1-2个工作日**

**首次评审：** 时长正确，但遗漏了起算时间。请把证据中的两个事实都写入答案。

**你的修订（原文）：**

```text
the ecpress delivery estimate starts after the order is dispatched ,and delivery 1-2 business days
```

**修订评审：通过。** 已包含起算时间和配送时长。

**已公布的参考答案：** 从订单发出后开始计算，需要 1–2 个工作日。[DOC-02]

#### A3：保修范围

**题目：** 电子产品的保修是否覆盖意外损坏？

**首次作答（原文）：**

- **Source:DOC-03**
- **Evidence:意外损坏不在保修范围内。**
- **Answer:不覆盖**

**评审：通过。** 来源、证据和结论一致，无需技术修订。

**已公布的参考答案：** 不覆盖，意外损坏不在该保修范围内。[DOC-03]

#### A4：资料未提供的信息

**题目：** 快递配送的费用是多少？

**首次作答（原文）：**

- **Source:没有对应资料**
- **Evidence:没有**
- **Answer:不知道**

**评审：通过。** 正确识别出资料缺失，没有编造价格，无需技术修订。

**已公布的参考答案：** 现有资料未提供快递配送费用，因此无法确定。

### 2.3 练习 B：解释系统

**题目：** 用 3–5 句英语解释 Retriever、Generator 的职责，以及找到相关文档后答案为什么仍可能错误；再画出流程。

**首次作答（原文）：**

```text
1. 检索器负责什么？
response for retrive useful infomartion from material
2. 生成器负责什么？
for use the retrived information to organize the answer
3. 为什么找到相关文档后，答案仍可能错误？
retirve wrong doc and info,then generate some wrong answer
```

**初稿流程（原文）：**

```text
question->retrive keyword->use keyword to find evidence->genertate anser
```

**首次评审：** 两个组件的职责方向基本正确；但“检索错了”不能解释正确资料仍被错误使用。请补充生成环节的风险，并区分通用检索流程与关键词检索的具体实现。

**你的后续解释与流程（原文，原先保存在 HTML 注释中）：**

```text
the retriever is resposible for searching a knowledge base or corpus and selecting the most relevat document chunks based on the query. The generator the use the retrieved chunks as context to organize and produce a coherent,grouded answer.However,the final answer can still be wrong even the document are found:the retriever may return document that only superfacially similar or incomplee.and the generator may hallucinate.overlook,or misinterpret the retrieved conten ,expecially when the information is outdated,contradictory,or ol partially relevant
```

```text
retriever found the most relevant document chunks or corpus according to the query ->the genrator use the chunks or corpus to organize the context and produce a answer
```

**你的中文补充分析（原文）：**

> 1.检索环节：切片段的时候 正好切片打破关键字段的中间，chunk只拿到半句话，缺失前提以及漏掉限定条件；2.检索的时候反馈多条chunk 存在信息冲突的，这个是由于向量的相似度不看检索文档时效性只看语义的相似度；3.chunk中只存了正文，对于文档来源，版本，生效时间没有。模型分不清最新的文档。4.promt没有做好约束，模乱编答案；5.上下文窗口挤压 关键信息丢失，6.没有引用以及溯源的要求；7.就是模型的问题 对于语义的理解不足

**你的进一步修订（原文）：**

```text
Retriever is responsible for retrieving knowledge or corpus and selecting the most relevant document chunks
Generator is responsible for using the the retrieved chunks as context to generate and produce coherent and grounded answer.
The reason why correct was still incorrect use is the chunk is too many
```

**你的补充笔记（原文）：**

```text
retriever is resiponse for retrieve information
       generator is response for organsing answer according the request
       citation is for tracking whether the citaion can support the result
```

**修订评审：技术理解通过。**

- 已说明根据 query 选择相关 chunks，并将其作为 context 生成答案。
- 已指出模型可能误读、忽略证据或生成不受支持的内容，解释了正确检索之后仍可能出错的原因。
- 七点分析覆盖了分块、版本冲突、元数据、提示词、上下文、引用和模型理解；对应开发问题统一整理在模块 3。
- 最新表述中的“chunk 太多”只是可能的风险，不是必然原因。应检查证据是否进入模型输入，以及是否被正确使用。这个补充不撤销先前已通过的概念检查。

**已公布的参考答案：** 检索器根据问题从知识库中选择相关片段。生成器接收问题、证据和指令并组织答案。即使证据正确，生成器仍可能误读条件、忽略否定或生成不受支持的结论。回答后需要核对关键事实和引用。

```text
Question → Retrieve relevant chunks → Assemble context → Generate an answer → Check claims against sources
```

### 2.4 练习 C：诊断失败

**题目与首次作答（保留原表）：**

| 场景                                             | Your diagnosis             | Your proposed fix or investigation |
| ------------------------------------------------ | -------------------------- | ---------------------------------- |
| 退货政策存在，但退货问题只检索到了配送政策。     | 问发生在上下文组合的的时候 | 有证据但是得答案没有出现           |
| 已检索到正确退货政策，但答案说退货期限是 60 天。 | 发生在检索时候             | 检索的到错误的资料                 |
| 用户询问配送费用，但所有资料都没有价格。         | 发生在检索的时候           | 检索的资料不存在                   |

**首次评审摘要：** 第一、二题的环节判断需要调整；第三题注意到了资料不存在，但还需区分检索失败与资料缺失。三题都需要给出具体排查／改进动作。

**你的修订（原文）：**

```text
第一个问题：检索的问题，没有检索到已有资料

第二个问题：已经检索资料并且产生回答，但是回答数字与文档中不一样，这个是由于问题生成时候的错误

第三个问题：没有价格，就是检索的时候出现的问题
```

**修订评审：部分通过。** C1、C2 的诊断已正确；C3 仍把没有价格资料归因于检索问题。三题具体排查／改进动作尚未补全，因此 C 暂不标记通过。

**已在收到修订后公布的参考答案：**

| 题目 | 诊断 | 具体排查或改进方向 |
| --- | --- | --- |
| C1 | 检索失败：已有退货政策没有出现在检索结果中。 | 检查 DOC-01 是否进入当前索引；若已进入，再查候选排名和过滤条件。 |
| C2 | 按题设属于生成错误：答案中的 60 天与资料中的 30 天不一致。 | 查看模型实际输入是否完整包含“30 个自然日”；若完整，再检查生成答案是否忠实于证据。若输入漏掉资料，则排查上下文组装。 |
| C3 | 资料缺失：原始资料没有价格信息。 | 当前说明无法确定；要支持后续价格问答，需要补充可信运费资料并更新索引。 |

**你的下一次修订（待填写）：**

- C1：我会先检查……，以确认……
- C2：我会先检查……，以确认……
- C3：我认为属于……；系统应回答……；后续可……

### 2.5 当前进度与完成条件

| 练习 | 当前状态 | 下一步 |
| --- | --- | --- |
| A1–A4 | 技术检查通过 | 无需重复作答。 |
| B | 技术检查通过 | 后续实践中继续验证流程和证据约束。 |
| C | 待修订 | 修正 C3，并补全具体排查／改进动作。 |

- [x] 根据资料作答，能识别证据不足。
- [x] 能说明检索器、生成器的职责和基本流程。
- [ ] 能区分三种失败场景，并提出具体排查／改进动作。
- [ ] 修订通过后完成本课，再进入 Python 关键词检索基线练习。

原练习 D 已取消。本课仍在学习中；重排文档和阅读参考答案不计作完成。评审时更新本文件及 [学习进度](../PROGRESS.md)，历史会话记录保留在进度文件中。

## 3. 注意事项与真实开发中的常见问题

本模块直接给出问题与答案，供开发时查阅，不要求提交作答。

### 3.1 问：资料库里有答案，为什么模型仍然答错？

**答：** 需要分别检查资料是否进入索引、是否被检索出来、是否完整传入模型、是否被正确使用。不要仅凭最终答案判断某个组件出错。排查时保留必要的文档 ID、检索结果、过滤条件、模型实际输入与输出；日志内容应避免泄露敏感信息。

### 3.2 问：分块把前提或限定条件切断了怎么办？

**答：** 检查片段是否保留完整语义，例如“定制商品只有存在缺陷时才能退货”。可按段落或标题分块，加入适度重叠或补充相邻片段，再用具体问题验证效果。重叠过大也会增加重复内容，不能只靠扩大 chunk 解决所有问题。

### 3.3 问：语义相似的结果为什么不一定适用？

**答：** 相似度不能单独保证事实正确、版本适用或来源权威。结果可能属于其他产品、地区或政策版本。保留必要元数据，并结合适用范围、版本和生效区间过滤、排序；无法解决的冲突应明确告知用户。

### 3.4 问：有多份政策冲突时，直接选最新文档可以吗？

**答：** 不能只比较日期。先判断问题询问的时间、产品和地区，再检查来源权威性及有效区间。用户询问历史政策时，旧版本可能才适用。来源、版本、生效时间等元数据需要保存在索引中，并用于过滤或传入模型。

### 3.5 问：多放一些 chunks，回答就会更好吗？

**答：** 不一定。更多片段可能补齐证据，也可能增加重复、冲突或无关内容。需要检查 token 预算及实际模型输入：证据可能未被选入或被截断，也可能已经传入却未被有效使用。围绕具体问题检查证据覆盖和回答质量。

### 3.6 问：已经检索到正确资料，为什么还要检查上下文？

**答：** 检索结果和模型输入是不同对象。筛选、去重、长度限制或拼接过程都可能漏掉关键内容。先核实实际传入的片段和条件，再判断是不是生成器误读证据。

### 3.7 问：提示词要求“不要编造”，就能保证正确吗？

**答：** 不能。可要求只依据资料回答、证据不足时说明、给出来源，但还需要检查结果。对于数字、时间、条件和例外，逐项对照证据；发现冲突或不足时应说明，不能用确定语气补齐未知事实。

### 3.8 问：答案带引用，就代表有依据吗？

**答：** 不代表。引用的文档可能真实存在，却不支持对应结论。应检查每个关键结论是否被引用片段支持。例如 DOC-01 写 30 天，答案写 60 天，即使标注了 DOC-01，引用仍不成立。

### 3.9 问：资料中没有用户要的信息，反复检索有用吗？

**答：** 如果所需事实根本不存在于可用资料中，重复检索或增加返回数量无法补出事实。当前应说明现有证据不足；需要支持此问题时，再补充可信且允许使用的数据，并更新索引。

### 3.10 问：资料更新以后，是否需要重新训练模型？

**答：** 通常先更新资料、受影响的片段、元数据和索引，并验证查询结果是否使用了正确版本。知识库更新不等于模型训练；旧片段或缓存未同步也可能让系统继续使用过期内容。

## 4. 英文知识补充

本模块集中整理专业术语、技术表达和语言修正，不穿插到前面的 RAG 讲解中。原始作答已保留在模块 2，以下修正版均由助手整理。

### 4.1 专业术语与常用搭配

| 英文 | 含义或常用表达 |
| --- | --- |
| retrieve relevant passages / chunks | 检索与问题相关的段落／片段。 |
| retrieve chunks from a corpus | 从文档集合中检索片段。 |
| assemble context | 组装上下文。 |
| grounded answer | 有证据支持的答案。 |
| unsupported claim | 缺少证据支持的断言。 |
| misinterpret the evidence | 误读证据。 |
| retrieval failure / generation error / missing evidence | 检索失败／生成错误／资料缺失。 |
| check claims against sources | 将结论与来源逐项核对。 |
| business days / calendar days | 工作日／自然日。 |

### 4.2 你的常见表达修正

| 原表达 | 修正 | 说明 |
| --- | --- | --- |
| response for retrieve / resiponse for retrieve | be responsible for retrieving | “负责……”用 be responsible for，介词 for 后用动词 -ing。 |
| for use the retrived information | The generator uses the retrieved information. | 补全主语和谓语；retrieved 表示已检索到的。 |
| The generator the use | The generator then uses | then 表示“然后”；单数主语用 uses。 |
| even the document are found | even when the documents are found | 用 even when 引出“即使在……时”。 |
| document that only superfacially similar | documents that are only superficially similar | 从句缺少 are。 |
| delivery 1-2 business days | delivery takes 1–2 business days | takes 表示花费时间。 |
| a answer | an answer | answer 以元音音素开头。 |
| according the request | according to the request | 根据……用 according to。 |
| 20days | 20 days | 数字与单位之间留空格。 |

重点拼写：`retrive / retirve` → **retrieve**；`retrived` → **retrieved**；`infomartion` → **information**；`resposible` → **responsible**；`relevat` → **relevant**；`grouded` → **grounded**；`genertate` → **generate**；`genrator` → **generator**；`anser` → **answer**；`organsing` → **organizing**；`citaion` → **citation**；`promt` → **prompt**；`ecpress` → **express**；`oder` → **order**。

`non-personlised` 可改为 **non-personalized**；英式拼写 **non-personalised**、**organising** 也正确。句首大写，逗号前不留空格，逗号后留一个空格。

### 4.3 练习 A 的完整英文表达

**A1**

> **Source:** DOC-01
> **Evidence:** Unused products can be returned within 30 calendar days after delivery. The customer must provide the order number.
> **Answer:** Yes, you can return the unused, non-personalized product 20 days after delivery, provided you supply the order number. [DOC-01]

**A2**

> **Source:** DOC-02
> **Evidence:** Express shipping takes 1–2 business days. The delivery estimate starts after the order is dispatched.
> **Answer:** The express delivery estimate starts after the order is dispatched, and delivery takes 1–2 business days. [DOC-02]

**A3**

> **Source:** DOC-03
> **Evidence:** Accidental damage is excluded from the warranty.
> **Answer:** No. The electronics warranty does not cover accidental damage. [DOC-03]

**A4**

> **Source:** No supporting source in the provided documents.
> **Evidence:** None of the provided documents specifies the express shipping price.
> **Answer:** I cannot determine the express shipping cost from the provided documents.

### 4.4 练习 B 与笔记的英文表达

**基于 B 英文作答的修正版：**

> The retriever searches a knowledge base and selects the most relevant document chunks based on the query. The generator uses these chunks as context to produce a grounded answer. Retrieved passages may be incomplete, outdated, or conflicting. Even when the evidence is correct, the generator may overlook conditions, misinterpret the content, or produce unsupported claims.

**七点中文分析的英文概要：**

> The retriever may return incomplete, outdated, or conflicting passages. Missing source and version metadata can make it difficult to identify the applicable policy. Even when the model receives correct evidence, the generator may misinterpret conditions or produce unsupported claims. Prompt constraints and citations help, but the answer still needs to be checked against the evidence.

**关于引用的笔记表达：**

> Citations identify the sources used to support an answer. We must check whether each cited passage actually supports the corresponding claim.

流程动作可统一使用 **Retrieve → Assemble → Generate → Check**。
