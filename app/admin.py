from django.contrib import admin
from app.models import User, Project, Service, Education, Experience

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'users')
    list_filter = ('name',)
    search_fields = ('name', 'id',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'users',
                    'institute', 'start_date', 'end_date')
    list_filter = ('degree',)
    search_fields = ('degree', 'id',)


class ExperirnceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'users',
                    'company', 'location', 'start_date', 'end_date')
    list_filter = ('name',)
    search_fields = ('name', 'id',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'gender', 'city',
                    'country', 'phone', 'degree', 'image', 'created_at', 'password', 'date_of_birth')
    list_filter = ('first_name',)
    search_fields = ('first_name', 'id',)
    ordering = ('email', 'id',)
    filter_horizontal = ()

    add_fieldset = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'id', 'date_of_birth', 'first_name', 'created_at',  'last_name', 'gender', 'phone', 'address', 'password1', 'password2', 'image', 'degree', 'country', 'city'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'date_of_birth', 'last_name', 'created_at', 'gender', 'phone', 'address', 'password1', 'password2', 'image', 'degree', 'country', 'city'),
        }),
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'users')
    list_filter = ('id',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperirnceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Service, ServiceAdmin)
