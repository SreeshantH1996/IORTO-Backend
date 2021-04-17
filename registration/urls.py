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
    url(r'^user_list/$', views.UserListForRTO.as_view(), name="user_list"),
    url(r'^renewal_list/$', views.LicenceRenewalListRto.as_view(), name="renewal_list"),
    url(r'^renewal_application/$', views.GetRenewalApplicationDetials.as_view(), name="renewal_application"),
    url(r'^rto_status_change/$', views.RtoStatusChange.as_view(), name="rto_status_change"),

    url(r'^application_list/$', views.LicenceApplicationListRto.as_view(), name="application_list"),
    url(r'^application_detials/$', views.GetNewApplicationDetails.as_view(), name="application_detials"),
    url(r'^get_new_status_data/$', views.GetNewStatusPageData.as_view(), name="get_new_status_data"),

]
