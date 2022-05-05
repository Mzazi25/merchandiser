from itsdangerous import serializer
from rest_auth.registration.views import RegisterView
from route.serializer import ManagerSignupSerializer,MerchandiserSignupSerializer,UserSerializer,LoginMechSerializer
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from route.permissions import IsManagerUser,IsMerchandiserUser
from route.models import Manager, Merchandiser


class MerchandiserSignupView(generics.GenericAPIView):
    serializer_class =MerchandiserSignupSerializer
    

    # def get(self,request,format=None):
    #     merchandisers = Merchandiser.objects.all()
    #     serializers = MerchandiserSignupSerializer(merchandisers,many=True)
    #     return Response(serializers.data)

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= self.request.user
        # token = Token.objects.create(user)
        return Response(serializer.data
            # 'user':UserSerializer(user,context=self.get_serializer_context()).data,
            # 'token':token[1]
           
        )
class LoginMerch(generics.GenericAPIView):
    serializer_class = LoginMechSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.create(user)[1]
            })
class MainUser(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class ManagerSignupView(generics.GenericAPIView):
    serializer_class = ManagerSignupSerializer
    queryset = Manager.objects.all()

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=self.request.user
        return Response( serializer.data
        #    'user':UserSerializer(user,context=self.get_serializer_context()).data,
            # 'token':Token.objects.get(user=user).key,
            # 'message':'account succesfully created'
        )
class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_excepion=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_client':user.is_client
        })
class LogoutView(APIView):
    def post(self,request,format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class ManagerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsManagerUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class MerchandiserOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsMerchandiserUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user
