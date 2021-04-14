from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.models import *
from registration.serializers import *


class UserLoginApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print("testt")
        try:
            data = request.data
            print(data)
            username = data.get("username")
            password = data.get("password")
            user_type = data.get("user_type")
            if user_type == "User":
                user_details = StandUser.objects.filter(username=username).first()
                if user_details:
                    if user_details.password == password:
                        return Response({
                            'data': {
                                'user_type': "user",
                                'name': user_details.name,
                                'user_id': user_details.id,
                                'user_name': user_details.username,
                                'message': "Valid user",
                                'status': True
                            }
                        })
                    else:
                        return Response({
                            'data': {
                                'message': "Invalid Username or password",
                                'status': False
                            }
                        })
                else:
                    return Response({
                        'data': {
                            'message': "Invalid Username or password",
                            'status': False
                        }
                    })
            elif user_type == "Admin":
                user = User.objects.filter(username=username).first()
                print("testsetset")
                print(user.password)
                if user:
                    if user.check_password(password):
                        return Response({
                            'data': {
                                'user_type': "admin",
                                'name': user.username,
                                'user_id': user.id,
                                'message': "Valid user",
                                'status': True
                            }
                        })
                    else:
                        return Response({
                            'data': {
                                'message': "Invalid Username or password",
                                'status': False
                            }
                        })
                else:
                    return Response({
                        'data': {
                            'message': "Invalid Username or password",
                            'status': False
                        }
                    })
            elif user_type == "rto":
                rto = RtoOfficer.objects.filter(username=username).first()
                if rto:
                    if rto.password == password:
                        return Response({
                            'data': {
                                'user_type': "rto",
                                'name': rto.name,
                                'user_id': rto.id,
                                'message': "Valid user",
                                'status': True
                            }
                        })
                    else:
                        return Response({
                            'data': {
                                'message': "Invalid Username or password",
                                'status': False
                            }
                        })
                else:
                    return Response({
                        'data': {
                            'message': "Invalid Username or password",
                            'status': False
                        }
                    })
            return Response({
                'data': {
                    'message': f'Successs',
                    'status': True
                }
            })


        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class UserRegistrationApiView(APIView):

    def post(self, request):
        try:
            data = request.data
            name = data.get("name")
            address = data.get("address")
            age = data.get("age")
            district = data.get("district")
            username = data.get("username")
            password = data.get("password")
            if StandUser.objects.filter(username=username).exists():
                return Response({
                    'data': {
                        'message': f'Username already exist, please try different.',
                        'status': False
                    }
                })
            StandUser.objects.create(
                name=name,
                address=address,
                age=age,
                district=district,
                username=username,
                password=password,
                phnumber=data.get("phnumber")
            )
            return Response({
                'data': {
                    'message': f'User Created successfully',
                    'status': True
                }
            })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class ApplicationForNewLicence(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get('user_id')).first()
            if user:
                print(user)
                if LicenceApplication.objects.filter(user=user).exists():
                    application = LicenceApplication.objects.filter(user=user).first()
                    application.user = user
                    application.district = data.get("district")
                    application.phnumber = data.get("phnumber")
                    application.name = data.get("name")
                    application.relation_with = data.get("relation")
                    application.relation_name = data.get("relationname")
                    application.gender = data.get("gender")
                    application.qualification = data.get("qualification")
                    application.emphnumber = data.get("enumber")
                    application.dob = data.get("dob")
                    application.country = data.get("country")
                    application.blood = data.get("bloodgroup")
                    application.identificationmark1 = data.get("idenmark1")
                    application.identificationmark2 = data.get("idenmark2")
                    application.prhousename = data.get("housename")
                    application.prstreet = data.get("street")
                    application.prlocation = data.get("landmark")
                    application.prpincode = data.get("pincode")
                    application.prvillage = data.get("village")
                    application.prtaluk = data.get("taluk")
                    application.trhousename = data.get("tmhousename")
                    application.tstreet = data.get("tmstreet")
                    application.trlocation = data.get("tmlandmark")
                    application.trpincode = data.get("tmpincode")
                    application.trvillage = data.get("tmvillage")
                    application.trtaluk = data.get("tmtaluk")
                    application.classofvehicle = data.get("classofveh")
                    sameasabove = data.get("sameasabove")
                    if sameasabove == "on":
                        application.trhousename = data.get("housename")
                        application.tstreet = data.get("street")
                        application.trlocation = data.get("landmark")
                        application.trpincode = data.get("pincode")
                        application.trvillage = data.get("village")
                        application.trtaluk = data.get("taluk")
                    application.save()
                    user.user_status = "Application Filled"
                    user.save()
                    return Response({
                        'data': {
                            'message': "Data Updated successfully",
                            'status': True
                        }
                    })
                else:
                    application = LicenceApplication.objects.create(
                        user=user,
                        district=data.get("district"),
                        phnumber=data.get("phnumber"),
                        name=data.get("name"),
                        relation_with=data.get("relation"),
                        relation_name=data.get("relationname"),
                        gender=data.get("gender"),
                        qualification=data.get("qualification"),
                        emphnumber=data.get("enumber"),
                        dob=data.get("dob"),
                        country=data.get("country"),
                        blood=data.get("bloodgroup"),
                        identificationmark1=data.get("idenmark1"),
                        identificationmark2=data.get("idenmark2"),
                        prhousename=data.get("housename"),
                        prstreet=data.get("street"),
                        prlocation=data.get("landmark"),
                        prpincode=data.get("pincode"),
                        prvillage=data.get("village"),
                        prtaluk=data.get("taluk"),
                        trhousename=data.get("tmhousename"),
                        tstreet=data.get("tmstreet"),
                        trlocation=data.get("tmlandmark"),
                        trpincode=data.get("tmpincode"),
                        trvillage=data.get("tmvillage"),
                        trtaluk=data.get("tmtaluk"),
                        classofvehicle=data.get("classofveh"),
                    )
                    sameasabove = data.get("sameasabove")
                    if sameasabove == "on":
                        application.trhousename = data.get("housename")
                        application.tstreet = data.get("street")
                        application.trlocation = data.get("landmark")
                        application.trpincode = data.get("pincode")
                        application.trvillage = data.get("village")
                        application.trtaluk = data.get("taluk")
                        application.save()
                    user.user_status = "Application Filled"
                    user.save()
                    return Response({
                        'data': {
                            'message': "Data Updated successfully",
                            'status': True
                        }
                    })
            else:
                return Response({
                    'data': {
                        'message': "User not found, Something went wrong",
                        'status': False
                    }
                })

        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class GetUserDetails(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                application = LicenceApplication.objects.filter(user=user).first()
                document_details = UserDocuments.objects.filter(user=user).first()

                print(f"DATA -{LicenceApplication.dob}")
                details_serializer = ApplicationDetails(application)
                document_serializer = DocumentSerializer(document_details)
                try:
                    print(dir(details_serializer.data))
                except Exception as e:
                    print(f"ERROR - {e}")
                return Response({
                    'data': {
                        'data': details_serializer.data,
                        'documents': document_serializer.data,
                        'message': f'Data fetch successfully',
                        'status': True
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class DocumentUpload(APIView):

    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                if UserDocuments.objects.filter(user=user).exists():
                    document_details = UserDocuments.objects.filter(user=user).first()
                    document_details.identitycertificate = data.get("identityproof")
                    document_details.eyecertificate = data.get("eyecertificate")
                    document_details.selfcertificate = data.get("selfdeclarationfrom")
                    document_details.photo = data.get("photo")
                    document_details.signature = data.get("signature")
                    document_details.identitytype = data.get("identity_type")
                    document_details.medicalcertificate = data.get("medical")
                    document_details.save()
                else:
                    UserDocuments.objects.create(
                        user=user,
                        identitycertificate=data.get("identityproof"),
                        eyecertificate=data.get("eyecertificate"),
                        selfcertificate=data.get("selfdeclarationfrom"),
                        photo=data.get("photo"),
                        signature=data.get("signature"),
                        identitytype=data.get("identity_type"),
                        medicalcertificate=data.get("medical"),
                    )
                renewal_flag = data.get("reneweldata")
                if renewal_flag == "True":
                    user.renewal_status = "Documents Uploaded"
                    user.save()
                else:
                    user.user_status = "Documents Uploaded"
                    user.save()
                return Response({
                    'data': {
                        'message': "Files uploaded successfully",
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': f'User not found, Something went wrong',
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class GetUserStatus(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                return Response({
                    'data': {
                        'user_status': user.user_status,
                        'renewal_status': user.renewal_status,
                        'message': f'Status fetched successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "Something went wrong",
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class UserStatusUpdate(APIView):

    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                if user.user_status == "Documents Uploaded":
                    user.user_status = data.get("status")
                    user.save()
                elif user.renewal_status == "Documents Uploaded":
                    user.renewal_status = data.get("status")
                    user.save()
                return Response({
                    'data': {
                        'user_status': user.user_status,
                        'message': f'Status updated successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "Something went wrong",
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class DocumentListAll(APIView):
    def post(self, request):
        try:
            data = request.data
            other_documents = []
            main_documents = []
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                main_documents = UserDocuments.objects.filter(user=user).first()
                other_documents = OtherDocuments.objects.filter(user=user)

                document_serializer = DocumentSerializer(main_documents)
                other_serializer = OtherDocumentSerializer(other_documents, many=True)
                return Response({
                    'data': {
                        'main_documents': document_serializer.data,
                        'other_documents': other_serializer.data,
                        'message': f'Data fetch successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "User not found, Something went wrong",
                        'status': False
                    }
                })

        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class OtherDocumentUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                OtherDocuments.objects.create(
                    user=user,
                    document_name=data.get("document_name"),
                    document=data.get("identityproof")
                )
                return Response({
                    'data': {
                        'message': f'Updated successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "User not found, Something went wrong",
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class OtherDocumentDelete(APIView):
    def post(self, request):
        try:
            data = request.data
            id = data.get("image_id")
            if id:
                OtherDocuments.objects.filter(id=id).delete()
                return Response({
                    'data': {
                        'message': f'Deleted successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "Id not found, Something went wrong",
                        'status': False
                    }
                })

        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class LicenceRenewalApplicationAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                if LicenceRenewalApplication.objects.filter(user=user).exists():
                    application = LicenceRenewalApplication.objects.filter(user=user).first()
                    application.district = data.get("district")
                    application.phnumber = data.get("phnumber")
                    application.name = data.get("name")
                    application.dob = data.get("dob")
                    application.prhousename = data.get("housename")
                    application.prstreet = data.get("street")
                    application.prlocation = data.get("landmark")
                    application.prpincode = data.get("pincode")
                    application.prvillage = data.get("village")
                    application.prtaluk = data.get("taluk")
                    application.trhousename = data.get("tmhousename")
                    application.tstreet = data.get("tmstreet")
                    application.trlocation = data.get("tmlandmark")
                    application.trpincode = data.get("tmpincode")
                    application.trvillage = data.get("tmvillage")
                    application.trtaluk = data.get("tmtaluk")
                    application.licencenumber = data.get("licencenumber")
                    application.licencefrom = data.get("licencefrom")
                    application.licenceto = data.get("licenceto")
                    sameasabove = data.get("sameasabove")
                    if sameasabove == "on":
                        application.trhousename = data.get("housename")
                        application.tstreet = data.get("street")
                        application.trlocation = data.get("landmark")
                        application.trpincode = data.get("pincode")
                        application.trvillage = data.get("village")
                        application.trtaluk = data.get("taluk")
                    application.save()
                    user.renewal_status = "Application Filled"
                    user.save()
                    return Response({
                        'data': {
                            'message': "Data Updated successfully",
                            'status': True
                        }
                    })
                else:
                    application = LicenceRenewalApplication.objects.create(
                        user=user,
                        district=data.get("district"),
                        phnumber=data.get("phnumber"),
                        name=data.get("name"),
                        dob=data.get("dob"),
                        prhousename=data.get("housename"),
                        prstreet=data.get("street"),
                        prlocation=data.get("landmark"),
                        prpincode=data.get("pincode"),
                        prvillage=data.get("village"),
                        prtaluk=data.get("taluk"),
                        trhousename=data.get("tmhousename"),
                        tstreet=data.get("tmstreet"),
                        trlocation=data.get("tmlandmark"),
                        trpincode=data.get("tmpincode"),
                        trvillage=data.get("tmvillage"),
                        trtaluk=data.get("tmtaluk"),
                        licencenumber=data.get("licencenumber"),
                        licencefrom=data.get("licencefrom"),
                        licenceto=data.get("licenceto"),
                    )
                    sameasabove = data.get("sameasabove")
                    if sameasabove == "on":
                        application.trhousename = data.get("housename")
                        application.tstreet = data.get("street")
                        application.trlocation = data.get("landmark")
                        application.trpincode = data.get("pincode")
                        application.trvillage = data.get("village")
                        application.trtaluk = data.get("taluk")
                        application.save()
                    user.renewal_status = "Application Filled"
                    user.save()
                    return Response({
                        'data': {
                            'message': "Data Updated successfully",
                            'status': True
                        }
                    })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class getuserRenewalData(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                user_details = LicenceRenewalApplication.objects.filter(user=user).first()
                document_details = UserDocuments.objects.filter(user=user).first()

                data_serializer = UserRenewalDataSerializer(user_details)
                document_serializer = DocumentSerializer(document_details)

                return Response({
                    'data': {
                        'data': data_serializer.data,
                        'document': document_serializer.data,
                        'message': f'Data fetch successfully',
                        'status': True
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class GetStatusPageData(APIView):
    def post(self, request):
        try:
            data = request.data
            user = StandUser.objects.filter(id=data.get("user_id")).first()
            if user:
                data = {
                    "name": user.name,
                    "address": user.address,
                    "phnumber": user.phnumber,
                    "status": user.renewal_status
                }
                return Response({
                    'data': {
                        'data': data,
                        'message': f'Data fetch successfully',
                        'status': True
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class CreateRTOByAdmin(APIView):
    def post(self, request):
        try:
            data = request.data
            if RtoOfficer.objects.filter(district=data.get("district")).exists():
                return Response({
                    'data': {
                        'message': f'Officer already exists for the {data.get("district")}',
                        'status': False
                    }
                })
            else:
                RtoOfficer.objects.create(
                    district=data.get("district"),
                    officerid=data.get("rtoid")
                )
                return Response({
                    'data': {
                        'message': f'Officer created successfully',
                        'status': True
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class GetRtoList(APIView):
    def get(self, request):
        try:
            rto_list = RtoOfficer.objects.all()
            rto_serializer = RtoAdminSerializer(rto_list, many=True)
            return Response({
                'data': {
                    'data': rto_serializer.data,
                    'message': f'Officer fetched successfully',
                    'status': True
                }
            })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class DeleteRtoOfficer(APIView):
    def post(self, request):
        try:
            data = request.data
            if data.get("id"):
                RtoOfficer.objects.filter(id=data.get("id")).delete()
                return Response({
                    'data': {
                        'message': f'Officer deleted successfully',
                        'status': True
                    }
                })
            else:
                return Response({
                    'data': {
                        'message': "Id not found, Something went wrong",
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })


class RTORegistration(APIView):
    def post(self, request):
        try:
            data = request.data
            district = data.get("district")
            rto_id = data.get("rtoid")
            rto_entry = RtoOfficer.objects.filter(district=district).first()
            if rto_entry:
                if rto_entry.officerid == rto_id:
                    rto_entry.name = data.get("name")
                    rto_entry.phnumber = data.get("phnumber")
                    rto_entry.username = data.get("username")
                    rto_entry.password = data.get("password")
                    rto_entry.save()
                    return Response({
                        'data': {
                            'message': "Data Updated successfully",
                            'status': True
                        }
                    })
                else:
                    return Response({
                        'data': {
                            'message': "Invalid RTO ID entered, Please contact admin",
                            'status': False
                        }
                    })
            else:
                return Response({
                    'data': {
                        'message': "No valid ID created for the district, Please contact admin",
                        'status': False
                    }
                })
        except Exception as e:
            return Response({
                'data': {
                    'message': f'Exception occured - {str(e)}',
                    'status': False
                }
            })
