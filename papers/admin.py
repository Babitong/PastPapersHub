from django.contrib import admin
from . models import Level,Subject,PastPaper,DownloadLog,EducationType,Department
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('level','name')
    list_filter = ('level','name')
    search_fields = ('level','name')

class LevelAdmin(admin.ModelAdmin):
    list_display = ('education_type','name')
    list_filter = ('education_type','name')
    search_fields = ('education_type','name')

class papersAdmin(admin.ModelAdmin):
    
    list_display = ('subject','year', 'paper_number')
    list_filter = ('subject','year', 'paper_number')
    search_fields = ('subject','year', 'paper_number')
    

class subjectsAdmin(admin.ModelAdmin):
    
    list_display = ('name','code', 'level')
    list_filter = ('name','code', 'level','department')
    search_fields = ('name','code', 'level','department')

class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ('paper','ip_address','downloaded_at')
    list_filter = ('paper','ip_address','downloaded_at')

admin.site.register(Level, LevelAdmin)
admin.site.register(EducationType)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject,subjectsAdmin)
admin.site.register(PastPaper,papersAdmin)
admin.site.register(DownloadLog,DownloadLogAdmin)



# Register your models here.
