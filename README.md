custom_app_names
================

Django app that allows you to customize your app names on the admin site. Created out of frustration, and based on this StackOverflow response: http://stackoverflow.com/questions/612372/can-you-give-a-django-app-a-verbose-name-for-use-throughout-the-admin#615760

### Installation

1. Clone this project into your project's directory

2. Add `appnames` to `INSTALLED_APPS` in `settings.py`

3. In your project's `urls.py`, add the following:

        from appnames.sites import AdminSite
        from django.contrib import admin
          
        admin.site = AdminSite()

4. Put the new name for your app in the `verbose_name` property of that app's `admin.py`:

        class MyAppAdmin(admin.ModelAdmin):
            verbose_name = "New Name for App"

You have to have the same value for `verbose_name` in each `ModelAdmin` definition, if you want to have those models appear under the same app name in the admin site. I find the following helpful if I have a bunch of `ModelAdmin`s to change:

        class MyAppAdminBase(admin.ModelAdmin):
            verbose_name = "New Name for App"
    
        class SomeOtherAdmin(MyAppAdminBase):
            pass
    
        class AnotherAdmin(MyAppAdminBase):
            pass
        ...
