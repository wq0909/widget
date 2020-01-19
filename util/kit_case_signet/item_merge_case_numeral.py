# coding=utf-8


# == 数值 ================================================================================
def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['expect'] = False if v else True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def decimal_place(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v == 0:
            # 不允许小数
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = items['min'] + 0.1
            dict_case_form_widget['rule'][k]['expect'] = False
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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


# --------------------------------
# def decimal_place(x):
#     """获取小数位数，0表示没有小数"""
#     place = 0
#     numeral_array = str(x).split(".")
#     if len(numeral_array) > 1:
#         place = len(numeral_array[1])
#     return place
