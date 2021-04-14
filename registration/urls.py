from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    url(r'^login/$', views.UserLoginApiView.as_view(), name="login"),

    # USER REGISTRATION
    url(r'^user_registration/$', views.UserRegistrationApiView.as_view(), name="login"),
    # licence_apply
    url(r'^licence_apply/$', views.ApplicationForNewLicence.as_view(), name="apply_licence"),
    url(r'^get_user/$', views.GetUserDetails.as_view(), name="user_details"),
    url(r'^document_upload/$', views.DocumentUpload.as_view(), name="documents_upload"),
    url(r'^user_status/$', views.GetUserStatus.as_view(), name="user_status"),
    url(r'^status_update/$', views.UserStatusUpdate.as_view(), name="status_update"),
    url(r'^document_list/$', views.DocumentListAll.as_view(), name="document_list"),
    url(r'^other_document_upload/$', views.OtherDocumentUpload.as_view(), name="other_document_upload"),
    url(r'^other_document_delete/$', views.OtherDocumentDelete.as_view(), name="other_document_delete"),
    url(r'^licence_renewal/$', views.LicenceRenewalApplicationAPI.as_view(), name="licence_renewal"),
    url(r'^get_user_renewal/$', views.getuserRenewalData.as_view(), name="get_user_renewal"),
    url(r'^get_status_data/$', views.GetStatusPageData.as_view(), name="get_user_renewal"),
    url(r'^create_rto/$', views.CreateRTOByAdmin.as_view(), name="create_rto"),
    url(r'^rto_list/$', views.GetRtoList.as_view(), name="rto_list"),
    url(r'^rto_delete/$', views.DeleteRtoOfficer.as_view(), name="rto_delete"),

    url(r'^rto_registration/$', views.RTORegistration.as_view(), name="rto_registration"),

]
