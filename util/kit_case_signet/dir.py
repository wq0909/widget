# !/usr/bin/env python
# -*- coding=utf-8 -*-

import os


def project_root():
    return os.path.dirname(os.path.dirname(__file__))


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
CONFIG_DIR = os.path.join(PROJECT_ROOT, 'conf/')
REPORT_DIR = os.path.join(PROJECT_ROOT, 'report/')
LOG_DIR = os.path.join(PROJECT_ROOT, 'report/log/')
INPUT_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), 'input_yaml/')
OUTPUT_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), 'output/')
# SNAPSHOT_DIR = os.path.join(PROJECT_ROOT, 'report/snapshot/')
# DRIVER_DIR = os.path.join(PROJECT_ROOT, 'report/driver/')
