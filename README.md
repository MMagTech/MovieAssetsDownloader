
# Movie Assets Downloader

Movie Assets Downloader is a Python script designed to automate the downloading of movie posters and backgrounds (backdrops) from the TMDB (The Movie Database) API. The script scans a specified directory for movie folders named in the format `MovieName (Year)`, fetches the corresponding movie data from the TMDB API, and saves the movie poster and background images directly into the respective movie folders.

## Features

- **Automated Scanning:** Automatically scans a base directory for movie folders and extracts movie names and release years.
- **TMDB Integration:** Fetches movie data, including poster and background URLs, from the TMDB API.
- **Concurrent Downloads:** Efficiently downloads multiple images using concurrent requests.
- **Error Logging:** Logs movies that failed to download their assets into a file for easy troubleshooting.
- **Customizable Paths:** Allows users to specify the base directory for movies and the output file for logging failed downloads.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/MovieAssetsDownloader.git
```

2. Navigate to the project directory:

```bash
cd MovieAssetsDownloader
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Update the `YOUR_API_KEY_GOES_HERE` placeholder with your TMDB API key in the script.
2. Set the `base_movie_path` to your movie directory path.
3. Run the script:

```bash
python MovieAssetsDownloader.py
```

## Example

```bash
python MovieAssetsDownloader.py
```

## Configuration

- **TMDB API Key:** Update the `YOUR_API_KEY_GOES_HERE` placeholder in the script with your TMDB API key.
- **Base Movie Path:** Set the `base_movie_path` variable to the directory containing your movie folders.
- **Failed Movies File:** The script saves a list of movies that failed to download their assets to `failed_movies.txt` in the same directory as the movie folders.

## Future Enhancements

- Support for downloading additional movie assets.
- Improved error handling and logging.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
