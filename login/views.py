# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import logout
# from django.shortcuts import HttpResponseRedirect
# from .models import login


# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})


# def home(request):
#     return render(request, 'index.html')


# def signin(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(requestrest_framework.authtokenlogin, username=username, password=password)

#         login(request, user)
#         login_data = login(username=username, password=password)
#         login_data.save()
#         return redirect('/profile')

#         # msg = 'Error Login'
#         # form = AuthenticationForm(request.POST)
#         # return render(request, 'login.html', {'form': form, 'msg': msg})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})


# def profile(request):
#     return render(request, 'profile.html')


# def signout(request):
#     logout(request)
#     return redirect('/')



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({'token': user.auth_token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# from django.contrib.auth import login

# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


csrf_exempt
class LoginView(APIView):
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # your authentication logic here
    #         return Response({'message': 'Login Successful!'}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
            
        print('mmmmmmmmmmmmmmmmm',username)
        print('pppppppppppppppppp',password)
        
        user = authenticate(username=username, password=password)
        print('uuuuuuser',user)
        if user:
            serializer = UserSerializer(data={'username': username, 'password': password})
            if serializer.is_valid():
                serializer.save()
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)