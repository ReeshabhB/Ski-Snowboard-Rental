# slope-rental 🎿

A command-line ski and snowboard rental shop management system written in Python. Tracks customers, manages equipment inventory, handles rentals, and calculates charges.

## Features

- Add and look up customers by ID
- Rent skis and snowboards with automatic inventory management
- Close out rentals and calculate charges automatically
- View all open rentals or all rentals for a specific customer
- Track total shop income and statistics

## Getting Started

**Requirements:** Python 3.7+

```bash
git clone https://github.com/yourusername/slope-rental.git
cd slope-rental
python main.py
```

No external dependencies — runs on the standard library.

## Usage

When you run `main.py`, you'll see an interactive menu:

```
------ MAIN MENU ------
1. Add new customer
2. Display a customer
3. Display all rentals for a customer
4. Display all OPEN rentals
5. Make new rental
6. Return a rental
7. Display inventory
8. Show statistics
9. Run test
0. Exit
```

**Typical workflow:**
1. Add a customer (option 1) — you'll receive their ID
2. Create a rental for that customer (option 5)
3. When they return equipment, complete the rental (option 6) — the charge is calculated automatically

## Pricing

| Equipment | Rate |
|-----------|------|
| Skis | $15 / hour |
| Snowboards | $10 / hour |

Charges are calculated as: `(skis × $15 + snowboards × $10) × hours`

## Project Structure

```
slope-rental/
├── shop.py     # Core classes: Customer, Rental, Shop
├── main.py     # CLI menu and test harness
└── README.md
```

### Classes

- **`Customer`** — stores last name, phone number, and an auto-assigned unique ID
- **`Rental`** — tracks equipment rented, hours, customer reference, and open/closed status
- **`Shop`** — manages inventory, customer list, rentals list, and total income

## Running the Test

Option 9 from the menu runs a built-in test that creates sample customers, makes rentals, completes one, and prints a summary — useful for a quick sanity check.

## Potential Improvements

- Persist data between sessions (JSON or SQLite)
- Input validation for negative numbers and non-integer input
- Unit tests with `pytest`
- Configurable rental rates per shop instance

## License

MIT
