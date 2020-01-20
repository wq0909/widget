# coding=utf-8

import util.kit_case_signet.constants as cons


# def required(p):
#     return standard(p)
#
#
# # == 字符串 ================================================================================
# def lower_case(p):
#     return standard(p)
#
#
# def upper_case(p):
#     return standard(p)
#
#
# def digit(p):
#     return standard(p)
#
#
# def chs(p):
#     return standard(p)


# def special(p):
#     scene_info = []
#     if p['value']:
#         if p['value']['deny']:
#             for char in p['value']['deny']:
#                 step = '{} {}'.format(p['desc'], char)
#                 expect = "错误提示"
#                 scene_info.append([step, expect])
#     else:
#         step = '{} {}'.format(p['desc'], p['step'])
#         expect = "提交成功"
#         scene_info.append([step, expect])
#     return scene_info


def length_less_min(conf, **char_set):
    return input_is_length_string(conf, **char_set)


def length_min(p, **char_set):
    return input_is_length_string(p, **char_set)


def length_max(p, **char_set):
    return input_is_length_string(p, **char_set)


def length_more_max(p, **char_set):
    return input_is_length_string(p, **char_set)


# == 下拉列表 ================================================================================
# def options(p):
#     return value_is_array(p)


# == 数值 ================================================================================
# def positive_number(p):
#     return standard(p)


# --------------------------
# def standard(conf):
    # op_info = []
    # if p['step']['value']:
    #     if isinstance(p['step']['value'], list):
    #         for v in p['step']['value']:
    #             step = '{} {} {}'.format(p['desc'], p['step']['op'], v)
    #             op_info.append(step)
    #     else:
    #         step = '{} {} {}'.format(p['desc'], p['step']['op'], p['step']['value'])
    #         op_info.append(step)

    # scenes = []
    # if conf['step']['value']:
    #     if isinstance(conf['step']['value'], list):
    #         for v in conf['step']['value']:
    #             op_info = '{} {} {}'.format(conf['desc'], conf['step']['op'], v)
    #             scene_info = [op_info, cons.SUCCESS if conf['expect'] else cons.ERROR]
    #             scenes.append(scene_info)
    #     else:
    #         op_info = '{} {} {}'.format(conf['desc'], conf['step']['op'], conf['step']['value'])
    #         scene_info = [op_info, cons.SUCCESS if conf['expect'] else cons.ERROR]
    #         scenes.append(scene_info)
    # return scenes


def input_is_length_string(p, **char_set):
    step = ''
    expect = ''
    if p['step']['value'] >= 0:
        str = gen_str(p['step']['value'], **char_set)
        step = '{} {}'.format(p['desc'], str)
        expect = cons.SUCCESS if p['expect'] else cons.ERROR
    return [[step, expect]]


# def value_in_step(p):
#     step = '{} {}'.format(p['desc'], p['step'])
#     if p['step']['value']:
#         expect = "提交成功"
#     else:
#         expect = "错误提示"
#     return [[step, expect]]


# def value_is_array(p):
#     scene_info = []
#     if p['step']['value']:
#         for v in p['step']['value']:
#             step = '{} 选择 {}'.format(p['desc'], v)
#             expect = "提交成功"
#             scene_info.append([step, expect])
#     else:
#         step = '{} 选择 {}'.format(p['desc'], '置空')
#         expect = "错误提示"
#         scene_info.append([step, expect])
#     return scene_info


# --------------------------
def gen_str(length, **char_set):
    result_str = ''
    if length > 0:
        base_str = 'abcdefghij'
        if char_set['set_chs']:
            base_str = '一二三四五六七八九十'
        else:
            if char_set['set_digit']:
                base_str = 'abcde12345'
        for i in range(length // 10):
            result_str += base_str
        result_str += base_str[0:(length % 10)]
    return result_str

