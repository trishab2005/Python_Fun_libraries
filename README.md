
# 🐍 Python Fun Libraries

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20%26%20Exploration-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A collection of Python experiments and mini-projects exploring interesting libraries, useful modules, and practical programming concepts.

This repository is a hands-on learning space for discovering how Python libraries can simplify everyday tasks, automate workflows, retrieve information, and build interactive applications.

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Objectives](#-objectives)
- [Technologies Used](#-technologies-used)
- [Project Highlights](#-project-highlights)
- [Getting Started](#-getting-started)
- [Installation](#-installation)
- [Running the Programs](#-running-the-programs)
- [Example: Movie Information Finder](#-example-movie-information-finder)
- [Learning Outcomes](#-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [Author](#-author)

## 📖 About the Project

**Python Fun Libraries** is a personal Python learning repository focused on experimenting with libraries and exploring their practical applications.

Instead of learning libraries only through theory, this project emphasizes writing and running small programs to understand how different modules work.

The repository can grow to include projects involving:

- Data retrieval using APIs
- HTTP requests and JSON processing
- Movie information and ratings
- Automation scripts
- Data manipulation and visualization
- Interactive applications
- Experiments with third-party Python libraries

The goal is to improve Python programming skills through practical implementation.

## 🎯 Objectives

- Explore useful Python libraries and their functionalities.
- Understand how to install and import external packages.
- Work with APIs and process JSON responses.
- Practice exception handling and debugging.
- Build small, reusable Python programs.
- Strengthen problem-solving and application development skills.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pip | Python package installation |
| Virtual Environment (`venv`) | Project dependency isolation |
| Requests | HTTP requests and API integration |
| JSON | Processing structured API responses |
| Git and GitHub | Version control and project hosting |

Additional libraries may be included as the repository evolves.

## ✨ Project Highlights

- **Library Exploration:** Experiment with third-party Python packages.
- **API Integration:** Retrieve information from external services.
- **Error Handling:** Handle network failures, invalid responses, and unexpected errors.
- **Practical Examples:** Learn through small, runnable scripts.
- **Beginner-Friendly Code:** Focus on readability and understanding.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3
- pip
- Git

Check your Python installation:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

### Clone the Repository

```bash
git clone https://github.com/trishab2005/Python_Fun_libraries.git
```

Navigate to the project directory:

```bash
cd Python_Fun_libraries
```

## 📦 Installation

It is recommended to use a virtual environment to keep project dependencies separate from your system Python installation.

### macOS / Linux

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required dependencies, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

If the repository does not contain a `requirements.txt` file, install the packages required by the specific program you want to run.

### Windows

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

## ▶️ Running the Programs

Navigate to the relevant Python script and execute it using Python.

For example:

```bash
python example.py
```

Replace `example.py` with the actual filename of the program you want to run.

Some scripts may require additional configuration, API keys, or package installations. Refer to the corresponding source code before execution.

## 🎬 Example: Movie Information Finder

One example of a Python library experiment is a movie information finder using the OMDb API.

The program accepts a movie title and retrieves information such as:

- Movie title
- Release year
- Genre
- Director
- IMDb rating
- Plot summary

### Libraries Used

```python
import requests
```

### Example API Request

```python
import requests

api_key = "YOUR_OMDB_API_KEY"

url = "https://www.omdbapi.com/"

params = {
    "t": "Carrie",
    "apikey": api_key
}

try:
    response = requests.get(
        url,
        params=params,
        timeout=(5, 30)
    )

    response.raise_for_status()
    movie = response.json()

    if movie.get("Response") == "True":
        print("Title:", movie.get("Title"))
        print("Year:", movie.get("Year"))
        print("Genre:", movie.get("Genre"))
        print("Director:", movie.get("Director"))
        print("IMDb Rating:", movie.get("imdbRating"))
        print("Plot:", movie.get("Plot"))
    else:
        print("Error:", movie.get("Error"))

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

except ValueError:
    print("Invalid JSON response received.")

```

Get an API key from [OMDb API](https://www.omdbapi.com/apikey.aspx) before running this example.

**Security note:** Never commit real API keys or other credentials to GitHub. Use environment variables for sensitive configuration.

## 📸 Screenshots

### Fetching IMDB live rating 
<img width="727" height="647" alt="Screenshot 2026-10-22 at 11 35 15 AM" src="https://github.com/user-attachments/assets/74b84d3a-81ea-4b87-a315-98645a2ddbea" />

### Drawing a circuit
<img width="521" height="346" alt="Screenshot 2026-10-22 at 11 36 38 AM" src="https://github.com/user-attachments/assets/5a8406f3-f0fe-42cf-a27b-ab29c6c81ad2" />

### Tabulation
<img width="565" height="319" alt="Screenshot 2026-10-22 at 11 38 03 AM" src="https://github.com/user-attachments/assets/278d1e6b-41b2-4656-ae6b-eb65ccd587b2" />

### Simple Dashboard without using FAST-API
<img width="1440" height="900" alt="Screenshot 2026-10-22 at 11 37 01 AM" src="https://github.com/user-attachments/assets/c0e82875-a47c-44e5-96a7-e2e2f29d532d" />
<img width="1440" height="900" alt="Screenshot 2026-10-22 at 11 37 25 AM" src="https://github.com/user-attachments/assets/980a125b-4b74-4f10-b4ac-7c06cf5bed45" />

## 📚 Learning Outcomes

Working with Python libraries helps develop practical experience in:

- Importing and using external modules.
- Managing dependencies and virtual environments.
- Making HTTP requests and interacting with APIs.
- Parsing JSON data.
- Handling exceptions and network errors.
- Writing readable and maintainable Python code.
- Debugging problems using error messages and diagnostic output.

## 🔮 Future Improvements

- Add more Python library experiments.
- Include automation and productivity scripts.
- Explore data analysis and visualization libraries.
- Build interactive command-line or web applications.
- Add screenshots and execution examples.
- Document dependencies and usage instructions for each program.
- Introduce automated tests where appropriate.

## 🤝 Contributing

Suggestions and improvements are welcome!

1. Fork this repository.
2. Create a new branch.
3. Add your changes or experiments.
4. Commit your changes with a descriptive message.
5. Open a pull request.

## 👩‍💻 Author

**Trisha Basak**

- GitHub: [@trishab2005](https://github.com/trishab2005)
- Repository: [Python_Fun_libraries](https://github.com/trishab2005/Python_Fun_libraries)

---

⭐ If you find this repository useful, consider giving it a star!

*Built with Python, curiosity, and a passion for learning.*
