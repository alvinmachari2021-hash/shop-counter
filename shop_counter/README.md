# Group 8 Python Project - Shop Counter

## Project Overview
Briefly describe your project:
- What it does (show products, buy items, reduce stock, keep sales history)
- Why you built it (learning Python, OOP, CLI, persistence)
- Any extra goals (practice teamwork, Git workflow)

## Features
List the main functionalities:
- Show available products with prices and stock
- Buy items and automatically update stock
- Save each sale to a file for persistence
- View past sales history

## User Roles / Team Responsibilities
- Person A → data.py (products and prices)
- Person B → inventory.py (show products, update stock)
- Person C → sales.py (buy items, save sales)
- Person D → main.py (menu and connects everything)
- Person E → tests + README (testing and documentation)

## Project Structure
List the main files and their purpose:
## How to Run
Explain step-by-step:
1. Open terminal or command prompt
2. Navigate to project folder
3. Run: `python -m shop_counter.main`
4. Follow the menu to show products, buy items, or view sales

## How to Test
Explain how to run tests:
- Inventory tests: `pytest tests/test_inventory.py`
- Sales tests: `pytest tests/test_sales.py`
- Briefly explain what each test checks (stock reduction, invalid product, sales file)

## Technologies Used
- Python 3.x
- JSON for sales persistence
- Git for version control

## Workflow / Git Process
- Each member forked the repo, cloned it, worked on their file
- Committed and pushed changes
- Created Pull Requests to merge into main branch
- Used a branching workflow to keep work organized

## Optional: Learning Outcomes
- Modular Python design
- OOP concepts
- File-based persistence
- CLI interface development
- Team collaboration and Git workflow
### How to Run Tests
From the project root:

```bash
export PYTHONPATH=$(pwd)
pytest tests/