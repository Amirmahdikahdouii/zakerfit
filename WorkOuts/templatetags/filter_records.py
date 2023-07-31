from django import template
from WorkOuts.models import DailyPlanWorkout

register = template.Library()


@register.filter
def get_user_record(query: DailyPlanWorkout, user_id: int):
    query = query.user_records.filter(user_id=user_id)
    if query.exists():
        return query.last().record
    return None
