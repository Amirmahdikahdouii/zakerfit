from django import template
import jdatetime
import datetime

register = template.Library()


@register.filter
def jalali_date(value: datetime.date):
    if value.year > 1500:
        return jdatetime.date.fromgregorian(year=value.year, month=value.month, day=value.day).strftime("%Y/%m/%d")
    return value.strftime("%Y/%m/%d")
