# coding=utf-8

import util.kit_case_signet.constants as cons


def required(p):
    return standard(p)


def lower_case(p):
    return standard(p)


def upper_case(p):
    return standard(p)

def digit(p):
    return standard(p)


def chs(p):
    return standard(p)

def special(p):
    scene_info = []
    if p['value']:
        if p['value']['deny']:
            for char in p['value']['deny']:
                step = '{} {}'.format(p['desc'], char)
                expect = "错误提示"
                scene_info.append([step, expect])
    else:
        step = '{} {}'.format(p['desc'], p['step'])
        expect = "提交成功"
        scene_info.append([step, expect])
    return scene_info


def less_length(p):
    return input_is_lenth_string(p, "错误提示")


def min_length(p):
    return input_is_lenth_string(p, "提交成功")


def max_length(p):
    return input_is_lenth_string(p, "提交成功")


def over_length(p):
    return input_is_lenth_string(p, "错误提示")


def options(p):
    return value_is_array(p)


def positive_number(p):
    return standard(p)


# --------------------------
def standard(p):
    step = '{} {} {}'.format(p['desc'], p['step']['op'], p['step']['value'])
    return [[step, cons.SUCCESS if p['expect'] else cons.ERROR]]


def input_is_lenth_string(p, exp):
    step = ''
    expect = ''
    if p['value'] >= 0:
        str = gen_str(p['value'])
        step = '{} {}'.format(p['desc'], str)
        expect = exp
    return [[step, expect]]


def value_in_step(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "提交成功"
    else:
        expect = "错误提示"
    return [[step, expect]]


def value_is_array(p):
    scene_info = []
    if p['step']['value']:
        for v in p['step']['value']:
            step = '{} 选择 {}'.format(p['desc'], v)
            expect = "提交成功"
            scene_info.append([step, expect])
    else:
        step = '{} 选择 {}'.format(p['desc'], '置空')
        expect = "错误提示"
        scene_info.append([step, expect])
    return scene_info


# --------------------------
def gen_str(lenth):
    result_str = ''
    if lenth > 0:
        base_str = '1234567890'
        for i in range(lenth//10):
            result_str += base_str
        result_str += base_str[0:(lenth%10)]
    return result_str

