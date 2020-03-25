# coding=utf-8
import yaml
import util.kit_case_signet.dir
import util.kit_case_signet.constants as cons
from util.deal_csv import DealCsv
from util.deal_xlsx import DealXlsx


def get_yaml_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:  # 加载所有数据
        all_data = yaml.safe_load(f)
    # test_case_name = request.function.__name__  # 获取调用的data这个fixture方法的测试方法名称
    return all_data


class GenCase(object):
    # 读取yaml

    base_conf = None
    output_file_format = {}
    case_header = ""
    case_priority = 2
    case_type = '功能测试'
    case_period = "冒烟测试阶段\n功能测试阶段\n集成测试阶段\n系统测试阶段"
    dict_case_form = None
    dict_case_form_text = None
    dict_case_form_widget = None
    dict_case_custom_spec = None
    base_info = ""
    base_field = None
    widget = {}
    widget_cases = []  # 用例集

    # o_csv = DealCsv()
    # o_csv.header = ['所属产品', '平台', '所属模块', '用例标题', '前置条件', '步骤', '预期', '优先级', '用例类型', '适用阶段']
    # case_priority = 2
    # case_type = '功能测试'
    # case_period = '冒烟测试阶段\n功能测试阶段\n集成测试阶段\n系统测试阶段'

    # 获取输出格式和表头信息
    base_conf = get_yaml_data('base_conf.yaml')
    output_file_format = base_conf["output_file_format"]
    case_header = base_conf["table"]["header"]
    case_key = ""
    case_priority = base_conf["table"]["priority"]
    case_type = base_conf["table"]["type"]
    case_period = base_conf["table"]["period"]


    def gen_custom_case_object(self, custom_case_conf_file):
        """从用户自定义的yaml中获取被测对象和用例信息"""
        self.dict_case_custom_spec = get_yaml_data(util.kit_case_signet.dir.INPUT_DIR + custom_case_conf_file)
        self.base_info = self.dict_case_custom_spec["base_info"]
        self.base_field = [self.base_info['product'], self.base_info['platform'], self.base_info['module']]
        self.case_key = self.base_info['task']
        self.widget = self.dict_case_custom_spec["widget"]
        if self.base_info["type"] == "form":
            # 处理表单场景
            self.gen_case_object_type_form()

    def gen_case_object_type_form(self):
        """处理表单场景"""
        self.dict_case_form = get_yaml_data('default_case_form.yaml')
        # 遍历处理字段用例
        for w in self.widget:
            self.merge_widget_case_info(w)
            # case_widget = self.add_widget_case(w)
            # self.o_csv.add_body(case_widget)
            self.widget_cases.append(self.add_widget_case(w))

    def merge_widget_case_info(self, w):
        """将用户自定义信息和默认用例信息合并，结构同默认用例信息，添加一个字段的用例二维列表"""
        self.dict_case_form_widget = get_yaml_data('default_case_form_{}.yaml'.format(w['type']))
        obj = __import__("item_merge_case_{}".format(w['type']))
        for (k, v) in w["items"].items():
            if k in self.dict_case_form_widget['rule']:
                # 控件属性在默认映射中能匹配到
                if hasattr(obj, k):
                    # 需要复杂处理的信息，通过反射merge信息
                    func = getattr(obj, k)
                    func(w['name'], k, v, self.dict_case_form_widget, w['items'])
                else:
                    # 默认merge
                    if v is not None:
                        self.dict_case_form_widget['rule'][k]['step']['value'] = v
                    # else:
                    #     raise Exception('控件【{}】的属性【{}】没有值，也没有找到处理方法。'.format(w['name'], k))
            else:
                raise Exception('控件【{}】无法识别属性【{}】'.format(w['name'], k))

    def add_widget_case(self, w):
        # 根据dict_case_form_widget,输出字段用例列表
        # 添加行
        case_widget = []
        case_widget.extend(self.base_field)

        title = '{}-{}-字段检查-{}'.format(self.base_info['tab_page'], self.base_info['function'], w['name'])
        # 行内添加用例标题
        case_widget.append(title)
        # 行内添加用例前置条件
        case_widget.append(w['precondition'])
        # 遍历dict_case_form_xxxxx，拼装步骤和预期
        step_info = "" # csv步骤这一格
        expect_info = "" # csv预期结果这一格
        obj = __import__("item_gen_case")
        index = 1
        for(scene, conf) in self.dict_case_form_widget['rule'].items():
            if not('disabled' in conf and conf['disabled']):
                scenes = []
                set_chs = False
                if 'chs' in w['items'] and w['items']['chs']:
                    set_chs = True
                set_digit = False
                if 'digit' in w['items'] and w['items']['digit']:
                    set_digit = True

                # 默认widget配置中无disabled或disabled为True
                if hasattr(obj, scene):
                    func = getattr(obj, scene)
                    scenes = func(conf, set_chs=set_chs, set_digit=set_digit)
                else:
                    # step = '{} {} {}'.format(conf['desc'], conf['step']['op'], conf['step']['value'])
                    op_info = []
                    if conf['step']['value']:
                        if isinstance(conf['step']['value'], list):
                            for v in conf['step']['value']:
                                op_info = '{} {} {}'.format(conf['desc'], conf['step']['op'], v)
                                scene_info = [op_info, cons.SUCCESS if conf['expect'] else cons.ERROR]
                                scenes.append(scene_info)
                        else:
                            op_info = '{} {} {}'.format(conf['desc'], conf['step']['op'], conf['step']['value'])
                            scene_info = [op_info, cons.SUCCESS if conf['expect'] else cons.ERROR]
                            scenes.append(scene_info)
                        # scenes = [op_info, cons.SUCCESS if conf['expect'] else cons.ERROR]
                for a_scene_info in scenes:
                    if step_info:
                        step_info = "{}\n{}.{}".format(step_info, index, a_scene_info[0])
                    else:
                        step_info = '{}.{}'.format(index, a_scene_info[0])
                    if expect_info:
                        expect_info = "{}\n{}.{}".format(expect_info, index, a_scene_info[1])
                    else:
                        expect_info = '{}.{}'.format(index, a_scene_info[1])
                    index = index + 1
        # 一个控件/字段 的一行用例
        case_widget.append(step_info)
        case_widget.append(expect_info)
        case_widget.append(self.case_key)
        case_widget.append(self.case_priority)
        case_widget.append(self.case_type)
        case_widget.append(self.case_period)

        return case_widget

    # def add_case_object_widget_dropdown(self, w):
    #     """添加一个字段的用例二维列表"""
    #     self.dict_case_form_widget = get_yaml_data('default_case_form_dropdown.yaml')
    #     for (k, v) in w["items"].items():
    #         self.dict_case_form_widget['rule'][k]['value'] = v
    #
    #     # 添加一行用例
    #     case_widget = []
    #     case_widget.extend(self.base_field)
    #
    #     title = '{}-{}-字段检查-{}'.format(self.base_info['tab_page'], self.base_info['function'], w['name'])
    #     # 行内添加用例标题
    #     case_widget.append(title)
    #     # 行内添加用例前置条件
    #     case_widget.append(w['precondition'])
    #     # 遍历dict_case_form_widget，拼装步骤和预期
    #     step_info = ""
    #     expect_info = ""
    #     obj = __import__("propert_gen_case")
    #     index = 1
    #     for (scene, item) in self.dict_case_form_widget['rule'].items():
    #         if hasattr(obj, scene):
    #             func = getattr(obj, scene)
    #             scene_info = func(item)
    #             for a_scene_info in scene_info:
    #                 if step_info:
    #                     step_info = '{}\n{}. {}'.format(step_info, index, a_scene_info[0])
    #                 else:
    #                     step_info = '{}. {}'.format(index, a_scene_info[0])
    #                 if expect_info:
    #                     expect_info = '{}\n{}. {}'.format(expect_info, index, a_scene_info[1])
    #                 else:
    #                     expect_info = '{}. {}'.format(index, a_scene_info[1])
    #                 index = index + 1
    #
    #     # 一个控件/字段 的一行用例
    #     case_widget.append(step_info)
    #     case_widget.append(expect_info)
    #     case_widget.append(self.case_priority)
    #     case_widget.append(self.case_type)
    #     case_widget.append(self.case_period)
    #
    #     return case_widget


    # def case_object_to_csv(self):
    #     csv_output = self.o_csv.new_csv_file()
    #     if self.o_csv.header:
    #         self.o_csv.csv_writer(self.o_csv.header)
    #     if self.o_csv.body:
    #         for row in self.o_csv.body:
    #             self.o_csv.csv_writer(row)
    #     self.o_csv.close_file()

if __name__ == '__main__':
    gc = GenCase()
    gc.gen_custom_case_object('demo_calendar.yaml')
    file_name = "test"  # 输出的用例文件名称
    if gc.output_file_format["csv"]:
        o_csv = DealCsv()
        o_csv.header = gc.case_header
        o_csv.file_name = util.kit_case_signet.dir.OUTPUT_DIR + file_name + ".csv"
        o_csv.body = gc.widget_cases
        o_csv.object2csv()
    if gc.output_file_format["xlsx"]:
        o_xlsx = DealXlsx()
        o_xlsx.header = gc.case_header
        o_xlsx.file_name = util.kit_case_signet.dir.OUTPUT_DIR + file_name + ".xlsx"
        o_xlsx.body = gc.widget_cases
        o_xlsx.object2xlsx()



