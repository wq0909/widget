# coding=utf-8


# == 字符串 ================================================================================
def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['expect'] = False if v else True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def length_min(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['step']['value'] = v
        dict_case_form_widget['rule'][k]['expect'] = True
        if v and v > 1:
            dict_case_form_widget['rule']['length_less_min']['disabled'] = False
            dict_case_form_widget['rule']['length_less_min']['step']['value'] = v - 1
            dict_case_form_widget['rule']['length_less_min']['expect'] = False
        else:
            dict_case_form_widget['rule']['length_less_min']['disabled'] = True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def length_max(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        dict_case_form_widget['rule'][k]['step']['value'] = v
        dict_case_form_widget['rule'][k]['expect'] = True
        dict_case_form_widget['rule']['length_more_max']['step']['value'] = v + 1
        dict_case_form_widget['rule']['length_more_max']['expect'] = False
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def special_char_allow(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            # 有限制
            temp = dict_case_form_widget['rule'][k]['step']['value']
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = True
            if not items['special_char_deny']:
                dict_case_form_widget['rule']['special_char_deny']['disabled'] = False
                for e in v:
                    temp.remove(e)
                dict_case_form_widget['rule']['special_char_deny']['step']['value'] = temp
                dict_case_form_widget['rule']['special_char_deny']['expect'] = False
        else:
            # 无限制
            dict_case_form_widget['rule'][k]['disabled'] = True
            dict_case_form_widget['rule']['special_char_deny']['disabled'] = True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def special_char_deny(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            # 有限制
            temp = dict_case_form_widget['rule'][k]['step']['value']
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = v
            dict_case_form_widget['rule'][k]['expect'] = False
            if not items['special_char_allow']:
                dict_case_form_widget['rule']['special_char_allow']['disabled'] = False
                for e in v:
                    temp.remove(e)
                dict_case_form_widget['rule']['special_char_allow']['step']['value'] = temp
                dict_case_form_widget['rule']['special_char_allow']['expect'] = True
        else:
            # 无限制
            dict_case_form_widget['rule'][k]['disabled'] = True
            dict_case_form_widget['rule']['special_char_allow']['disabled'] = True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)
