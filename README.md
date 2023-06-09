# LiberOasis
A Django - React Book Library Website

Steps:
```
Two terminals need to be opened. One for running the django backend and another for running the react frontend.

First in terminal navigate to the directory, where you want to clone the repository. Then Run the below commands.
```
Clone the repository
 - `git clone https://github.com/sambit-git/LiberOasis.git`
 - `cd LiberOasis`

```
Now the Project repository is cloned! You can use the same terminal window for running the django backend server or the react frontend.

Since two terminals are needed, you open another terminal instance in the same LiberOasis directory.

Then as per below instructions run the commands in separate terminals.
```

Run Backend (Django Server) - Terminal-1
 - `cd backend`
 - `python -m venv venv`
 - `.\venv\Scripts\Activate.ps1`
 - `pip install -r requirements.txt`
 - `cd LiberOasis`
 - `python manage.py migrate`
 - `python manage.py loaddata authors`
 - `python manage.py loaddata books`
 - `python manage.py runserver 0.0.0.0:8000`

Run Frontend (React) - Terminal-2
 - `cd Frontend` 
 - `cd LiberOasis`
 - `npm install`
 - `npm start`