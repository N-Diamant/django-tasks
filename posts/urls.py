from posts import views

from django.urls import path  #path func responsible for mapping a view function to a url

urlpatterns = {

    path("homepage/",views.homepage,name ="posts_home" ),
    path("",views.PostListCreateView.as_view(),name="list_posts"),
    path("<int:post_id>",views.PostRetrieveUpdateDeleteView.as_view(),name = "post_details"),



}
