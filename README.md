# This is a site of blog was written on Django and uses Postgresql BD.

**Functionality:** 
* displays list of posts and certain post,
* pagination,
* comments under posts,
* ability to share a post by email,
* post's tags,
* recommended posts,
* custom manager, tags and template filters,
* site map,
* RSS feed,
* system of search via trigramm.

**How to use this project:**

1. Create a directory and install virtual environment in it: "python3 -m venv <your_env_name>" (for Linux) or "python -m venv <your_env_name>" (for Windows);
2. Activate your virtual environment: "source <your_env_name>/bin/activate" (for Linux) or "<your_env_name> /Scripts/activate" (for Windows);
3. Activate Git in your directory with command: "git init";
4. Clone files from this repository to yours with command: "git clone https://github.com/VasiliyHaroshka/blog.git";
5. Install necessary libraries from requirements.txt with command: "pip install -r requirements.txt";
6. Move to directory with file manage.py and launch a local sever on your PC with command: "python manage.py runserver".