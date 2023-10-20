from django.urls import path
from . import views

urlpatterns = [
    path('api/worker/', views.WorkerListCreate.as_view()),
    # path('api/worker/', views.workers),
    path('api/worker/<str:pk>', views.workers_pk),
]
