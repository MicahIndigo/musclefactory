# Muscle Factory

Muscle Factory is a full-stack Django fitness membership platform where users can browse gym classes and unlock booing access by purchasing a membership via Stripe payments.

## Live Features

- User registration & login
- Member profile system
- Gym class listings
- Membership payment system (Stripe test mode)
- Access control (members vs non-members)
- Mobile-first Bootstrap UI


---

## User Goals

Users can:
- Create an account
- Purchase a gym membership
- Access and book fitness clases
- View class details on mobile or desktop

---

## Tech Stack

- Python
- Django
- SQLite (dev)
- Stripe API (payments)
- Bootstrap 5 (mobile-first UI)
- HTML/CSS

## Apps Structure

- `core` - homepage
- `accounts` - authentication
- `profiles` - user membership profile
- `classes` - gym classes + bookings
- `checkout` - Stripe payment logic

---

## Stripe Test Payment

Test card:
- 4242 4242 4242 4242
- Any future expiry date
- Any CVC


---


```bash
git clone <https://github.com/MicahIndigo/musclefactory.git>
cd musclefactory
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver