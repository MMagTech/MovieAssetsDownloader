import os
import requests
import re

def read_movies_from_directories(base_path):
    movies = []
    for entry in os.scandir(base_path):
        if entry.is_dir():
            # Extract movie name and release year from the directory name
            match = re.match(r'^(.*) \((\d{4})\)$', entry.name)
            if match:
                movie_name = match.group(1)
                release_year = match.group(2)
                movies.append((movie_name, release_year, entry.path))
    return movies

def fetch_movie_data(movie_name, release_year, api_key):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': movie_name,
        'year': release_year
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Just get the first result for simplicity
            first_result = data['results'][0]
            return {
                'title': first_result.get('title'),
                'release_date': first_result.get('release_date'),
                'poster_path': "https://image.tmdb.org/t/p/original" + first_result.get('poster_path') if first_result.get('poster_path') else None,
                'background_path': "https://image.tmdb.org/t/p/original" + first_result.get('backdrop_path') if first_result.get('backdrop_path') else None
            }
    return None

def download_image(url, save_path):
    try:
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {save_path}.")
                return True
            else:
                print(f"Failed to download {save_path}. HTTP Status Code: {response.status_code}")
        else:
            print(f"No URL for {save_path}.")
    except Exception as e:
        print(f"Exception occurred while downloading {save_path}: {e}")
    return False

def main():
    api_key = "YOUR_API_KEY_GOES_HERE"
    base_movie_path = r'base_movie_path'  # Base path to your movie directories
    failed_movies_file = r'base_movie_path\failed_movies.txt'  # Path to save the failed movies list. 

    # Check if the base path exists and is accessible
    if not os.path.exists(base_movie_path):
        print(f"Base path {base_movie_path} does not exist or is not accessible.")
        return

    movies_list = read_movies_from_directories(base_movie_path)
    failed_movies = []
    for movie_name, release_year, movie_path in movies_list:
        movie_data = fetch_movie_data(movie_name, release_year, api_key)
        if movie_data:
            print(f"Movie: {movie_data['title']}, Release Date: {movie_data['release_date']}, Poster URL: {movie_data['poster_path']}, Background URL: {movie_data['background_path']}")
            # Ensure the movie folder exists
            if not os.path.exists(movie_path):
                print(f"Movie path {movie_path} does not exist or is not accessible.")
                failed_movies.append(f"{movie_name} ({release_year})")
                continue
            # Download the poster as poster.jpg inside the movie folder
            poster_path = os.path.join(movie_path, 'poster.jpg')
            if not download_image(movie_data['poster_path'], poster_path):
                failed_movies.append(f"{movie_name} ({release_year}) - Poster")
            # Download the background as background.jpg inside the movie folder
            background_path = os.path.join(movie_path, 'background.jpg')
            if not download_image(movie_data['background_path'], background_path):
                failed_movies.append(f"{movie_name} ({release_year}) - Background")
        else:
            print(f"Movie: {movie_name} - Data not found.")
            failed_movies.append(f"{movie_name} ({release_year})")

    if failed_movies:
        print("\nMovies that failed to download images:")
        for movie in failed_movies:
            print(movie)
        # Save the failed movies list to a file
        with open(failed_movies_file, 'w') as file:
            for movie in failed_movies:
                file.write(f"{movie}\n")
        print(f"\nFailed movies list saved to {failed_movies_file}")

if __name__ == "__main__":
    main()
