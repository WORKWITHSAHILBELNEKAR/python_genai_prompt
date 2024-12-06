def replace_user_name_template(user_name):
    if len(user_name) < 3:
        print("UserName must have at least 3 characters.")
        return
    print(f"Hello {user_name}, How are you?")


replace_user_name_template("sahil")
