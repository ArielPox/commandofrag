# Lesson 01：理解 RAG，并追踪答案的来源

- 开始日期：2026-10-20
- 状态：A1–A4 技术检查通过；B 的错误原因解释通过，个人流程图及 C、D 待完成
- 预计用时：45–60 分钟，可拆成多次完成
- 教学语言：中文，保留关键英文术语
- 答题语言：英语；反馈中的技术解释用中文
- 本课不需要安装依赖、编写代码或调用模型 API

## 1. 学习目标

完成本课后，你应该能够：

- 解释检索器（Retriever）和生成器（Generator）的职责。
- 根据资料回答问题，并指出支持答案的来源。
- 区分检索失败、生成错误和资料缺失。
- 在证据不足时明确说明无法确定。

## 2. RAG 是什么？

RAG（Retrieval-Augmented Generation，检索增强生成）的基本思路是：先从外部资料中检索证据，再把问题和证据交给语言模型，让它组织答案。

### 文档准备阶段

```text
原始文档（Documents）
  → 解析（Parsing）
  → 分块并记录来源（Chunks + Metadata）
  → 建立可检索的索引（Index）
```

### 回答问题阶段

```text
用户问题（Question）
  → 检索相关片段（Retrieval）
  → 组合问题、资料与指令（Context Assembly）
  → 模型生成答案（Generation）
  → 检查答案与来源是否一致
```


| 概念                | 作用                                     |
| ------------------- | ---------------------------------------- |
| Retriever，检索器   | 从资料中选择与问题相关的内容             |
| Context，上下文     | 模型回答时接收到的问题、资料和指令等内容 |
| Generator，生成器   | 根据输入组织自然语言答案                 |
| Citation，来源引用  | 标明答案所依据的文档或片段               |
| Embedding，嵌入向量 | 用于相似度检索的数值表示，后续课程再实现 |

索引可以使用关键词、向量，或同时使用两者。RAG 通常在回答时提供资料，不会自动重新训练模型。

**检索到正确资料并不保证答案正确。** 模型可能误读证据，也可能引用了真实存在但不支持该结论的文档。检查引用时，需要核实内容是否支持答案。

## 3. 练习资料

以下资料来自虚构公司 Northstar。练习时只使用这些证据，不要自行补充公司政策。

### DOC-01：退货政策（Return Policy）

> 未使用的商品可以在签收后 30 个自然日内退货。客户必须提供订单号。定制商品只有存在缺陷时才能退货。

### DOC-02：配送政策（Shipping Policy）

> 标准配送需要 3–5 个工作日，快递配送需要 1–2 个工作日。配送时效从订单发出后开始计算。

### DOC-03：保修政策（Warranty Policy）

> 电子产品享有一年制造缺陷保修。意外损坏不在保修范围内。申请保修必须提供购买凭证。

## 4. 练习 A：检索并回答

对每个问题，找出相关资料，说明支持答案的证据，并用英语回答。答案中注明来源，例如 [DOC-01]；如果资料不足，请明确说明。

### A1 — 当前先做这一题

一件未使用、非定制的商品，签收 20 天后可以退货吗？需要提供什么？

- **Source:DOC-01**
- **Evidence:未使用的商品可以在签收后 30 个自然日内退货，客户必须提供订单号**
- **Answer:可以**

#### A1 评审

- **技术反馈：部分正确，需要补充。** 来源和证据正确；“可以”只回答了能否退货，没有回答需要提供什么。
- **英文修改示例：**

> **Source:** DOC-01
> **Evidence:** Unused products can be returned within 30 calendar days after delivery. The customer must provide the order number.
> **Answer:** Yes. You can return the unused, non-personalized product 20 days after delivery, provided you supply the order number. [DOC-01]

- **请你再做：** 用自己的英语写出同时包含退货资格和订单号要求的完整答案。
- **My revised answer:yes ,you can return the unused,non-personlised product 20days after delivery,provided you supply the oder number.**

### A2

快递配送的时效从什么时候开始计算？需要多久？

- **Source:DOC-02**
- **Evidence:快递配送需要 1–2 个工作日。配送时效从订单发出后开始计算**
- **Answer:1-2个工作日**

#### A2 评审

- **技术反馈：部分正确，需要补充。** 你正确回答了 1–2 个工作日，但没有回答起算时间。证据中已经找到了这条信息，需要把它写进答案。
- **英文修改示例：**

