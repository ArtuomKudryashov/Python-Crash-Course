user_roles = ("admin", "editor", "viewer")
for  role in  user_roles:
    print(role)
print("admin" in user_roles)
print("Chiki" in user_roles)
print(user_roles[0])
print(type(user_roles))

# Итерация  с одним  элементом

my_tuple= ("admin",)
print(type(my_tuple))

#unpuck less<=2 dosn't work

role_1, role_2,role_3 = user_roles
print(role_1)
print(role_2)
print(role_3)

#I have to  print 2
role_1, role_2, _ = user_roles
print(role_1)
print(role_2)





