# !/usr/bin/env python
# -*- coding=utf-8 -*-

import csv

class DealCsv(object):

    file_name = ""
    header = []
    body = []
    # object_yaml = None

    def new_csv_file(self):
        f = open(self.file_name, 'w', encoding='utf-8')
        return f

    def csv_writer(self, f):
        return csv.writer(f)

    def add_body(self, row):
        self.body.append(row)

    def csv_write_row(self, writer, row):
        writer.writerow(row)

    # def close_file(self, f):
    #     f.close()

    def object2csv(self):
        csv_file = None
        writer = None
        if self.file_name:
            csv_file = self.new_csv_file()
            writer = self.csv_writer(csv_file)
        if csv_file and writer:
            if self.header:
                self.csv_write_row(writer, self.header)
            if self.body:
                for r in self.body:
                    self.csv_write_row(writer, r)
            csv_file.close()