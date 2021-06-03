from django.contrib import admin

from Customers.models import Contact, Process, Userinfo, Order, OrderUpdt
admin.site.register(Contact)
admin.site.register(Userinfo)
admin.site.register(Order)
admin.site.register(OrderUpdt)
admin.site.register(Process)
# Register your models here.
