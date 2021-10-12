from django.contrib import admin

# Register your models here.
from location.models import Location, TravelType, TravelTime, TransportType, Difficulty

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('title', 'get_travel_type', 'get_transport_type', 'get_travel_time', 'get_difficulty', 'ostan', 'shahr', 'approved')

    def get_travel_type(self, obj):
        tags = []
        for d in obj.travel_type.all():
            tags.append(d.title_P)
        return tags
    get_travel_type.short_description = "نوع سفر"

    def get_transport_type(self, obj):
        tags = []
        for d in obj.transport_type.all():
            tags.append(d.title_P)
        return tags

    get_transport_type.short_description = "حمل و نقل"

    def get_travel_time(self, obj):
        tags = []
        for d in obj.travel_time.all():
            tags.append(d.title_P)
        return tags

    get_travel_time.short_description = "زمان سفر"

    def get_difficulty(self, obj):
        tags = []
        for d in obj.difficulty.all():
            tags.append(d.title_P)
        return tags

    get_difficulty.short_description = "سختی سفر"

admin.site.register(Location, LocationAdmin)
admin.site.register(TravelType)
admin.site.register(TravelTime)
admin.site.register(TransportType)
admin.site.register(Difficulty)
