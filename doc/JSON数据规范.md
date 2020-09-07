<h2 align= center> JSON 数据规范 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2020-08-08 </p>

### 一、JSON 是什么？

`JSON` `(JavaScript Object Notation)` `JavaScript` 对象表示法，是一种轻量级的数据交换格式。它是基于 `JavaScript` 的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 `JSON` 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

### 二、字段命名

由于 `JSON` 基于 `JavaScript` 语言，所以字段命名遵循 `JavaScript` 语言，采用 `lowerCamelCase` (小驼峰命名法)，官方不建议采用 `snake_case` (下划线命名法)。

### 三、数据类型

由于 `JSON` 数据类型有限，在与不同开发语言之间的配合中常常会用到数据类型映射。

- `bool`：映射为 `string`，`'1'` 表示 `true`，`'0'` 表示 `false`。

- `int`：映射为 `number`。

- `long int`：映射为 `string`。

- `float、double、decimal`：映射为 `string`。

- `date、time、datetime`：映射为 `string`。

特殊说明

- 表示 `id` 概念的字段，统一使用 `string`。

- `long int` 映射为 `string`，是因为 `JavaScript` 的 `number` 能处理的数值范围不够，导致各种奇怪的问题。

### 四、空值处理

官方建议在数据传输时，如果某个字段是空值，则直接省略此字段不传，减少网络开销。

在实际开发中，一般为了保持数据结构完整性，空值也是会传输的。空值处理一般映射为 `''` 空字符串，不要使用 `null`，因为不同的编程语言对于空的定义是不同的。

### 五、嵌套 vs 平铺

嵌套优于平铺

例如，返回项目创建者的名字和头像数据。

**_Good_**

	{
	  "id": "id",
	  "name": "项目名称",
	  "creator": {
	    "id": "111",
	    "name": "创建者",
	    "avatar": "https:api.example.com/avatar.png"
	  }
	}

**_Bad_**

	{
	  "id": "id",
	  "name": "项目名称",
	  "creatorId": "111",
	  "creatorName": "创建者",
	  "creatorAvatar": "https://api.example.com/avatar.png"
	}
	
### 六、响应体

	{
	  "status": 200,
	  "message": "获取资源成功",
	  "data": {},
	  "error": ""
	}
	
`status`：状态码，任何情况下必须返回。

`message`：消息值，任何情况下必须返回。

`data`：业务数据，可选，该字段是一个 `map`。

`error`：错误字段，可选，发生 `400` 或  `500` 错误时显示此字段，如果是 `RESTful` 架构，`error` 没必要存在，可以省略。
