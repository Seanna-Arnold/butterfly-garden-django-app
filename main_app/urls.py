from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('butterflies/', views.butterflies_index, name='index'),
  path('butterflies/<int:butterfly_id>/', views.butterflies_detail, name='detail'),
  path('butterflies/create/', views.ButterflyCreate.as_view(), name='butterflies_create'),
  path('butterflies/<int:pk>/update/', views.ButterflyUpdate.as_view(), name='butterflies_update'),
  path('butterflies/<int:pk>/delete/', views.ButterflyDelete.as_view(), name='butterflies_delete'),
  path('butterflies/<int:butterfly_id>/add_cycle/', views.add_feeding, name='add_cycle'),
  path('butterflies/<int:butterfly_id>/assoc_flora/<int:flora_id>/', views.assoc_flora, name='assoc_flora'),
  path('butterflies/<int:butterfly_id>/unassoc_flora/<int:flora_id>/', views.unassoc_flora, name='unassoc_flora'),
  path('floras/', views.FloraList.as_view(), name='floras_index'),
  path('floras/<int:pk>/', views.FloraDetail.as_view(), name='floras_detail'),
  path('floras/create/', views.FloraCreate.as_view(), name='floras_create'),
  path('floras/<int:pk>/update/', views.FloraUpdate.as_view(), name='floras_update'),
  path('floras/<int:pk>/delete/', views.FloraDelete.as_view(), name='floras_delete'),
]