from django.urls import path
from .views import many_fields_form_widget, user_form, many_fields_form, add_user, upload_image


urlpatterns = [
    path("user/add/", user_form, name="user_form"),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('forms_widget/', many_fields_form_widget, name='many_fields_form_widget'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
