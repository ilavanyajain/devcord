# Devcord

Devcord is a modern, developer-friendly chat application inspired by Discord, built with Django. It supports password-protected chat rooms, in-app notifications, file sharing (coming soon), and is installable as a Progressive Web App (PWA) for a native-like experience on desktop and mobile.

---

## Features

- **Password-Protected Rooms:** Only users with the correct password can join a room.
- **Admin Room Creation:** The first user to create a room sets the password and becomes the admin.
- **In-App Notifications:** Get browser pop-up notifications for new messages.
- **Responsive Design:** Works beautifully on desktop and mobile.
- **PWA Support:** Install Devcord to your home screen for a native app feel.
- **Custom Branding:** Easily change the logo and favicon.
- **(Planned) File Sharing:** Upload and share files in chat rooms.

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/ilavanyajain/devcord.git
cd devcord
```

### 2. Set Up a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Run the Development Server

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Deployment (Render)

1. **Push your code to GitHub.**
2. **Create a new Web Service on [Render](https://render.com/):**
   - **Build Command:**  
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   - **Start Command:**  
     ```
     gunicorn devcord.wsgi:application
     ```
   - **Environment Variables:**
     - `DJANGO_SETTINGS_MODULE=devcord.settings`
     - `SECRET_KEY=your-very-secret-key`
     - `DEBUG=False`
3. **Add your Render URL to `ALLOWED_HOSTS` in `devcord/settings.py`.**
4. **Trigger a deploy and visit your live app!**

---

## PWA (Add to Home Screen)

- On mobile or desktop, open Devcord in your browser.
- Use the browser menu to "Add to Home Screen."
- Enjoy a native app experience!

---

## Customization

- **Logo:** Replace `static/devcord-logo.jpg` with your own.
- **Favicon:** Replace `static/favicon.ico`.
- **Colors:** Edit CSS in `templates/home.html` and `templates/room.html`.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE) 