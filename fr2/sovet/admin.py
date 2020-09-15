from django.contrib import admin

from .models import okrug, party, deputat, commision
# Register your models here.


@admin.register(okrug)
class OkrugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(party)
class PartyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(deputat)
class DeputatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'okrug','party','bDate']
    ordering = ['-chairman', 'first_name']


@admin.register(commision)
class CommisionAdmin(admin.ModelAdmin):
    pass


