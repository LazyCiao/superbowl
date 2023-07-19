SuperBowl Web App
SuperBowl Logo

Welcome to SuperBowl, a Django web app that allows users to view and bet on American football games! SuperBowl provides real-time information on past, current, and upcoming games, allowing users to place bets and view their betting history. This README will guide you through the installation process and explain the features and functionalities of the application.

Table of Contents
Getting Started

Prerequisites
Installation
Running the App
Usage

Home
Roster
Bets
User Registration and Activation
Bureau Access
API Endpoints
Database Models

Team
Player
Game
Bet
Contributing

License

Getting Started
Prerequisites
Before running SuperBowl, make sure you have the following installed on your system:

Python (>=3.7)
Django (>=3.1)
pip (Python package manager)
Installation
Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/your-username/superbowl.git
cd superbowl
Install the required Python packages using:

Copy code
pip install -r requirements.txt
Running the App
Start the Django development server using the following command:

Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to access the SuperBowl app.

Usage
Home
The home page displays three sections of American football games:

Past Games: Shows a list of recently completed games.
Current Games: Displays games that are currently in progress.
Upcoming Games: Lists games that are yet to start.
Roster
The roster page allows users to view team rosters for specific games. Select a home team and an away team from the dropdown lists to see their respective rosters.

Bets
To access the bets page, users must first register and log in. Once logged in, users can view and place bets on upcoming games. Users can also edit or cancel their existing bets. The bets page shows three sections:

Past Games: Displays past games for which users have already placed bets.
Current Games: Shows current games for which users can still place bets.
Upcoming Games: Lists upcoming games available for betting.
User Registration and Activation
To register as a user, click on the "Register" link at the top-right corner of the page. Fill in the required information, and an activation email will be sent to your registered email address. Click the activation link to activate your account and start placing bets.

Bureau Access
SuperBowl has a special feature for staff members and superusers. The "Bureau" section is accessible only to users with staff or superuser privileges. Bureau access allows staff members to manage games and terminate matches. Only staff members can view the "Match" and "Detail" pages.

API Endpoints
SuperBowl provides API endpoints to access information about teams, players, games, and bets. These endpoints allow external applications to access the data provided by the SuperBowl app.

/api/teams/: Provides a list of all teams and their details.
/api/players/: Provides a list of all players and their details.
/api/games/: Provides a list of all games and their details.
/api/bets/: Provides a list of all bets and their details.
Database Models
Team
The Team model represents an American football team. It has the following fields:

name: The name of the team.
image: An optional field for the team's image/logo.
Player
The Player model represents a football player. It has the following fields:

first_name: The player's first name.
last_name: The player's last name.
team: A foreign key to the associated team.
age: The player's age.
player_number: The player's jersey number.
state: The state associated with the player.
Game
The Game model represents an American football game. It has the following fields:

home_team: A foreign key to the home team.
away_team: A foreign key to the away team.
score: The final score of the game (when available).
commentary: Commentary about the game (when available).
weather: The weather conditions during the game (when available).
home_team_odds: The odds for the home team to win.
away_team_odds: The odds for the away team to win.
duration: The duration of the game.
datetime: The date and time of the game's start.
datetime_end: The date and time of the game's end.
Bet
The Bet model represents a user's bet on a football game. It has the following fields:

user: A foreign key to the user who placed the bet.
game: A foreign key to the game on which the user placed the bet.
team: A foreign key to the team the user bet on (optional for future use).
bet_amount: The amount the user bet on the game.
result: The result of the bet (True for win, False for loss, None for pending).
Contributing
We welcome contributions to the SuperBowl project! To contribute, follow these steps:

Fork the repository and create a new branch for your feature or bug fix.
Make your changes and test them thoroughly.
Submit a pull request with a detailed description of your changes.
License
SuperBowl is open-source software licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.
