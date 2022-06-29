from django.urls import path

from . import views

urlpatterns = [
    path('award/', views.ListCreateAwardView.as_view()),
    path('award/<int:pk>', views.UpdateDeleteAwardView.as_view()),
    path('formApply/', views.ListCreateFormApplyView.as_view()),
    path('formApply/<int:pk>', views.UpdateDeleteFormApplyView.as_view()),

    path('studentTranscript/', views.ListCreateStudentTranscriptView.as_view()),
    path('studentTranscript/<int:pk>', views.UpdateDeleteStudentTranscriptView.as_view()),

    path('student/', views.ListCreateUserView.as_view()),
    path('student/<int:pk>',views.UpdateDeleteUserView.as_view()),
    # path('mail/',views.success),

    # path('testSendMail/', views.testSendMail)


]
