from rest_framework.response import Response
from .serializers import UserLoginSerializer
from rest_framework.views import APIView
from login import models
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ValidationError




class UserLogin(APIView):
    # get method handler
    def get(self, request, id=None):
        is_all = request.GET.get('is_all',True)
        print('isssssssssssssssss',is_all)
        if is_all:
            all_login = [obj.login_data_dict() for obj in models.User.objects.all()]
            # print('alllllllllllllllllllll',all_login)
            return Response(status=200, data = {"data":all_login})
        
        login_instance = models.User.objects.filter(id=id).last()
        
        # logging.info(f"GET_SCHOOL: {school_instance}")

        if not login_instance:
            return Response(status=400, data = {"data":"school is not found"})

        return Response(status=200, data = {"data":login_instance.get_school_data_dict()})
    
    @ensure_csrf_cookie
    def post(self, reqeust, id=None):

        serializer_instance  = UserLoginSerializer(data = reqeust.data)
        print('postttttttttttttt',serializer_instance)

        if not serializer_instance.is_valid():
            return Response(status=400, data = {"data":serializer_instance.errors})

        username = serializer_instance.validated_data.get('username')
        email = serializer_instance.validated_data.get('email')
        password = serializer_instance.validated_data.get('password')
        ifLogged = serializer_instance.validated_data.get('ifLogged')
        mobile_no = serializer_instance.validated_data.get('mobile_no')

        return Response(status=200, data = {"data":'PARAS'})
