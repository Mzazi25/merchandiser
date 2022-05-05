from rest_framework import serializers
from route .models import Manager,Merchandiser,User
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_manager']

class MerchandiserSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
    class Meta:
        model = User
        fields=['username', 'email', 'password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self,**kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password = self.validated_data['password']
        )
        user.set_password('password')
        user.is_merchandiser = True
        user.save()
        Merchandiser.objects.create(user=user)
        return user
class LoginMechSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('incorrect credentials')

class ManagerSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password2"},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        # password=self.validated_data['password'],
        # password2=self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({"error":"password does not match"})
        user.set_password('password')
        user.is_manager=True
        user.save()
        Manager.objects.create(user=user)
        return user
        
# class ManagerSignupSerializer(RegisterSerializer):
#     manager = serializers.PrimaryKeyRelatedField(read_only = True)
#     company = serializers.CharField(required=True)

#     def get_cleaned_data(self):
#         data = super(ManagerSignupSerializer,self).get_cleaned_data()
#         extra_data = {
#             'company':self.validated_data.get('company',),
#         }
#         data.update(extra_data)
#         return data

#     def save(self, request):
#         user = super(ManagerSignupSerializer,self).save(request)
#         user.is_manager = True
#         user.save()
#         manager = Manager(manager= user, company = self.cleaned_data.get('company'))
#         manager.save()
#         return user

# class MerchandiserSignupSerializer(RegisterSerializer):
#     name = serializers.PrimaryKeyRelatedField(read_only=True)
#     area = serializers.CharField(required = True)
#     description = serializers.CharField(required=True)

#     def get_cleaned_data(self):
#         data = super(MerchandiserSignupSerializer,self).get_cleaned_data()
#         extra_data = {
#             'area':self.validated_data.get('area',),
#             'description':self.validated_data.get('description',)
#         }
#         data.update(extra_data)
#         return data 

#     def save(self,request):
#         user = super(MerchandiserSignupSerializer,self).save(request)
#         user.is_merchandiser =True
#         user.save()
#         merchandiser = Merchandiser(merchandiser=user,area=self.cleaned_data.get('country'),description=self.cleaned_data.get('description'))
#         merchandiser.save()
#         return user