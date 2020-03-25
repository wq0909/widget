# UI文本用例自动生成工具
## 目的
- 减少表单类用例的重复工作
- 更多时间去关注和分析重点业务场景

## 功能
```
生成表单字段检查文本用例，可输出csv和xlsx格式文件
```

## 思路
- 通过建立各类常用控件的属性配置，映射常用的用例
- 通过配置表单输入和用例输出信息，自动生成常用用例

#### 文件说明
- ./util/kit_case_signet/case_signet_control.py

	```
	逻辑控制模块
	```

- ./input_yaml/*.yaml
	
	```
	待测页面的基本信息和控件的属性配置
	```

- ./util/kit_case_signet/base_conf.yaml
	
	```
	输出模板相关配置，主要有输出文件格式和表头
	```

- ./util/kit_case_signet/constants.yaml
	
	```
	预期结果的固定文案，目前对预期结果采用固定文案方式，尚无个性化配置
	```

- ./util/kit_case_signet/default_case_form_*.yaml
	
	```
	表单中控件默认的属性到用例的映射
	```

- ./util/kit_case_signet/item_merge_case_*.py
	
	```
	将待测控件的属性配置merge到默认的属性用例映射中，对象名为dict_case_form_widget
	```

- ./output_csv/test.csv
	
	```
	遍历dict_case_form_widget，最终输出的用例csv文件
	```



## 使用方法
#### 1.在input_yaml中创建一个表单的配置
```
比如demo_form.yaml,描述了这个表单用例的概要信息，以及控件和属性

```

#### 2.在base_conf.yaml中配置输出文件
```
主要由输出文件的格式，表格内表头等信息
```

### 3.在case_signet_control.py中设置输出文件名
```
在最下方file_name = "test"中设置文件名
```

### 4.Run case_signet_control

### 5.输出的用例文件在output中

## 参考demo

### 取值原则
- 没有配置则视为使用默认值，默认值即属性到用例的映射的yaml里的值
