from django.contrib import admin

from .models import okrug, party, deputat, commision
# Register your models here.


class CommisionMembersInline(admin.TabularInline):

	model = commision.members.through
	extra = 1


@admin.register(okrug)
class OkrugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(party)
class PartyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(deputat)
class DeputatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'okrug','party','bDate']
    ordering = ['-chairman', '-vicechairman', 'first_name']


@admin.register(commision)
class CommisionAdmin(admin.ModelAdmin):
    inlines = [CommisionMembersInline]
    exclude = ('members',)
    prepopulated_fields = {'slug':('title',)}


