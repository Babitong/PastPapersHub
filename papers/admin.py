from django.contrib import admin
from . models import Level,Subject,PastPaper,DownloadLog
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin



class papersAdmin(admin.ModelAdmin):
    
    list_display = ('subject','year', 'paper_number')
    list_filter = ('subject','year', 'paper_number')
    search_fields = ('subject','year', 'paper_number')
    

class subjectsAdmin(admin.ModelAdmin):
    
    list_display = ('name','code', 'level')
    list_filter = ('name','code', 'level')
    search_fields = ('name','code', 'level')

class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ('paper','ip_address','downloaded_at')
    list_filter = ('paper','ip_address','downloaded_at')

admin.site.register(Level)
admin.site.register(Subject,subjectsAdmin)
admin.site.register(PastPaper,papersAdmin)
admin.site.register(DownloadLog,DownloadLogAdmin)



# Register your models here.
