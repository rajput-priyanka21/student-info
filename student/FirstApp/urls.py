from django.urls import path

from FirstApp import views

urlpatterns=[
    path('student info/',views.all_student_info),
    path('annual_defaulter/',views.all_annual_fee_defaulter_info),
    path('monthly_defaulter/',views.all_monthly_fee_defaulter_info),
]