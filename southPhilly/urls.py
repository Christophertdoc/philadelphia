from django.urls import path

from . import views

urlpatterns = [
    # ex: /southPhilly/
    path('', views.index, name='index'),
    # ex: /southPhilly/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /southPhilly/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /southPhilly/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]