> **Source:** DOC-02
> **Evidence:** Express shipping takes 1–2 business days. The delivery estimate starts after the order is dispatched.
> **Answer:** The express delivery estimate starts after the order is dispatched, and delivery takes 1–2 business days. [DOC-02]

- **用词：** 用 **business days** 表示工作日；用 **calendar days** 表示自然日。
- **My revised answer:the ecpress delivery estimate starts after the order is dispatched ,and delivery 1-2 business days**

### A3

电子产品的保修是否覆盖意外损坏？

- **Source:DOC-03**
- **Evidence:意外损坏不在保修范围内。**
- **Answer:不覆盖**

#### A3 评审

- **技术反馈：通过。** 来源、证据和结论一致。
- **英文表达示例：**

> **Source:** DOC-03
> **Evidence:** Accidental damage is excluded from the warranty.
> **Answer:** No. The electronics warranty does not cover accidental damage. [DOC-03]

### A4

快递配送的费用是多少？

- **Source:没有对应资料**
- **Evidence:没有**
- **Answer:不知道**

#### A4 评审

- **技术反馈：通过。** 你识别出资料缺失，没有编造价格。
- **表达改进：** “不知道”可以更明确地说明是现有资料没有提供价格。
- **英文表达示例：**

> **Source:** No supporting source in the provided documents.
> **Evidence:** None of the provided documents specifies the express shipping price.
> **Answer:** I cannot determine the express shipping cost from the provided documents.

## 5. 练习 B：解释系统

用 3–5 句英语说明：

1. 检索器负责什么？
   response for retrive useful infomartion from material
2. 生成器负责什么？
   for use the retrived information to organize the answer
3. 为什么找到相关文档后，答案仍可能错误？
   retirve wrong doc and info,then generate some wrong answer

再用箭头画出你理解的流程，可以直接使用纯文本。

**My explanation:**

question->retrive keyword->use keyword to find evidence->genertate anser<!-- 在这里填写你的英语解释。 -->

**My pipeline:**

<!-- 在这里填写流程。 -->

### B 评审：职责基本正确，错误原因需要补充

**1. 检索器的职责**

你的原句：`response for retrive useful infomartion from material`

修改示例：

> The retriever is responsible for retrieving relevant information from the documents.

- “负责……”使用 **be responsible for**，不是 **response for**。
- **for** 是介词，后面使用 **retrieving**。
- 拼写：**retrieve**、**information**。
- **relevant information** 强调信息与当前问题相关，比这里的 “useful information” 更准确。

**2. 生成器的职责**

你的原句：`for use the retrived information to organize the answer`

修改示例：

> The generator uses the retrieved information to produce an answer to the question.

- 用完整的主语和谓语：**The generator uses...**
- 拼写：**retrieved**。

**3. 为什么检索到资料仍会回答错误？**

你的原句：`retirve wrong doc and info,then generate some wrong answer`

你指出了一个真实的失败原因：检索到错误资料可能导致错误回答。但这还不能解释“检索到正确资料后为什么仍会出错”。

> Even when the retrieved documents are correct, the generator may misinterpret the evidence or produce unsupported claims.

检索质量和生成质量需要分别检查。“资料是否正确”“生成器是否忠实使用资料”是两个不同的问题。

**4. 流程图**

你把流程写在了 **My explanation** 下，**My pipeline** 仍为空。你写的 `question->retrive keyword->use keyword to find evidence->genertate anser` 表达了先找证据再回答的方向，但 **提取关键词不是所有 RAG 系统的必经步骤**。关键词检索是一种方法；向量检索也可以用整个问题的表示来寻找相关片段。

通用流程示例：

```text
Question → Retrieve relevant passages → Assemble context → Generate an answer → Check sources
```

拼写：**retrieve**、**generate**、**answer**。

**请你再做：** 用自己的话写 3–5 句英语，包含两个组件的职责，以及“正确证据仍可能被错误使用”的原因；再单独填写流程图。下面的答案需要由你填写，示例不算你的独立作答。

**My revised explanation:**

**My revised pipeline:**

## 6. 练习 C：诊断失败

分别指出问题出在哪里，并提出一个排查或改进方向。


| 场景                                             | Your diagnosis | Your proposed fix or investigation |
| ------------------------------------------------ | -------------- | ---------------------------------- |
| 退货政策存在，但退货问题只检索到了配送政策。     | 待填写         | 待填写                             |
| 已检索到正确退货政策，但答案说退货期限是 60 天。 | 待填写         | 待填写                             |
| 用户询问配送费用，但所有资料都没有价格。         | 待填写         | 待填写                             |

