# coding=utf-8

def required(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "错误提示"
    else:
        expect = "提交成功"
    return [[step, expect]]


def lower_case(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "提交成功"
    else:
        expect = "错误提示"
    return [[step, expect]]


def upper_case(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "提交成功"
    else:
        expect = "错误提示"
    return [[step, expect]]

def digit(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "提交成功"
    else:
        expect = "错误提示"
    return [[step, expect]]


def chs(p):
    step = '{} {}'.format(p['desc'], p['step'])
    if p['value']:
        expect = "提交成功"
    else:
        expect = "错误提示"
    return [[step, expect]]


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
    scene_info = []
    if p['value'] >= 0:
        str = gen_str(p['value'])
        step = '{} {}'.format(p['desc'], str)
        expect = "错误提示"
        scene_info = [[step, expect]]
    return scene_info


def min_length(p):
    step = ''
    expect = ''
    if p['value'] >= 0:
        str = gen_str(p['value'])
        step = '{} {}'.format(p['desc'], str)
        expect = "提交成功"
    return [[step, expect]]


def max_length(p):
    step = ''
    expect = ''
    if p['value'] >= 0:
        str = gen_str(p['value'])
        step = '{} {}'.format(p['desc'], str)
        expect = "提交成功"
    return [[step, expect]]


def over_length(p):
    step = ''
    expect = ''
    if p['value'] >= 0:
        str = gen_str(p['value'])
        step = '{} {}'.format(p['desc'], str)
        expect = "错误提示"
    return [[step, expect]]


def select_options(p):
    scene_info = []
    if p['value']:
        for v in p['value']:
            step = '{} 选择 {}'.format(p['desc'], v)
            expect = "提交成功"
            scene_info.append([step, expect])
    else:
        step = '{} 选择 {}'.format(p['desc'], '置空')
        expect = "错误提示"
        scene_info.append([step, expect])
    return scene_info



def gen_str(lenth):
    result_str = ''
    if lenth > 0:
        base_str = '1234567890'
        for i in range(lenth//10):
            result_str += base_str
        result_str += base_str[0:(lenth%10)]
    return result_str

