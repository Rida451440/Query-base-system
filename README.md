# Corvit Query Assistant

An automated query response system for **Corvit Systems, Rawalpindi Campus**. Students and visitors ask about courses, fees, schedules and contact details, and the assistant answers instantly from the information published on the Corvit website, in **English or Roman Urdu**.

It was built so the campus team no longer has to reply to the same calls and messages one by one.

Built with **Flask**, **SQLite** and **scikit-learn**, with optional AI-written answers using the **Claude API**.

## Features

- **Answers from the Corvit website.** Courses, fee structure, class schedule, campus address, phone and how to apply
- **English and Roman Urdu.** Questions such as "AI course ki fee kitni hai?" or "Python course kab start hogi?" work as well as English ones
- **Starter data included.** The assistant works immediately with the Rawalpindi fees and schedule pages already loaded
- **Website crawler.** Refreshes the data from the Corvit website with one command or one button. It respects `robots.txt` and waits between pages
- **Optional AI answers.** With an API key, Claude reads the matching website information and writes a short, clear reply, using only the supplied facts. Without a key, the assistant shows the matching website information directly
- **Admin page.** Refresh the website data, add extra information that is not on the website, and review questions the assistant could not answer
- **Voice input** in Google Chrome
- **Responsive design** in Corvit's red and white theme, for desktop and mobile

## How it works

1. A visitor asks a question in the chat.
2. The assistant searches the stored website information using TF-IDF similarity, with support for Roman Urdu keywords and spelling differences.
3. Questions unrelated to Corvit are not answered. The visitor is pointed to the campus phone and WhatsApp number.
4. If an API key is set, the best matching information is sent to Claude, which writes the reply using only that information.
5. Questions the assistant could not answer are saved so the admin can add the missing information.

## Tech stack

| Part | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Search | scikit-learn (TF-IDF, cosine similarity) |
| Crawler | requests, BeautifulSoup |
| AI (optional) | Claude API (Anthropic) |
| Frontend | HTML, CSS, JavaScript |

## Project structure

```
corvit-query-assistant/
├── app.py              # Flask application, chat and admin routes
├── bot.py              # Search and answer logic (with or without AI)
├── crawl_website.py    # Reads the Corvit website and stores its text
├── seed_knowledge.py   # Starter data: Rawalpindi fees, schedule and contact details
├── database.py         # Database setup
├── config.py           # Organisation details and the pages to crawl
├── requirements.txt
├── templates/
│   ├── index.html      # Chat page
│   └── admin.html      # Admin page
└── static/
    └── style.css       # Styling (red and white theme)
```

## Getting started

### Prerequisites
- Python 3.9 or later
- An Anthropic API key (optional, for AI-written answers)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

Open **http://127.0.0.1:5000** in your browser. The database is created automatically on the first run.

### Add the Corvit logo (optional)

Save the logo as `static/logo.png` (`.webp`, `.jpg` and `.svg` also work). Without it, the page loads the logo from the Corvit website.

### Enable AI-written answers (optional)

Set your API key as an environment variable before running the app.

```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your-key-here"

# macOS / Linux
export ANTHROPIC_API_KEY="your-key-here"
```

> **Never commit your API key to GitHub.** Keep it in an environment variable only.

To use a different Claude model, set the `CLAUDE_MODEL` environment variable. The admin page shows whether AI answers are active.

## Refreshing the website data

```bash
python crawl_website.py
```

You can also click **Refresh website data** on the admin page. The pages to read are listed in `config.py` under `crawl_urls`. To go back to the starter data, run `python database.py reset`.

## Admin page

Open **http://127.0.0.1:5000/admin?key=admin123**

- **Refresh website data** reads the website again
- **Extra information** lets you add facts that are not on the website, such as a discount or an admission date. They take effect immediately
- **Unanswered queries** lists the questions the assistant could not answer

The default admin key is `admin123`. Change it before real use by setting the `ADMIN_KEY` environment variable.

## Using it for another organisation

Edit `config.py` (name, contact details, logo and the website pages to crawl), then run `python crawl_website.py`. The chat page, footer and answers update automatically.

## Important notes

- The starter fee data is the **2025 Rawalpindi fee structure** and the schedule is for **August 2026**. Run the crawler to get the latest information. The assistant always advises confirming fees with the campus.
- Use the crawler responsibly and get permission from the website owner first.
- Voice input works in Google Chrome only.

<!--
## Screenshots
Add your screenshots to a `screenshots/` folder, then remove these comment markers.

![Chat page](screenshots/chat.png)
![Admin page](screenshots/admin.png)
-->

## Author

**Rida Shahzadi**
BS Computer Science, Arid Agriculture University, Rawalpindi
Developed during an internship at Corvit Systems, Rawalpindi.

## License

This project was developed for educational and internship purposes.
