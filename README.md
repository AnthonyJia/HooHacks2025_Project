# 🥗 LeftOver Hub (HooHacks2025 Project – Food Sharing Web App)

## 🌟 Purpose
This Django web application was built during **HooHacks 2025** to help fight food waste and food insecurity. It allows **families and restaurants** to share surplus or soon-to-expire food by posting it online so others nearby can access it. The goal is to reduce food waste while providing free food to those who need it or simply want to avoid letting good food go uneaten.

## 💡 How It Works
- **Post Food**: Users (families or restaurants) can create listings with the food name, expiration date, and pickup location.
- **Browse Listings**: Anyone can browse available food listings nearby.
- **Pick Up**: If interested, users can visit the listed location before the deadline to pick up the food for free.

This project promotes **sustainability**, **community sharing**, and supports people facing **food insecurity**.

## 🛠️ How to Install & Run Locally

> ⚠️ This app is not currently deployed online. Follow the steps below to run it on your local machine.

```bash
# Clone the repository
git clone https://github.com/AnthonyJia/HooHacks2025_Project.git
cd HooHacks2025_Project

# (Optional but recommended) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
python3 -m pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver

# Open your browser and go to:
# http://127.0.0.1:8000

