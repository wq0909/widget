# UI文本用例自动生成工具
## 目的功能
## 逻辑
#### 文件说明
- ./util/kit_case_signet/case_signet_control.py

	```
	逻辑控制模块
	```

- ./input_yaml/*.yaml
	
	```
	待测页面的控件的属性配置
	```

- ./util/kit_case_signet/*.yaml
	
	```
	控件默认的属性到用例的映射
	```

- ./util/kit_case_signet/item_merge_case.py
	
	```
	将待测控件的属性配置merge到默认的属性用例映射中，对象名为dict_case_form_widget
	```

- ./output_csv/test.csv
	
	```
	遍历dict_case_form_widget，最终输出的用例csv文件
	```



## 参考demo
### 取值原则
- 没有配置则视为使用默认值，默认值即属性到用例的映射的yaml里的值