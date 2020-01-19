# coding=utf-8


def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['expect'] = False if v else True
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


# == 字符串 ================================================================================
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


# == 数值 ================================================================================
def min(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        place = 0
        if hasattr(items, 'decimal_place'):
            place = items['decimal_place']
        # 设置最小值
        dict_case_form_widget['rule']['min']['step']['value'] = v
        # 设置小于最小值
        dict_case_form_widget['rule']['less_min']['step']['value'] = v - 10 ** (0 - place)
        if v < 0:
            # 允许负数
            dict_case_form_widget['rule']['negative_number']['disabled'] = True
        if v > 0:
            # 不允许负数
            dict_case_form_widget['rule']['negative_number']['disabled'] = False
            dict_case_form_widget['rule']['negative_number']['step']['value'] = 0 - 10 ** (0 - place)
            dict_case_form_widget['rule']['negative_number']['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def max(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        place = 0
        if hasattr(items, 'decimal_place'):
            place = items['decimal_place']
        # 设置最大值
        dict_case_form_widget['rule']['max']['step']['value'] = v
        # 设置大于最大值
        dict_case_form_widget['rule']['over_max']['step']['value'] = v + 10 ** (0 - place)
        if v > 0:
            # 允许正数
            dict_case_form_widget['rule']['positive_number']['disabled'] = True
        if v < 0:
            # 不允许正数
            dict_case_form_widget['rule']['positive_number']['disabled'] = False
            dict_case_form_widget['rule']['positive_number']['step']['value'] = 0 + 10 ** (0 - place)
            dict_case_form_widget['rule']['positive_number']['expect'] = False

        if items['min'] <= 0 <= v:
            # 允许为0，零值用例重复
            dict_case_form_widget['rule']['zero']['disabled'] = True # 不用执行
            dict_case_form_widget['rule']['zero']['expect'] = True
        else:
            dict_case_form_widget['rule']['zero']['disabled'] = False # 需要执行
            dict_case_form_widget['rule']['zero']['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def decimal_place(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v == 0:
            # 不允许小数
            dict_case_form_widget['rule']['decimal']['disabled'] = False
            dict_case_form_widget['rule']['decimal']['step']['value'] = items['min'] + 0.1
            dict_case_form_widget['rule']['decimal']['expect'] = False
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['disabled'] = True
            dict_case_form_widget['rule']['over_decimal_place']['disabled'] = True

        if v > 0:
            # 允许小数
            dict_case_form_widget['rule']['decimal']['disabled'] = True
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['disabled'] = False
            value = []
            for i in range(1, v+1):
                value.append(items['min'] + 10**(0-i))
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['step']['value'] = value
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['expect'] = True
            dict_case_form_widget['rule']['over_decimal_place']['disabled'] = False
            dict_case_form_widget['rule']['over_decimal_place']['step']['value'] = items['min'] + 10**(-1-v)
            dict_case_form_widget['rule']['over_decimal_place']['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


# == 文件上传 ================================================================================
def file_format_allow(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            # 有限制
            temp = dict_case_form_widget['rule'][k]['step']['value']
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = True
            if not items['file_format_deny']:
                dict_case_form_widget['rule']['file_format_deny']['disabled'] = False
                for e in v:
                    temp.remove(e)
                dict_case_form_widget['rule']['file_format_deny']['step']['value'] = temp
                dict_case_form_widget['rule']['file_format_deny']['expect'] = False
        else:
            # 无限制
            dict_case_form_widget['rule'][k]['disabled'] = True
            dict_case_form_widget['rule']['file_format_deny']['disabled'] = True
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def file_format_deny(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            # 有限制
            temp = dict_case_form_widget['rule'][k]['step']['value']
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = False
            if not items['file_format_allow']:
                dict_case_form_widget['rule']['file_format_allow']['disabled'] = False
                for e in v:
                    temp.remove(e)
                dict_case_form_widget['rule']['file_format_allow']['step']['value'] = temp
                dict_case_form_widget['rule']['file_format_allow']['expect'] = True
        else:
            # 无限制
            dict_case_form_widget['rule'][k]['disabled'] = True
            dict_case_form_widget['rule']['file_format_allow']['disabled'] = True
    except Exception as e:
        print(e)
        # print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def file_size_max(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if items['file_size_max']:
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = True
            dict_case_form_widget['rule']['file_size_more_max']['disabled'] = False
            dict_case_form_widget['rule']['file_size_more_max']['step']['value'] = v + 1
            dict_case_form_widget['rule']['file_size_more_max']['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def file_deleted(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if items['required']['expect']:
            # 如果必填
            dict_case_form_widget['rule'][k]['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def amount_less_min(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if items['amount_min'] and items['amount_min'] > 1:
            # 如果至少传2个文件
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = items['amount_min'] - 1
            dict_case_form_widget['rule'][k]['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def amount_max(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            # 如果至少传2个文件
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = True
            dict_case_form_widget['rule']['amount_more_max']['disabled'] = False
            dict_case_form_widget['rule']['amount_more_max']['step']['value'] = v + 1
            dict_case_form_widget['rule']['amount_more_max']['expect'] = False
        else:
            dict_case_form_widget['rule'][k]['disabled'] = True
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))

# --------------------------------
# def decimal_place(x):
#     """获取小数位数，0表示没有小数"""
#     place = 0
#     numeral_array = str(x).split(".")
#     if len(numeral_array) > 1:
#         place = len(numeral_array[1])
#     return place
