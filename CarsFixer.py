from Storge import Storge
from Products import Products
from Services import Services
from RegisterLogin import RegisterLogin
from Customers import Customer
    
storge = Storge()

# Adding products to the Storge
storge.add_product(Products("Car_Tent", 2500, 50))
storge.add_product(Products("Dash_Cam", 700, 30))
storge.add_product(Products("Phone_Car_Holder", 80, 20))
storge.display_products()

print()

storge.add_service(Services("Tire_change", 3000, True, '2024-10-23', '7PM'))
storge.add_service(Services("Oil_change", 115, True, '2024-10-27', '2PM'))
storge.add_service(Services("Car_maintenance", 350, True, '2024-10-29', '11AM'))
storge.display_services()

print()

custumer = Customer('osama', 'osama_f', '123bb')
registerLogin = RegisterLogin()

registerLogin.register_customer(custumer)
registerLogin.login_customer('osama_f', '123bb')

# custumer = registerLogin.get_customer('osama_f')

custumer.product_cart.add_to_cart(storge.get_product(0), 10)
custumer.product_cart.add_to_cart(storge.get_product(1), 20)
custumer.product_cart.add_to_cart(storge.get_product(2), 4)

custumer.checkout_products_cart()
print()
custumer.service_cart.add_to_cart(storge.get_services(0), '2024-10-23', '7PM')
custumer.checkout_service_cart()

