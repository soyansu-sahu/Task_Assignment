from django.contrib import admin
from task_app.models import User, Team, Task

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'last_login', 'first_name', 'last_name', 'is_team_leader')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team_leader')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'assigned_team', 'status', 'started_at', 'completed_at')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # print(db_field)
        # print("=")
        # print(request.META)
        if db_field.name == "assigned_team":

            kwargs["queryset"] = User.objects.all()
        return super(TaskAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
