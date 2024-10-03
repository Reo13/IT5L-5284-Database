from database.Database import Database

db = Database('localhost', 'root', '', 'blog_mantalaba')

while True:

    print("[1] Register \n [2] Login \n [3] Log-Out \n [4] Create Blog \n [5] Fetch All \n [x] Exit")
    choice = input()

    if choice == 'x':
        break

    if choice == '1':
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")

        db.register(name, username, password)

    elif choice == '2':
        username = input("Please Enter Your Username: ")
        password = input("Please Enter Your Password: ")

        user = db.login(username, password)

        if not user:
            print("Wrong username or password!")
            continue
        print("Login Success!")

    elif choice == '3':
        db.logout()

    elif choice == '4':
        if db.is_logged_in():
            post = input("Input Post: ")
            db.create_blog(post)

        else:
            print("Please login First!")
    elif choice == '5':
         blogs = db.fetch_blogs()
         for blog in blogs:
             print(blog[1])