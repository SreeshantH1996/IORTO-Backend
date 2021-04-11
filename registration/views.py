from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.models import StandUser


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
