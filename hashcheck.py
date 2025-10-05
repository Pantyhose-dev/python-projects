import bcrypt

# The hashed password
hashed_password = '$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom'

# The password you want to check
password = 'your_password_here'

# Check if the password matches the hash
if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
    print("Password matches!")
else:
    print("Password does not match.")
