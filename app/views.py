from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.serializers import UserLoginSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer, UserProfileSerializer, ChangePasswordSerializer, UserSerializer, ServiceSerializer,  ProjectSerializer, EducationSerializer, ExperienceSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from app.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import User, Service, Project, Experience, Education
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST
from rest_framework.decorators import permission_classes, api_view
import json


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refreh": str(refresh),
        'access': str(refresh.access_token),
    }


# -------------------UserRegistrationView--------------------


class GetUserRole(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        role = request.user.role
        return Response({'role': role})


class ProjectAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    # -------------Create Project-----------------------

    def post(self, request, formate=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Project Create Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

# --------------Update Project-----------------------
    def put(self, request, pk, formate=None):
        id = pk
        project = Project.objects.get(pk=id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Completely data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

    def patch(self, request, pk, formate=None):
        id = pk
        project = Project.objects.get(pk=id)
        serializer = ProjectSerializer(
            project, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)
# -----------------Delete Project-----------------------

    def delete(self, request, pk, formate=None):
        id = pk
        project = Project.objects.get(pk=id)
        serializer = ProjectSerializer(project, data=request.data)
        project.delete()
        return Response({'msg': 'Project Delete Completely'})


class UserAPI(APIView):
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']
    renderer_classes = [UserRenderer]
    permission_classes = [AllowAny, IsAuthenticated]


# -------------Create Employee-----------------------

    def post(self, request, formate=None):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'User Create Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

# --------------Update Employee---------------------------------------------
    def put(self, request, pk, formate=None):
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Completely data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

    def patch(self, request, pk, formate=None):
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)
# -----------------Delete Employee-----------------------

    def delete(self, request, pk, formate=None):
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data)
        user.delete()
        return Response({'msg': 'User Delete Completely'})


class ServiceAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]


# -------------Create Salary-----------------------

    def post(self, request, formate=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Service Create Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

# --------------Update Salary-----------------------
    def put(self, request, pk, formate=None):
        id = pk
        service = Service.objects.get(pk=id)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Completely data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

    def patch(self, request, pk, formate=None):
        id = pk
        service = Service.objects.get(pk=id)
        serializer = ServiceSerializer(
            service, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)
# -----------------Delete Task-----------------------

    def delete(self, request, pk, formate=None):
        id = pk
        service = Service.objects.get(pk=id)
        serializer = ServiceSerializer(service, data=request.data)
        service.delete()
        return Response({'msg': 'Service Delete Completely'})


class ExperienceAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]


# -------------Create Salary-----------------------

    def post(self, request, formate=None):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Service Create Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

# --------------Update Salary-----------------------
    def put(self, request, pk, formate=None):
        id = pk
        experience = Experience.objects.get(pk=id)
        serializer = ExperienceSerializer(experience, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Completely data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

    def patch(self, request, pk, formate=None):
        id = pk
        experience = Experience.objects.get(pk=id)
        serializer = ExperienceSerializer(
            experience, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)
# -----------------Delete Task-----------------------

    def delete(self, request, pk, formate=None):
        id = pk
        experience = Experience.objects.get(pk=id)
        serializer = ExperienceSerializer(experience, data=request.data)
        experience.delete()
        return Response({'msg': 'Experience Delete Completely'})


class EducationAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]


# -------------Create Salary-----------------------

    def post(self, request, formate=None):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Education Create Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

# --------------Update Salary-----------------------
    def put(self, request, pk, formate=None):
        id = pk
        eduction = Education.objects.get(pk=id)
        serializer = EducationSerializer(eduction, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Completely data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)

    def patch(self, request, pk, formate=None):
        id = pk
        eduction = Education.objects.get(pk=id)
        serializer = EducationSerializer(
            eduction, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors, status=status.HTTP_400_Bad_Request)
# -----------------Delete Task-----------------------

    def delete(self, request, pk, formate=None):
        id = pk
        eduction = Education.objects.get(pk=id)
        serializer = EducationSerializer(eduction, data=request.data)
        eduction.delete()
        return Response({'msg': 'Education Delete Completely'})


class UserLoginView(APIView):
    allowed_methods = ['POST']
    renderer_classes = [UserRenderer]

    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'role': user.role,  'msg': 'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email and Password not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_401_Bad_Request)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, formate=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_get(request, pk=None, formate=None):
    id = pk
    if id is not None:
        project = Project.objects.get(id=id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            # Change the response structure
            return Response({'msg': 'Password Change Successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Change the response structure
            return Response({'msg': 'Password Reset Successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self,  request, uid, token,  formate=None):
        serializer = UserPasswordResetSerializer(data= request.data, context={'uid':uid, 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset link send. Check Your Email'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def services_get(request, pk=None, formate=None):
    id = pk
    if id is not None:
        service = Service.objects.get(id=id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def users_get(request, pk=None, formate=None):
    id = pk
    if id is not None:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def experience_get(request, pk=None, formate=None):
    id = pk
    if id is not None:
        experience = Experience.objects.get(id=id)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)
    experience = Experience.objects.all()
    serializer = ExperienceSerializer(experience, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def education_get(request, pk=None, formate=None):
    id = pk
    if id is not None:
        education = Education.objects.get(id=id)
        serializer = EducationSerializer(education)
        return Response(serializer.data, status=status.HTTP_200_OK)
    education = Education.objects.all()
    serializer = EducationSerializer(education, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
