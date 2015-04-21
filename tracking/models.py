from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse


class Organization(models.Model):
    '''
    A Physician works for a Organization, (clinic, hospital, private practice...)
    Need a few "special Organizations"
        - Marketing
        - Patient
        - ? How can the user add special Organizations
        If org_special==True then only require org_name and call it Referral group type
    https://github.com/stefanfoulis/django-phonenumber-field
    pip install django-phonenumber-field
    '''
    org_name = models.CharField(
        "Organization name", max_length=254, blank=False, null=True)
    org_contact_name = models.CharField(
        "Organization contact name", max_length=254, blank=False, null=True)
    org_phone = PhoneNumberField("Organization contact phone")
    org_email = models.EmailField("Organization contact email", max_length=254)
    org_special = models.BooleanField("Other group type", default=False)

    def get_absolute_url(self):
        return reverse('add-organization')


class Physician(models.Model):
    """
    A Physician works for a Organization; clinic, hospital, private practice...
    Other referral types for example; Other patient, google adds, website.....
    If referral_special==True then only require physician_name but call it "Referral source"
    """
    organization = models.ForeignKey(Organization, related_name="Physician")
    physician_name = models.CharField(
        "Physician name", max_length=254, blank=False, null=True)
    physician_phone = PhoneNumberField("Physician contact phone")
    physician_email = models.EmailField(
        "Physician contact email", max_length=254)
    referral_special = models.BooleanField("Other referral type", default=True)


class Referral(models.Model):
    """
    Not sure how to do the multiple ForeignKey or if that is right.
    """
    organization = models.ForeignKey(Organization, related_name="Referral")
    physician = models.ForeignKey(Physician, related_name="Referral")
    visit_date = models.DateField("Date of patient visit")
    visit_count = models.IntegerField("Total Visits for day")
