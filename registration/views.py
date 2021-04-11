from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.models import StandUser, LicenceApplication
from registration.serializers import ApplicationDetails


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
                password=password
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
                application =LicenceApplication.objects.filter(user=user).first()
                print(f"DATA -{LicenceApplication.dob}")
                details_serializer = ApplicationDetails(application)
                try:
                    print(dir(details_serializer.data))
                except Exception as e:
                    print(f"ERROR - {e}")
                return Response({
                    'data': {
                        'data': details_serializer.data,
                        'message': f'Data fetch successfull',
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
