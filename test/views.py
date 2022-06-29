from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status,permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Award, FormApply, User, StudentTranscript
from .Serializer import AwardSerializer, FormApplySerializer, UserSerializer, StudentTranscriptSerializer




class ListCreateAwardView(ListCreateAPIView):
    model = Award
    serializer_class = AwardSerializer

    def get_queryset(self):
        return Award.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AwardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Award successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteAwardView(RetrieveUpdateDestroyAPIView):
    model = Award
    serializer_class = AwardSerializer

    def get_queryset(self):
        awardName = self.kwargs['pk']
        return Award.objects.filter(id=awardName)

    def put(self, request, *args, **kwargs):
        award = get_object_or_404(Award, id=kwargs.get('pk'))
        serializer = AwardSerializer(award, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Award successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        award = get_object_or_404(Award, id=kwargs.get('pk'))
        award.delete()

        return JsonResponse({
            'message': 'Delete Award successful!'
        }, status=status.HTTP_200_OK)





# ////////
class ListCreateFormApplyView(ListCreateAPIView):
    model = FormApply
    serializer_class = FormApplySerializer

    def get_queryset(self):
        formApply= FormApply.objects.filter()
        s = self.request.query_params.get('s')
        if s is not  None:
            formApply= formApply.filter(status=s)
        return formApply

    def create(self, request, *args, **kwargs):
        serializer = FormApplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Award successful!'
            }, status=status.HTTP_201_CREATED)


        return JsonResponse({
            'message': 'Create a new Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)



class UpdateDeleteFormApplyView(RetrieveUpdateDestroyAPIView):
    model = FormApply
    serializer_class = FormApplySerializer


    def get_queryset(self):
        student_id = self.kwargs['pk']
        return FormApply.objects.filter(id=student_id)

    def put(self, request, *args, **kwargs):
        formApply = get_object_or_404(FormApply, id=kwargs.get('pk'))
        serializer = FormApplySerializer(formApply, data=request.data)
        # mail_subject = 'Activate your blog account.'
        # email = "nguyenduykhuong0201t@gmail.com"
        # message = "hello"
        # send_email = EmailMessage(mail_subject, message, to=[email])
        # send_email.send()
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Award successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        formApply = get_object_or_404(FormApply, id=kwargs.get('pk'))
        formApply.delete()

        return JsonResponse({
            'message': 'Delete Award successful!'
        }, status=status.HTTP_200_OK)



class ListCreateStudentTranscriptView(ListCreateAPIView):
    model = StudentTranscript
    serializer_class = StudentTranscriptSerializer

    def get_queryset(self):
        transcript = StudentTranscript.objects.filter()
        p = self.request.query_params.get("p")
        if p is not None:
            transcript=transcript.filter(student_id=p)
        return transcript


    def create(self, request, *args, **kwargs):
        serializer = StudentTranscriptSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Award successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteStudentTranscriptView(RetrieveUpdateDestroyAPIView):
    model = StudentTranscript
    serializer_class = StudentTranscriptSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return StudentTranscript.objects.filter(id=user_id)

    def put(self, request, *args, **kwargs):
        studentTranscript = get_object_or_404(StudentTranscript, id=kwargs.get('pk'))
        serializer = StudentTranscriptSerializer(studentTranscript, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Award successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Award unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        studentTranscript = get_object_or_404(StudentTranscript, id=kwargs.get('pk'))
        studentTranscript.delete()

        return JsonResponse({
            'message': 'Delete Award successful!'
        }, status=status.HTTP_200_OK)

    # /////


class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return JsonResponse({
            'message': 'Create a new Student successful!'
        }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new  Student unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return User.objects.filter(id=user_id)

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return JsonResponse({
            'message': 'Update  Studentsuccessful!'
        }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update  Student unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': 'Delete  Student successful!'
        }, status=status.HTTP_200_OK)
    # send mail

