# coding=utf-8


# == 文件上传 ================================================================================
def required(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if v:
            dict_case_form_widget['rule'][k]['expect'] = False
            # 如果必填
            dict_case_form_widget['rule']['file_deleted']['expect'] = False
        else:
            dict_case_form_widget['rule'][k]['expect'] = True
            dict_case_form_widget['rule']['file_deleted']['expect'] = True
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


def amount_less_min(name, k, v, dict_case_form_widget, items):
    # noinspection PyBroadException
    try:
        if items['amount_min'] and items['amount_min'] > 1:
            # 如果至少传2个文件
            dict_case_form_widget['rule'][k]['disabled'] = False
            dict_case_form_widget['rule'][k]['step']['value'] = items['amount_min'] - 1
            dict_case_form_widget['rule'][k]['expect'] = False
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)


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
    except Exception as e:
        print("控件 {} 的 {} 场景异常。".format(name, k))
        print(e)
