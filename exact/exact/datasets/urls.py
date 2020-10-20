from django.urls import path

from . import views

app_name = 'datasets'
urlpatterns = [
    path('', views.index, name='index'),

    # MICCAI
    path('asthma_miccai/create/', views.create_miccai_asthma_dataset, name='create-miccai-asthma-dataset'),
    path('eiph_miccai/create/', views.create_miccai_eiph_dataset, name='create-miccai-eiph-dataset'),
    path('mitotic_miccai/create/', views.create_miccai_mitotic_dataset, name='create-miccai-mitotic-dataset'),

    #path('eiph/create/', views.create_eiph_dataset, name='create-eiph-dataset'),
    #path('asthma/create/', views.create_asthma_dataset, name='create-asthma-dataset'),
]