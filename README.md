<div align="center">

# Frost GO

</div>

# About The Repository
Frost GO is a search engine api made using python

# Contribution Guidelines

When contributing to `Frost GO`, whether on GitHub or in other community spaces:

- Be respectful, civil, and open-minded.
- Before opening a new pull request, try searching through the [issue tracker](https://github.com/IBK2024/Frost-GO/issues) for known issues or fixes.
- If you want to make code changes based on your personal opinion(s), make sure you open an issue first describing the changes you want to make, and open a pull request only when your suggestions get approved by maintainers.

## How to Contribute

### Prerequisites

In order to not waste your time implementing a change that has already been declined, or is generally not needed, start by [opening an issue](https://github.com/IBK2024/Frost-GO/issues/new/choose) describing the problem you would like to solve.

### Setup your environment locally
- First you will need to create a fork of the repository.
- Then clone the forked repository using the command but replacing`repository` with the url of the forked repository:
  ```bash
  git clone <repository>
  ```
- Then you will need to install virtualenv:
  ```bash
  # macOS/linux
  python3 -m pip install virtualenv

  # Windows 
  # You can also use `py -3 -m pip install virtualenv`
  python -m pip install virtualenv
  ```
- Then you will need to create virtual environment:
  ```bash
  # macOS/linux
  python3 -m venv .venv

  # Windows 
  # You can also use `py -3 -m venv .venv`
  python -m venv .venv
  ```
- Then you will need to create a `.env` file in the env directory with the content of `.env.example` in the same directory
- Activate the virtual environment
  ```bash
  # Mac and linux:
  source envname/bin/activate

  # Windows:
  envname\scripts\activate
  ```
- Then you will need to install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Implement your changes
To run:
```bash
python -m uvicorn src/main:app --reload
```
> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

> ⚠ To view all the api routes go to http://127.0.0.1:8000/docs
> 

### When your done
Create a pull request