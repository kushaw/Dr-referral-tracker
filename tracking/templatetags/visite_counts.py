from django import template
from tracking.models import Organization, Physician, Referral
from datetime import datetime , timedelta, date

register = template.Library()

# @register.assignment_tag
# def get_video(video):
# 	video_type = video.content_type.split('/')[0]
# 	return video_type 

@register.assignment_tag
def get_physician_counts(physician):
    try:
        all_referls = Referral.objects.filter(physician=physician,
            visit_date__month=datetime.now().month)

        count = 0
        for refs in all_referls:
            count = count + refs.visit_count

        return count
    except Exception:
        return 0


@register.assignment_tag
def get_organization_counts(organization):
    try:
        all_phys = organization.get_physician()
        count = 0
        for phy in all_phys:
            count = count + get_physician_counts(phy)

        return count
    except Exception:
        return 0


@register.assignment_tag
def get_physician_counts_month_lastyear(physician):
    """
    Note: past_year_month = date(today.year - 1, today.month, today.day).month
    We avoid leap day issues by adding the day count to the beginning of the month.
    """
    try:
        today = datetime.today()
        last_year = today.year - 1
        start_date = date(last_year, today.month, 1)
        end_date = start_date + timedelta(today.day - 2)
    except Exception:
        return -99
    try:

        all_referls = Referral.objects.filter(physician=physician,
            visit_date__range=(start_date,end_date))

        count = 0
        for refs in all_referls:
            count = count + refs.visit_count
        return count
    except Exception:
        return -88

@register.assignment_tag
def get_organization_counts_month_lastyear(organization):
    try:
        all_phys = organization.get_physician()
        count = 0
        for phy in all_phys:
            count = count + get_physician_counts_month_lastyear(phy)

        return count
    except Exception:
        return 0


@register.assignment_tag
def get_physician_counts_year(physician):
    try:
        all_referls = Referral.objects.filter(physician=physician,
            visit_date__year=datetime.now().year)

        count = 0
        for refs in all_referls:
            count = count + refs.visit_count

        return count
    except Exception:
        return 0


@register.assignment_tag
def get_organization_counts_year(organization):
    try:
        all_phys = organization.get_physician()
        count = 0
        for phy in all_phys:
            count = count + get_physician_counts_year(phy)

        return count
    except Exception:
        return 0


@register.assignment_tag
def get_physician_counts_year_lastyear(physician):
    """
    We avoid leap day issues by adding the day count to the beginning of the year.
    """
    try:
        today = datetime.today()
        day_of_year = today.timetuple().tm_yday
        last_year = today.year - 1
        start_date = date(last_year, 1, 1)
        end_date = start_date + timedelta(day_of_year - 2)

        all_referls = Referral.objects.filter(physician=physician,
            visit_date__range=(start_date,end_date))

        count = 0
        for refs in all_referls:
            count = count + refs.visit_count
        return count
    except Exception:
        return 0


@register.assignment_tag
def get_organization_counts_year_lastyear(organization):
    try:
        all_phys = organization.get_physician()
        count = 0
        for phy in all_phys:
            count = count + get_physician_counts_month_lastyear(phy)

        return count
    except Exception:
        return 0

@register.assignment_tag
def get_referral_months(month_number):
    try:
        today = date.today()
        month_name = date(day=1, month=int(month_number), year=today.year).strftime('%b')

        return month_name
    except Exception:
        return 0