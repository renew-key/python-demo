import os
password = os.environ.get("DB_P")
print(f"password = {password}")
username = os.environ.get("DB_U")
print(f"repository = {username}")
