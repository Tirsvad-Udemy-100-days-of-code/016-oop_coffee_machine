# OOP Coffee Machine

An object-oriented coffee machine in Python, solved as an assignment of Udemy's
*100 Days of Code: The Complete Python Pro Bootcamp*. The program takes a drink
order, checks that the ingredients are sufficient, takes coins, gives change and
makes the drink. It has no runtime dependencies, so it is easy to read, run and
compare with your own solution.

The classes and methods use the assignment's names:

| Class | Methods |
| --- | --- |
| `Menu` | `get_items`, `find_drink` |
| `CoffeeMaker` | `report`, `is_resource_sufficient`, `make_coffee` |
| `MoneyMachine` | `report`, `process_coins`, `make_payment` |

At the prompt you can type a drink name (`espresso`, `latte` or `cappuccino`),
`report` to print the resources and the money in the machine, or `off` to stop.

## Requirements

- Python 3.13 or newer.
- `venv` and `pip`, which come with Python (on Debian they are separate packages).
- Git, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

There are no runtime dependencies. `pytest`, `ruff` and `mypy` are installed
only for development, through the `dev` extra.

## Set up

Clone the repository and change into it:

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine.git
cd 016-oop_coffee_machine
```

Then create a local virtual environment named `.venv`, upgrade `pip` and install
the project in it.

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow it for this window only
with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

### Linux debian

```bash
sudo apt install python3 python3-venv python3-pip git
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Debian 13 (trixie) ships Python 3.13. On an older release, install Python 3.13
first (for example with `pyenv`) and use it to create the `.venv`.

### MacOS

```bash
brew install python@3.13 git
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To leave the virtual environment, run `deactivate`.

## Run

With the virtual environment active:

```bash
python -m coffee_machine
```

The installed command does the same:

```bash
coffee-machine
```

Example session:

```text
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 12
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.50 in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino): off
```

## Run the tests

With the virtual environment active:

```bash
python -m pytest
```

The linter and the strict type check that the project also uses:

```bash
ruff check .
mypy
```

## Continuous integration

The workflow in `.gitea/workflows/ci.yml` runs on Gitea Actions on every push and
pull request. It creates a virtual environment on Python 3.13, upgrades `pip`,
installs the project with the `dev` extra and runs `ruff check .`, `mypy` and
`python -m pytest`. GitHub does not read the `.gitea` folder, so a GitHub mirror
does not run it.

## Build the source documentation

The source uses Doxygen comments and the `Doxyfile` in the repository root. Install
Doxygen (`winget install DimitriVanHeesch.Doxygen` on Windows,
`sudo apt install doxygen` on Debian, `brew install doxygen` on MacOS), then run:

```bash
doxygen Doxyfile
```

The HTML documentation is written to `docs/doxygen/html/`; open `index.html` in a
browser. The output folder is ignored by git.

## Project layout

```text
.
├── src/coffee_machine/   The program
│   ├── constants.py      Menu, resources, coins, commands and messages
│   ├── menu.py           Menu and MenuItem
│   ├── coffee_maker.py   CoffeeMaker
│   ├── money_machine.py  MoneyMachine
│   ├── main.py           The loop that keeps the machine running
│   └── __main__.py       Lets `python -m coffee_machine` start the program
├── tests/                pytest tests
├── docs/                 Project documents (business case, plan, milestones, reviews)
├── Doxyfile              Doxygen configuration
├── pyproject.toml        Project configuration
└── .gitea/workflows/     Continuous integration
```

## License

GNU Affero General Public License v3.0, see [LICENSE](LICENSE).
