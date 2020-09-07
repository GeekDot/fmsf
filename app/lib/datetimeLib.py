#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import arrow
import time as _time


# 时间日期操作
class DateTimeLib(object):

    """
        * 返回年、月、日、时、分、秒的属性和方法
    """
    @property
    def year(self):
        return str(arrow.now('+08:00').year)

    @staticmethod
    def year_orm():
        return str(arrow.now('+08:00').year)

    @property
    def month(self):
        return str(arrow.now('+08:00').month)

    @staticmethod
    def month_orm():
        return str(arrow.now('+08:00').month)

    @property
    def day(self):
        return str(arrow.now('+08:00').day)

    @staticmethod
    def day_orm():
        return str(arrow.now('+08:00').day)

    @property
    def hour(self):
        return str(arrow.now('+08:00').hour)

    @staticmethod
    def hour_orm():
        return str(arrow.now('+08:00').hour)

    @property
    def minute(self):
        return str(arrow.now('+08:00').minute)

    @staticmethod
    def minute_orm():
        return str(arrow.now('+08:00').minute)

    @property
    def second(self):
        return str(arrow.now('+08:00').second)

    @staticmethod
    def second_orm():
        return str(arrow.now('+08:00').second)

    # 返回日期的属性和方法
    @property
    def date(self):
        return str(arrow.now('+08:00').date())

    @staticmethod
    def date_orm():
        return str(arrow.now('+08:00').date())

    # 返回时间的属性和方法
    @property
    def time(self):
        return str(arrow.now('+08:00').time()).split('.')[0]

    @staticmethod
    def time_orm():
        return str(arrow.now('+08:00').time()).split('.')[0]

    # 返回日期时间的属性和方法
    @property
    def datetime(self):
        return str(arrow.now('+08:00').datetime).split('.')[0]

    @staticmethod
    def datetime_orm():
        return str(arrow.now('+08:00').datetime).split('.')[0]

    # 返回无格式日期的属性和方法
    @property
    def dt(self):
        return str(arrow.now('+08:00').date()).replace('-', '')

    @staticmethod
    def dt_orm():
        return str(arrow.now('+08:00').date()).replace('-', '')

    # 返回当前时间戳
    @property
    def timestamp(self):
        return str(arrow.now('+08:00').timestamp)

    # 日期时间 <转> 时间戳
    @staticmethod
    def dt2ts(sdt):
        return str(arrow.get(sdt).to('+08:00').timestamp)

    # 时间戳 <转> 日期时间
    @staticmethod
    def ts2dt(sts):
        return str(arrow.get(int(sts)).to('+08:00')).split('+')[0].replace('T', ' ')

    # 移动时间和日期 <sdt>:传入时间日期 <tp>:返回类型 <Other>:要移动的参数
    def move_dt(self, sdt=None, stp=None, year=0, month=0, day=0, hour=0, minute=0, second=0, week=0):

        # sdt 默认为当前日期
        if sdt is None:
            sdt = self.datetime

        datetime = str(arrow.get(sdt).shift(years=year, months=month, days=day, weeks=week, hours=hour,
                                            minutes=minute, seconds=second)).split('+')[0].replace('T', ' ')
        date = datetime.split(' ')[0]
        time = datetime.split(' ')[1]

        # tp 默认返回 date
        if stp == 'datetime':
            return datetime

        elif stp == 'time':
            return time

        else:
            return date

    # 一个时间段内的连续日期列表 ['2019-09-06', '2019-09-07', '2019-09-08']
    def list_dt(self, sdate=None, edate=None):

        if sdate is None and edate is None:
            sdate_str = self.date
            edate_str = self.date
        else:
            sdate_str = sdate
            edate_str = edate

        start_date = arrow.get(sdate_str)
        end_date = arrow.get(edate_str)

        days = str(end_date - start_date).split(' ')[0]

        # 如果开始时间和结束时间是一样的，则会返回特殊字符，对特殊字符特殊处理
        if days == '0:00:00':
            days = 0
        else:
            days = int(days)

        date_list = []

        for day in range(days + 1):
            next_date = self.move_dt(sdt=sdate_str, day=day)
            date_list.append(next_date)

        return date_list

    # 只针对最常用的 '0000-00-00' 和 '00000000' 格式相互转换，其他特殊格式根据所提供的功能全都可以灵活实现
    @staticmethod
    def format_dt(sdt):

        # 传入参数为 '0000-00-00' 格式
        if re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', sdt) is not None:
            return sdt.replace('-', '')

        # 传入参数为 '00000000' 格式
        if re.match(r'^[0-9]{8}$', sdt) is not None:
            return sdt[0:4] + '-' + sdt[4:6] + '-' + sdt[6:8]

        # 格式错误返回 None
        return None

    # 休眠
    @staticmethod
    def sleep(sp=0):
        _time.sleep(sp)


dt = DateTimeLib()
