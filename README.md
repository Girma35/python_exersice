# Ethiopian Map Navigation using Turtle Graphics

This Python script allows you to navigate an interactive map of Ethiopia using the Turtle graphics library. The script loads city coordinates from a CSV file, displays the map using an image file, and prompts users to guess and locate cities by their names.

## Preview

![Ethiopian Map](ethiopian_map.gif)

*Image Source:![Geographic-map-of-Ethiopia-that-shows-regions-and-chartered-cities](https://github.com/Girma35/python_exersice/assets/143084812/3bb5cd51-34e1-42ee-b4ba-950bfdbb1acd)


## Features

- Loads city coordinates from a CSV file (`coordinates.csv`).
- Displays an interactive map using Turtle graphics with the Ethiopian map image.
- Prompts users to input city names and locates them on the map.
- Tracks and displays the score based on correct guesses out of 16 possible cities.
- Saves missed city names to `missed_city.csv` upon exiting the game.

## Requirements

- Python 3.x
- Turtle graphics library
- Pandas library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Girma35/python_exersice.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python_exersice
   ```

3. Install the required Python libraries (if not already installed):

   ```bash
   pip install pandas
   ```

## Usage

1. Download the Ethiopian map image (`image.gif`) from [Ethiopian Mapping Agency](https://www.ema.gov.et/) or use your preferred map image.

2. Place the map image (`image.gif`) and city coordinates CSV file (`coordinates.csv`) in the project directory.

3. Run the script:

   ```bash
   python main.py
   ```

4. The Ethiopian map window will open, displaying the map image (`image.gif`).

5. Input city names as prompted in the Turtle graphics window. The script will locate and mark the city on the map if correct.

6. The game ends after 16 guesses or when the user types "EXIT". The script will save missed city names to `missed_city.csv`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
