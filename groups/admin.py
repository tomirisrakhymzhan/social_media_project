from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
admin.site.register(models.Group)

'''
class OrderItemTabular(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'ordered_date', 'coupon', 'payment', 'shipping_address', 'status',
                    'refund_requested', 'refund_granted', 'ref_code']
    inlines = [
        OrderItemTabular,
    ]

admin.site.register(Order, OrderAdmin)'''