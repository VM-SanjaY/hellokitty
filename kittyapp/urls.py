from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.loginpage, name = 'loginpage'),
    path('register/',views.registerpage, name = 'registerpage'),
    path('sendotp/',views.sendotp, name = 'sendotp'),
    path('otp/',views.otppage, name = 'otppage'),
    path('logout/',views.logoutpage,name="logout"),
    path('resertpassword/',auth_views.PasswordResetView.as_view(template_name="kittyapp/forgotpassword.html"), name = "reset_password"),
    path('resertpassword_sent/',auth_views.PasswordResetDoneView.as_view(template_name="kittyapp/forgotmail.html"), name = "password_reset_done"),
    path('resert/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="kittyapp/passwordchange.html"), name = "password_reset_confirm"),
    path('resertpassword_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="kittyapp/changed.html"), name = "password_reset_complete"),
    path('',views.indexpage, name = 'indexpage'),
    path('details/',views.detailspage, name = 'detailspage'),
    path('home/details/',views.afterdetail, name = 'afterdetail'),
    path('home/',views.indexpage2, name = 'indexpage2'),
    path('patreon/',views.patreon,name='patreon'),
    path('patreon/paymentstatus/',views.paymentstatus,name='paymentstatus'),
    path('home/profile/',views.profile,name='profile'),
    path('vid/',views.vid,name='vid'),
    path('v3/',views.v3,name='v3'),
    path('v4/',views.v4,name='v4'),
    # after login
    path('home/craft/',views.craftpdf,name='craftpdf'),
    path('home/momsurprise/',views.mompdf,name='mompdf'),
    path('home/pop-princess/',views.poppdf,name='poppdf'),
    path('home/paradise/',views.hello,name='hello'),
    path('home/paradise/ep1/',views.hello1,name='hello1'),
    path('home/paradise/ep2/',views.hello2,name='hello2'),
    path('home/paradise/ep3/',views.hello3,name='hello3'),
    path('home/paradise/ep4/',views.hello4,name='hello4'),
    path('home/paradise/ep5/',views.hello5,name='hello5'),
    path('home/paradise/ep6/',views.hello6,name='hello6'),
    path('home/paradise/ep7/',views.hello7,name='hello7'),
    path('home/paradise/ep8/',views.hello8,name='hello8'),
    path('home/paradise/ep9/',views.hello9,name='hello9'),
    path('home/paradise/ep10/',views.hello10,name='hello10'),
    path('home/thertical/',views.theatre,name='theatre'),
    path('home/thertical/ep1/',views.theatre1,name='theatre1'),
    path('home/thertical/ep2/',views.theatre2,name='theatre2'),
    path('home/thertical/ep3/',views.theatre3,name='theatre3'),
    path('home/thertical/ep4/',views.theatre4,name='theatre4'),
    path('home/thertical/ep5/',views.theatre5,name='theatre5'),
    path('home/thertical/ep6/',views.theatre6,name='theatre6'),
    path('home/thertical/ep7/',views.theatre7,name='theatre7'),
    path('home/thertical/ep8/',views.theatre8,name='theatre8'),
    path('home/kuroppi/',views.kuroppi,name='kuroppi'),
    path('home/kuroppi/ep1',views.kuroppi1,name='kuroppi1'),
    path('home/kuroppi/ep2',views.kuroppi2,name='kuroppi2'),
    path('home/kuroppi/ep3',views.kuroppi3,name='kuroppi3'),
    path('home/draw-hellokitty/',views.draw,name='draw'),
    path('home/draw-hellokitty/draw',views.draw1,name='draw1'),

    

  
]



