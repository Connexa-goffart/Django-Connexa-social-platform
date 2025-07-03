# Connexa Social Platform

Connexa is a modern Django-based social platform for connecting users, sharing posts, joining groups, and organizing events. The project features a clean, responsive UI inspired by leading social networks, with a focus on usability and extensibility.

## Features

- User registration, login, and profile management
- Home feed with posts, comments, likes, saves, shares, and reposts
- Modern card-based UI for posts and events
- Group creation, joining, and group feeds
- Event creation, registration, and attendee management
- Private messaging between users
- Search for users, posts, and groups
- Responsive design using Tailwind CSS
- Clickable usernames and group names throughout the UI
- Clean, modern comment section with live toggling

## Project Structure

```
├── bucosa/                # Main Django project folder
│   ├── activities/        # App for posts, events, comments, etc.
│   ├── users/             # App for user profiles, auth, groups, etc.
│   ├── media/             # Uploaded media (ignored by git)
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates (ignored by git)
│   ├── db.sqlite3         # SQLite database (ignored by git)
│   └── manage.py          # Django management script
├── .gitignore             # Git ignore rules (media, templates, migrations, etc.)
├── README.md              # This file
├── requirement.txt        # Python dependencies
└── ...
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
<<<<<<< HEAD
   git clone <https://github.com/Connexa-goffart/Django-Connexa-social-platform.git>
=======
   git clone  https://github.com/Connexa-goffart/Django-Connexa-social-platform.git
>>>>>>> 4f4636a3f4c2840d86c5e13f8fb5588a2d90ba6f
   cd Django-social-platform-Connexa
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirement.txt
   ```

4. **Apply migrations:**
   ```sh
   python bucosa/manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```sh
   python bucosa/manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python bucosa/manage.py runserver
   ```

7. **Access the app:**
   - Open your browser and go to `http://127.0.0.1:8000/`

## Development Notes

- **Static files:** Place custom CSS/JS/images in `bucosa/static/`.
- **Media uploads:** User-uploaded files are stored in `bucosa/media/` (ignored by git).
- **Templates:** All HTML templates are in `bucosa/templates/` (ignored by git).
- **Migrations:** All Django migrations are ignored by git for a clean repo.
- **Tailwind CSS:** The UI uses Tailwind via CDN for rapid prototyping and modern design.

## Contributing

1. Fork the repository and create your branch from `main`.
2. Make your changes and commit with clear messages.
3. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For questions or support, open an issue or contact the maintainer:

**Maintainer:** Kithulovali goffart  jean Marc 
**Email:** kithulovalibin@gmail.com
