from django.urls import path, re_path
from . import views
#app_name='app'
urlpatterns =[


    path('AboutUs', views.AboutUs,name="درباره ما  "),
    path('create_about', views.create_about,name="    ثبت و ذخیره    "),
    path('list_about', views.list_about,name="     لیست   "),
    path('update_about', views.update_about,name="  ویرایش        "),
    path('delet_about', views.delet_about,name="   پاک کردن     "),
    #######################################
    path('Blog',views.Blog,name="وبلاگ    "),
    path('Blogdetails',views.Blogdetails,name="  جزییات وبلاگ    "),
    path('create_blog',views.create_blog,name="    ثبت و ذخیره    "),
    path('list_blog',views.list_blog,name="     لیست   "),
    path('update_blog',views.update_blog,name="  ویرایش"),
    path('delet_blog',views.delet_blog,name="   پاک کردن     "), 
    #########################################################
    path('create_moshaver', views.create_moshaver,name="    ثبت و ذخیره    "),
    path('panel_moshaver', views.panel_moshaver,name="     پنل شخصی    "),
    path('page_moshaver1', views.page_moshaver1,name="     پنل عمومی    "),  
    path('path/to/list_moshaver1', views.list_moshaver1, name='list_moshaver1'),
   
    path('consultant/<int:pk>/podcasts/',views.consultant_podcasts, name='consultant_podcasts'),  # صفحه پادکست‌ها
    path('consultant/<int:pk>',views.get, name='consultant_public_panel'),  # پنل عمومی مشاور
    path('get/<int:pk>/', views.get, name="geth"), 
   
    path('consultant/<int:pk>/datav/', views.getv, name="consultant_vidio"), 
    path('consultant/<int:pk>/datat/', views.gett, name="consultant_test"), 
    path('sabt_moshaver', views.sabt_moshaver,name="ثبت اطلاعات مشاور  "),
    path('list_moshaver', views.list_moshaver, name=" لیست مشاوران "),
    #####################################################
    path('ContactUs', views.ContactUs,name="   تماس با ما   "),
    path('contact', views.contact,name="    ثبت و ذخیره    "),
    path('mycomment', views.mycomment,name="    ثبت و ذخیره    "),
    path('update_ContactUs', views.update_ContactUs,name="  ویرایش        "),
    path('delet_ContactUs', views.delet_ContactUs,name="   پاک کردن     "),
    ###################################################
    path('Faq', views.Faq,name=" سوالات "),
    path('create_Faq', views.create_Faq,name="    ثبت و ذخیره    "),
    path('list_Faq', views.list_Faq,name="     لیست   "),  
    path('delete_Faq', views.delete_Faq,name="   پاک کردن     "),
    path('get_ask_with_comment/<int:pk>', views.get_ask_with_comment,name="         "),
    ###################################################
    path('index', views.index,name="   صفحه اصلی   "),
    path('indexk', views.indexk,name="   صفحه اصلی   "),
    path('index2', views.index2,name="       "),
    ##############################################################
    path('sing_up', views.sing_up,name="عضو شدن در سایت     "),
    path('cheklogins', views.cheklogins,name="  چک کردن عملیات لاگین  "), 
    path('chekout', views.chekout,name="   ایا لاگین شده یا نه   "), 
    path('logouts', views.logouts,name="    خارج شدن از حساب کاربری    "),
    path('', views.logins,name="logins"),
    
    path('Register', views.Register,name="   ثبت نام   "),
    #####################################################
 
  
    
    path('gallery_2', views.gallery_2,name="  عکس ها   "),
    path('create_img', views.create_img,name="    ثبت و ذخیره    "),
    path('list_img', views.list_img,name="     لیست   "),
    path('update_img', views.update_img,name="  ویرایش        "),
    path('delet_img', views.delet_img,name="   پاک کردن     "),
    #################################################
   
  
    
    ##############################################
    path('select_usertype', views.select_usertype,name="        "),
  
    ############################################
    path('answer_d', views.answer_d,name="   جواب  "),
    path('create_answer', views.create_answer,name="    ثبت و ذخیره    "),  
    path('update_answer', views.update_answer,name="  ویرایش        "),
    path('delet_answer', views.delet_answer,name="   پاک کردن     "),
    ###########################################
    path('padcast_d', views.padcast_d,name="  پادکست   "),
    path('create_padcast', views.create_padcast,name="    ثبت و ذخیره    "),
    path('list_padcast', views.list_padcast,name="     لیست   "),
    path('update_padcast', views.update_padcast,name="  ویرایش        "),
    path('delet_padcast', views.delet_padcast,name="   پاک کردن     "),
    ###########################################
    path('test_d', views.test_d,name="   تست  "),
    path('create_test', views.create_test,name="    ثبت و ذخیره    "),
    path('list_test', views.list_test,name="     لیست   "),
    path('update_test', views.update_test,name="  ویرایش        "),
    path('delet_test', views.delet_test,name="   پاک کردن     "), 
    ##########################################
    path('vidio_d', views.vidio_d,name="  ویدیو   "),
    path('create_vidio', views.create_vidio,name="    ثبت و ذخیره    "),
    path('list_vidio', views.list_vidio,name="     لیست   "),
    path('update_vidio', views.update_vidio,name="  ویرایش        "),
    path('delet_vidio', views.delet_vidio,name="   پاک کردن     "),    
    #################################################
    path('filteres', views.filteres,name="     جستجو کردن     "),
    path('filtered', views.filtered,name="    فیلتر کردن     "),
   
   #####################################################
    path('takhasos', views.takhasos,name="  انواع تخصص ها        "),
    path('nomoshavere', views.nomoshavere,name="      انواع مشاوره ها    "),
    path('savetakhasos', views.savetakhasos,name="       ثبت تخصص ها    "),
    path('savenomoshavere', views.savenomoshavere,name="       ثبت انواع مشاوره    "),
    path('list_filter/<int:pk>', views. list_filter,name="     فیلتر کردن انواع تخصص ها      "),
    ###################################
    path('user_type/', views.select_usertype, name='select_usertype'),
    path("verify_license/", views.verify_license, name="verify_license"),
    path("send_docs/", views.send_docs, name="send_docs"),
    ########################################################
  
    ]

  
    