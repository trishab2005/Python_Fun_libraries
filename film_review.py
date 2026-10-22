
import requests

def get_movie_review():
    movie_name = input("Enter the name of the movie: ").strip()

    api_key = "efcf96b6"
    url = "https://www.omdbapi.com/"

    params = {
        "t": movie_name,
        "apikey": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=(5, 30))
        response.raise_for_status()

        details = response.json()

        if details.get("Response") == "True":
            print("\n--- Movie Details ---")
            print(f"Title: {details.get('Title')}")
            print(f"Year: {details.get('Year')}")
            print(f"Rated: {details.get('Rated')}")
            print(f"Genre: {details.get('Genre')}")
            print(f"Director: {details.get('Director')}")
            print(f"IMDb Rating: {details.get('imdbRating', 'N/A')}")
            print(f"Plot: {details.get('Plot')}")

        else:
            print("Movie not found:", details.get("Error"))

    except requests.exceptions.RequestException as error:
        print("Network/API error:", error)

    except ValueError:
        print("The server returned invalid JSON. Please try again.")

get_movie_review()



