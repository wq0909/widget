# coding=utf-8


# == 下拉框 ================================================================================
def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['expect'] = False if v else True
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))