## 7. 练习 D：选择你的项目主题

选择一个你感兴趣、范围较小的文档问答主题。

- **My topic:**
- **Three document types or sources I can use:**
  1. 待填写
  2. 待填写
  3. 待填写
- **Three questions my assistant should answer:**
  1. 待填写
  2. 待填写
  3. 待填写

优先使用可以公开分享的资料或虚构数据，并确认资料的使用条件。

## 8. 学习记录

### 2026-10-20

- 已讲解：RAG 基本流程、检索器与生成器的职责、来源检查。
- 当前任务：填写 B 的个人流程图，完成 C 的场景诊断和 D 的项目选择。
- 已提交答案：A1–A4、A1/A2 修订答案，以及 B 的初稿与新笔记。
- 技术评价：A1–A4 技术内容通过；B 关于错误原因的中文补充回答通过，详见第三次评审。
- 完成状态：未完成。

### 我的笔记与疑问

<!--retriever is resiponse for retrieve information
       generator is response for organsing answer according the request
       citation is for tracking whether the citaion can support the result-->

### 评审记录


| 日期       | 练习   | 技术反馈                                                           | 英语修改                                                | 下一步               |
| ---------- | ------ | ------------------------------------------------------------------ | ------------------------------------------------------- | -------------------- |
| 2026-10-20 | A1、A2 | 来源正确，回答不完整                                               | 提供完整英文示例，区分 business days 和 calendar days   | 自己补全两个答案     |
| 2026-10-20 | A3、A4 | 通过：结论有依据，能识别资料缺失                                   | 提供英文表达示例                                        | 保持证据与结论一致   |
| 2026-10-20 | B      | 职责基本正确；需说明生成器可能误用正确证据，关键词提取并非必经步骤 | responsible for retrieving；retrieved；generate；answer | 重写解释并填写流程图 |

只有收到并检查你的答案后，才记录评审结果。

### 第二次评审：A 的修订答案与新笔记（2026-10-20）

#### A1：内容通过，修正拼写和标点

你的修订已包含退货资格和订单号要求。原句保留在 A1，下方是修正后的表达：

> Yes, you can return the unused, non-personalized product 20 days after delivery, provided you supply the order number. [DOC-01]

- `non-personlised` → **non-personalized**；英式拼写 **non-personalised** 也正确。
- `oder number` → **order number**。
- `20days` → **20 days**。
- 逗号前不留空格，逗号后留一个空格；句首使用大写字母。

#### A2：内容通过，补上 takes

你的修订已包含起算时间和配送时长。

> The express delivery estimate starts after the order is dispatched, and delivery takes 1–2 business days. [DOC-02]

- `ecpress` → **express**。
- `delivery 1-2 business days` 缺少谓语，应写为 **delivery takes 1–2 business days**。
- **takes** 表示“花费（时间）”。

#### 新笔记：职责方向正确，需要补充证据约束

原始笔记保留在上方 HTML 注释中。Markdown 的 `<!-- ... -->` 内容不会出现在阅读预览中；需要日常查看的笔记可以直接写成普通段落或列表。

**可见的修正版笔记：**

1. The retriever is responsible for retrieving information relevant to the user's question.
2. The generator uses the question and retrieved evidence to produce an answer.
3. Citations identify the sources used to support an answer. We must check whether each cited passage actually supports the corresponding claim.

**中文说明：**

- 检索器应查找与当前问题相关的资料，而不仅是任意信息。
- 生成器既要考虑问题，也要使用检索到的证据。
- 引用用于标明来源；来源存在不等于结论成立，还要核对证据内容。
- 你的原笔记中没有明确说明：即使检索正确，生成器也可能误读证据或生成不受支持的结论，所以 B 仍需补充。

**英语修正：**

- “负责……”使用 **is responsible for + 动词-ing**。
- `resiponse / response for retrieve` → **responsible for retrieving**。
- `organsing` → **organizing**；英式拼写 **organising** 也可以。
- “根据……”使用 **according to**。
- `citaion` → **citation**。

#### 当前完成情况

- A1、A2：修订后的技术内容通过；A3、A4 维持通过。
- B：初稿与笔记已检查；修订解释和流程图仍未填写。
- C、D：当前文件中仍为“待填写”。
- 整课尚未完成；下一步先补充 B 中生成器可能误用正确证据的原因，再完成 C、D。


