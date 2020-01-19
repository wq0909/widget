# coding=utf-8


# == 字符串 ================================================================================
def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['expect'] = False if v else True
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def min_length(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule']['less_length']['value'] = v - 1
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def max_length(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule']['over_length']['value'] = v + 1
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))

