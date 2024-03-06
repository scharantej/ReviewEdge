## Project: Create a Simple Blog Application

### HTML Files

- **main.html** (Homepage): Displays a list of blog posts with titles and summaries.
- **post.html** (Post Page): Displays the full content of a blog post, including title, author, date, and body.
- **login.html** (Login Page): Enables users to log in to the application.
- **admin.html** (Admin Page): Restricted to administrators, allows creation, editing, and deletion of posts.

### Routes

- **GET / (main.html)**: Homepage displays a list of blog posts.
- **GET /post/<int:post_id> (post.html)**: Post page displays the full content of a blog post.
- **GET /login (login.html)**: Login page prompts the user for credentials.
- **POST /login**: Validates the user's credentials and sets a session cookie if successful.
- **GET /admin (admin.html)**: Admin page allows administrators to manage blog posts.
- **POST /admin/create**: Creates a new blog post.
- **POST /admin/update/<int:post_id>**: Updates an existing blog post.
- **POST /admin/delete/<int:post_id>**: Deletes a blog post.
- **POST /logout**: Invalidates the session cookie and logs the user out.