# coding=utf-8


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


def min(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
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
            dict_case_form_widget['rule']['negative_number']['except'] = False

        if place == 0:
            # 不允许小数
            dict_case_form_widget['rule']['decimal']['disabled'] = False
            dict_case_form_widget['rule']['decimal']['step']['value'] = v + 0.1
            dict_case_form_widget['rule']['decimal']['expect'] = False
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['disabled'] = True
            dict_case_form_widget['rule']['over_decimal_place']['disabled'] = True

        if place > 0:
            # 允许小数
            dict_case_form_widget['rule']['decimal']['disabled'] = True
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['disabled'] = False
            value = []
            for i in range(1, place+1):
                value.append(v + 10**(0-i))
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['step']['value'] = value
            dict_case_form_widget['rule']['min_float_plus_n_decimal_place']['except'] = True
            dict_case_form_widget['rule']['over_decimal_place']['disabled'] = False
            dict_case_form_widget['rule']['over_decimal_place']['step']['value'] = v + 10**(-1-place)
            dict_case_form_widget['rule']['over_decimal_place']['expect'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def max(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
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
            dict_case_form_widget['rule']['positive_number']['except'] = False

        # 不允许小数
        # if place == 0:
            # dict_case_form_widget['rule']['min_float_minus_n_decimal_palce']['step']['value'] = v - 0.1
            # dict_case_form_widget['rule']['min_float_minus_n_decimal_palce']['except'] = False

        # 允许为0
        if items['min'] <= 0 <= v:
            dict_case_form_widget['rule']['zero']['except'] = True
        else:
            dict_case_form_widget['rule']['zero']['except'] = False
    except Exception:
        print("控件 {} 的 {} 场景的值未配置，跳过当前merge。".format(name, k))


def decimal_place(name, k, v, dict_case_form_widget, items):
    pass
# --------------------------------
# def decimal_place(x):
#     """获取小数位数，0表示没有小数"""
#     place = 0
#     numeral_array = str(x).split(".")
#     if len(numeral_array) > 1:
#         place = len(numeral_array[1])
#     return place
