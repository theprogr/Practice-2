is_logged_in = True
is_admin = False

print("Is logged in:", is_logged_in)
print("Is admin:", is_admin)

has_access = is_logged_in and is_admin
print("Has full access:", has_access)
