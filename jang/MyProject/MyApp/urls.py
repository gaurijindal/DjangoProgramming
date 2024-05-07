from django.urls import path, re_path
from .import views
# from MyApp.views import FormView
urlpatterns = [

          # Static Urls
          # path('hello/', views.hello),
          # path('home/', views.home),
          # path('hom1/', views.user),
          # path('dishes/', views.menuitems),

          # # Dynamic Urls(Route Parameters)
          # path('greet/<str:name>', views.greeting),
          # path('food/<str:dish>', views.menuitem),
          # path('sum/<int:num1>/<int:num2>', views.add),
          # path('greett/', views.greet),
          # path('add/', views.sum),

          # # Dynamic Urls(Query Parameters)
          # path('calculate/', views.calculate),
          # re_path(r'^user/(?P<username>[a-zA-Z]+)/$',views.user_profile),
          # # re_path(r'^items/(?P<item_id>\d+)/$', views.items),
          # re_path(r'^products/(?P<product_id>[a-zA-Z \d]+)/$',views.products),
          # re_path(r'^post/(?P<post>[\w-]+)/?$', views.post),
          # re_path(r'^restaurant/(?P<category>[\s\w$-%]+)/?(?P<subcategory>[\s\w$-%]*)/?$', views.order),
          # path('index/', views.index),
          # path('carte/', views.carte),
          # path('snacks/', views.menu),
          # path('eatery/<str:delicacy>', views.eatery),
          # path('homme/', views.homme, name='homme'),
          # path('about/', views.about, name='about'),
          # path('foodie/', views.food, name='food'),
          # path('feed/<str:item>', views.feed, name='feed'),
          # path('form/', views.simpleform),
          # path('forms/', views.simpleforms),
          # path('testcss/', views.testcss),
          # path('form1/', FormView.as_view()), #when rendering a class
          # path('formfunc/', views.FormViews, name = 'FormViews'),
          # path('validation/',views.validation),
          # path('val_django_form/', views.val_django_form),
          # path('sign/', views.Sign),
          # path('signup/', views.Signup),
          # path('get/', views.get_cookie),
          # path('set/', views.set_cookie),
          # path('del/', views.delete_cookie),
          # path('blogspot/', views.blogspot),
          # path('set_session/',views.set_session),
          # path('get_session/',views.get_session),
          # path('deleted_session/',views.delete_session),
          path('login/', views.user_login),
          path('logout/', views.user_logout),
          path('success/', views.success, name='success'),
          path('reset/', views.password_reset)
]