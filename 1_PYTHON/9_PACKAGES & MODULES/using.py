import my_library.my_package_3.greeting 

my_library.my_package_3.greeting .namaskara(" Nandy") 


from my_library.my_package_3 import greeting

greeting.goodbye("Nandy")


from my_library.my_package_3 import greeting as greet

greet.namaskara("Nandy")


from my_library.my_package_3.greeting import namaskara as nm

nm(" Nandy")