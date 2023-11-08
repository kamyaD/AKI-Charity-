from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("team", views.team, name="team"),
    path("testimonials", views.testimonials, name="testimonials"),
    path("services", views.services, name="services"),
    path("blog", views.blog, name="blog"),
    path("education", views.education, name="education"),
    path("health", views.health, name="health"),
    path("economic", views.economic, name="economic"),
    path("conflict", views.conflict, name="conflict"),
    path("climate", views.climate, name="climate"),
    path("partner", views.partnerships, name="partnerships"),
    path("get-contact", views.get_contact_message, name="get-contact"),
    path("contact", views.contact, name="contact"),
    path("success_page", views.success, name="success_page"),
    path("blog/<int:post_id>/", views.post_detail, name='post_detail')
]