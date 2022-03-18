



from orders.models import OrderItems
from orders.models import OrderItemAppointments
order_items = OrderItems.objects.all()

for item in order_items:
	for _ in range(item.service.follow_up):
		OrderItemAppointments.objects.create(order_item = item, service_time = item.order.services_time)




obj = OrderItemAppointments.objects.filter(order_item__order__id = 174)
for o in obj:
	print(o.service_time)



* */1 * * * /path/to/python /path/to/project/root/manage.py runcrons

* */1 * * * // /home/ubuntu/EXFX-Django/manage.py runcrons


from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

all_apps = ("django_auth", "users", "stores", "cart", "orders", "promotions", "accounts", "chat_assistant", "master_data")

for app in all_apps:
	app_models = apps.get_app_config(app).get_models()
	for model in app_models:
		print(model)


string = '''
<class 'django_auth.models.Token'>
<class 'users.models.Role'>
<class 'users.models.UserProfile'>
<class 'users.admin.ExfxUserLead'>
<class 'users.admin.EXFXUser'>
<class 'stores.models.StoresDetails'>
<class 'stores.models.StoreImages'>
<class 'stores.models.Gender'>
<class 'stores.models.ServiceCategory'>
<class 'stores.models.StoreServices'>
<class 'stores.models.Amenities'>
<class 'stores.models.StoreAmenities'>
<class 'stores.models.StoreTimeSlot'>
<class 'stores.models.StoreGeneralOpeningHours'>
<class 'stores.models.StoreSpecificClosingHours'>
<class 'stores.models.StoreInventory'>
<class 'stores.models.StoreRecharges'>
<class 'stores.models.StoreRechargesHistory'>
<class 'cart.models.Cart'>
<class 'orders.models.ServiceStatus'>
<class 'orders.models.Orders'>
<class 'orders.models.OrderItems'>
<class 'orders.models.OrderItemAppointments'>
<class 'orders.models.ReviewQuestions'>
<class 'orders.models.OrderReviews'>
<class 'orders.models.ReviewQuestionRelations'>
<class 'orders.models.PaymentDetails'>
<class 'orders.admin.OngoingOrders'>
<class 'orders.admin.CompletedOrders'>
<class 'promotions.models.Promotions'>
<class 'promotions.models.Offers'>
<class 'promotions.models.StoreOffers'>
<class 'promotions.models.ServiceOffers'>
<class 'promotions.models.UserOffers'>
<class 'promotions.models.Banners'>
<class 'accounts.models.StoreAccounts'>
<class 'accounts.models.PaymentHistory'>
<class 'accounts.models.MerchantRecharges'>
<class 'accounts.models.MerchantRechargesHistory'>
<class 'chat_assistant.models.ChatThreadStatus'>
<class 'chat_assistant.models.ChatThread'>
<class 'chat_assistant.models.ChatMessages'>
<class 'chat_assistant.models.ChatTag'>
<class 'chat_assistant.models.ChatTagRelation'>
<class 'chat_assistant.models.FAQType'>
<class 'chat_assistant.models.FAQs'>
<class 'chat_assistant.models.FAQVotes'>
<class 'master_data.models.MasterContent'>
<class 'master_data.models.MasterValues'>
<class 'master_data.models.MasterVariables'>
<class 'master_data.models.States'>
<class 'master_data.models.Sgst'>
<class 'master_data.models.Cgst'>
<class 'master_data.models.Cities'>
'''

lines = string.split('\n')
for line in lines:
	a = line.split('.')[0][8:]
	b = line.split('.')[-1][:-2]
	print(f'{a} - {b}')



django_auth - Token
users - Role
users - UserProfile
users - ExfxUserLead
users - EXFXUser
stores - StoresDetails
stores - StoreImages
stores - Gender
stores - ServiceCategory
stores - StoreServices
stores - Amenities
stores - StoreAmenities
stores - StoreTimeSlot
stores - StoreGeneralOpeningHours
stores - StoreSpecificClosingHours
stores - StoreInventory
stores - StoreRecharges
stores - StoreRechargesHistory
cart - Cart
orders - ServiceStatus
orders - Orders
orders - OrderItems
orders - OrderItemAppointments
orders - ReviewQuestions
orders - OrderReviews
orders - ReviewQuestionRelations
orders - PaymentDetails
orders - OngoingOrders
orders - CompletedOrders
promotions - Promotions
promotions - Offers
promotions - StoreOffers
promotions - ServiceOffers
promotions - UserOffers
promotions - Banners
accounts - StoreAccounts
accounts - PaymentHistory
accounts - MerchantRecharges
accounts - MerchantRechargesHistory
chat_assistant - ChatThreadStatus
chat_assistant - ChatThread
chat_assistant - ChatMessages
chat_assistant - ChatTag
chat_assistant - ChatTagRelation
chat_assistant - FAQType
chat_assistant - FAQs
chat_assistant - FAQVotes
master_data - MasterContent
master_data - MasterValues
master_data - MasterVariables
master_data - States
master_data - Sgst
master_data - Cgst
master_data - Cities


