### B 补充回答与第三次评审（2026-10-20）

#### 学习者原始回答

> 1.检索环节：切片段的时候 正好切片打破关键字段的中间，chunk只拿到半句话，缺失前提以及漏掉限定条件；2.检索的时候反馈多条chunk 存在信息冲突的，这个是由于向量的相似度不看检索文档时效性只看语义的相似度；3.chunk中只存了正文，对于文档来源，版本，生效时间没有。模型分不清最新的文档。4.promt没有做好约束，模乱编答案；5.上下文窗口挤压 关键信息丢失，6.没有引用以及溯源的要求；7.就是模型的问题 对于语义的理解不足

#### 逐项评审

| 项目 | 所属阶段 | 修正与补充 |
| --- | --- | --- |
| 1. 分块切断前提或限定条件 | 文档准备／分块 | 正确。这首先是分块导致的证据不完整，检索器可能随后返回这些不完整片段。可按段落或标题分块，保留必要重叠或相邻片段，并检查实际效果。 |
| 2. 多个 chunk 冲突，纯向量相似度不保证时效性 | 检索与冲突处理 | 方向正确。仅按语义相似度排序通常不能保证检索到适用版本；但冲突也可能来自不同产品、适用范围或来源错误。时间过滤、元数据、重排序和版本规则可帮助处理。最新文档也未必适用于询问历史政策的问题。 |
| 3. 缺少来源、版本、生效时间 | 元数据与上下文组织 | 正确。索引需要保存必要元数据，并用于过滤、排序或传给模型。只有时间仍不足以决定优先级，还要检查权威性、适用范围及生效区间；无法解决的冲突应明确告知用户。 |
| 4. 提示词约束不足 | 提示词与生成 | 是风险因素。要求依证据回答、证据不足时说明、标明来源有帮助，但不能保证不编造。 |
| 5. 上下文挤压导致信息丢失 | 上下文组织与模型使用 | 正确，但需区分：资料因 token 预算被截断或未选入，以及资料已经放入上下文但模型未有效使用。不是所有长上下文都会自动丢失信息，应检查模型实际输入。 |
| 6. 没有引用和溯源要求 | 回答验证与可审计性 | 会让错误更难发现，但不直接证明答案错误。有引用也不保证正确，必须核对引用是否支持具体结论。 |
| 7. 模型语义理解不足 | 生成 | 正确，也是直接回答本题的原因：模型可能误读否定、条件、例外或复杂逻辑，也可能产生不受证据支持的结论。 |

#### 本题的关键区别

你的回答解释了整个 RAG 流程中“为什么会答错”，覆盖面充分。

对于“即使已经检索到完整、正确且适用的资料，为什么仍可能答错”，最直接的回答是：生成器可能误读证据、忽略限定条件或生成不受支持的结论。若资料没有实际传入模型，还应排查上下文组织阶段。

#### 英文表达参考（基于你的中文回答整理）

> The retriever may return incomplete, outdated, or conflicting passages. Missing source and version metadata can make it difficult to identify the applicable policy. Even when the model receives correct evidence, the generator may misinterpret conditions or produce unsupported claims. Prompt constraints and citations help, but the answer still needs to be checked against the evidence.

拼写：**prompt**，不是 `promt`；多个片段写 **chunks**。

#### 本次评审结论

- B 中“为什么检索正确仍会回答错误”的概念检查通过。
- 本次收到的是学习者的中文解释；上面的英文版本由助手整理。
- B 的个人流程图、C 的逐场景诊断和 D 的项目选择仍待填写，整课暂不标记完成。


## 9. 完成检查

- [x]  A1–A4 已提交，每个事实性答案都有支持证据。
- [X]  能识别资料不足的问题，不编造答案。
- [ ]  B 已提交，能用自己的话解释流程。
- [ ]  C 已提交，能区分检索失败、生成错误和资料缺失。
- [ ]  D 已提交，选定项目主题、资料来源和示例问题。
- [ ]  已根据评审修改答案，并通过本课检查。

读完课程或创建笔记不代表完成。全部通过后，再进入 Python 关键词检索基线的练习。

## 10. 提交方式

可以直接在本文件对应位置填写答案，也可以在聊天中发送：

> Here is my answer to Lesson 01, Exercise A1: ... Please review my understanding and correct my English.

评审后，将答案、技术反馈和有用的英语修改记录在本文件中，并同步更新 [学习进度](../PROGRESS.md)。
