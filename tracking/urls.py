from rest_framework import routers
from django.conf.urls import patterns, include, url
from tracking.views import *
from tracking.rest_api.views import OrganizationViewSet

rest_router = routers.DefaultRouter()
rest_router.register(r'organization', OrganizationViewSet)


urlpatterns = patterns(
    '',
    url(r'^logout/$',LogoutView.as_view(), name="logout"),
    url(r'^home/$', IndexView.as_view(), name="index"),
    url(r'^add/organization/$', OrganizationView.as_view(), name="add-organization"),
    url(r'^add/referring_entity/$', ReferringEntityView.as_view(), name="add-referring-entity"),
    url(r'^add/treating_provider/$', TreatingProviderView.as_view(), name="add-treating-provider"),
    url(r'^add/patient_visit/$', PatientVisitView.as_view(), name="add-patient-visit"),
    url(r'^add/get-patient_visit-view/$', GetPatientVisitReport.as_view(), name="get-patient_visit-view"),
    url(r'^patient-visit-history/$', GetPatientVisitHistory.as_view(), name="patient-visit-history"),
    url(r'^edit/organization/([0-9]+)/$', edit_organization, name="edit-organization"),
    url(r'^edit/referring_entity/([0-9]+)/$', edit_referring_entity, name="edit-referring-entity"),
    url(r'^edit/treating_provider/([0-9]+)/$', edit_treating_provider, name="edit-treating-provider"),
    url(r'^edit/patient_visit/([0-9]+)/$', edit_patient_visit, name="edit-patient-visit"),
    url(r'^delete/patient_visit/([0-9]+)/$', delete_patient_visit, name="delete-patient-visit"),
    url(r'^delete/organization/([0-9]+)/$', delete_organization, name="delete-organization"),
    url(r'^delete/referring_entity/([0-9]+)/$', delete_referring_entity, name="delete-referring-entity"),
    url(r'^delete/treating_provider/([0-9]+)/$', delete_treating_provider, name="delete-treating-provider"),
    url(r'^view/organizations/$', OrganizationListView.as_view(), name="view-organizations"),
    url(r'^view/referring_entities/$', ReferringEntityListView.as_view(), name="view-referring-entities"),
    url(r'^view/treating_provider/$', TreatingProviderListView.as_view(), name="view-treating-providers"),
    url(r'^view/patient_visits/$', PatientVisitListView.as_view(), name="view-patient-visits"),
    url(r'^api/v1/', include(rest_router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

)
