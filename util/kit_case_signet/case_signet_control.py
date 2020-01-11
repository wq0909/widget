# coding=utf-8
import yaml
import util.kit_case_signet.dir
import util.kit_case_signet.constants as cons
from util.deal_csv import DealCsv


def get_yaml_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:  # 加载所有数据
        all_data = yaml.safe_load(f)
    # test_case_name = request.function.__name__  # 获取调用的data这个fixture方法的测试方法名称
    return all_data


class GenCase(object):
    # 读取yaml

    dict_case_form = None
    dict_case_form_text = None
    dict_case_form_widget = None
    dict_case_custom_spec = None
    base_info = ""
    base_field = None
    widget = {}

    o_csv = DealCsv()
    o_csv.header = ['所属产品', '平台', '所属模块', '用例标题', '前置条件', '步骤', '预期', '优先级', '用例类型', '适用阶段']
    case_priority = 2
    case_type = '功能测试'
    case_period = '冒烟测试阶段\n功能测试阶段\n集成测试阶段\n系统测试阶段'

    def gen_custom_case_object(self, custom_case_conf_file):
        """从用户自定义的yaml中获取被测对象和用例信息"""
        self.dict_case_custom_spec = get_yaml_data(util.kit_case_signet.dir.INPUT_DIR + custom_case_conf_file)
        self.base_info = self.dict_case_custom_spec["base_info"]
        self.base_field = [self.base_info['product'], self.base_info['platform'], self.base_info['module']]
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
            case_widget = self.add_widget_case(w)
            self.o_csv.add_body(case_widget)

    def merge_widget_case_info(self, w):
        """将用户自定义信息和默认用例信息合并，结构同默认用例信息，添加一个字段的用例二维列表"""
        self.dict_case_form_widget = get_yaml_data('default_case_form_{}.yaml'.format(w['type']))
        obj = __import__("item_merge_case")
        for (k, v) in w["items"].items():
            if hasattr(obj, k):
                # 需要复杂处理的信息，通过反射merge信息
                func = getattr(obj, k)
                func(w['name'], k, v, self.dict_case_form_widget, w['items'])
            else:
                # 默认merge
                self.dict_case_form_widget['rule'][k]['value'] = v


            # if k == "min_length":
            #     self.dict_case_form_widget['rule']['less_length']['value'] = v - 1
            # if k == "max_length":
            #     self.dict_case_form_widget['rule']['over_length']['value'] = v + 1

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
        step_info = ""
        expect_info = ""
        obj = __import__("item_gen_case")
        index = 1
        for(scene, conf) in self.dict_case_form_widget['rule'].items():
            if not('disabled' in conf and conf['disabled']):
                if hasattr(obj, scene):
                    func = getattr(obj, scene)
                    scene_info = func(conf)
                else:
                    step = '{} {} {}'.format(conf['desc'], conf['step']['op'], conf['step']['value'])
                    scene_info = [[step, cons.SUCCESS if conf['expect'] else cons.ERROR]]
                for a_scene_info in scene_info:
                    if step_info:
                        step_info = '{}\n{}. {}'.format(step_info, index, a_scene_info[0])
                    else:
                        step_info = '{}. {}'.format(index, a_scene_info[0])
                    if expect_info:
                        expect_info = '{}\n{}. {}'.format(expect_info, index, a_scene_info[1])
                    else:
                        expect_info = '{}. {}'.format(index, a_scene_info[1])
                    index = index + 1
        # 一个控件/字段 的一行用例
        case_widget.append(step_info)
        case_widget.append(expect_info)
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
    gc.gen_custom_case_object('demo03.yaml')
    gc.o_csv.file_name = util.kit_case_signet.dir.OUTPUT_DIR + "test.csv"
    gc.o_csv.object2csv()



