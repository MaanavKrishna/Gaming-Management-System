# 🎮 Gaming Management System (GMS)
Gaming Management System (GMS) is an efficient solution for organizing and managing game inventories and subscriber information. Designed to simplify administrative tasks, GMS offers tools to manage game details, subscriber records, and generate detailed reports in an organized manner.

🕹️ Key Features

Game Management
	•	Add Games: Easily register new games with essential details like game number, name, description, and platform/application.
	•	Modify Games: Update game information to keep your records accurate and up to date.
	•	Delete Games: Remove outdated or irrelevant games from the database.
	•	Search Games: Quickly find games using their number or name for easy access to details.

Subscriber Management
	•	Add Subscribers: Register new subscribers with attributes such as name, email, subscription status, and newsletter preferences.
	•	Modify Subscribers: Edit existing subscriber records to reflect updated information.
	•	Delete Subscribers: Clean up the database by removing inactive or duplicate subscribers.
	•	Search Subscribers: Retrieve subscriber records using unique identifiers or names.

Reporting
	•	Active Subscriber Report: Generate a list of all active subscribers to monitor engagement.
	•	Closed Subscriber Report: Identify subscribers who are no longer active.
	•	Newsletter Sent/Returned Report: Analyze newsletter delivery status and engagement rates.

💻 Technologies Used
	•	Python: The core programming language used for development.
	•	MySQL: A robust database system for efficient data storage and management.
	•	Tabulate: A library used for presenting data in clean and visually appealing table formats.

📦 Installation Guide

Step 1: Clone the Repository

git clone https://github.com/MaanavKrishna/gaming-management-system.git
cd gaming-management-system

Step 2: Install Dependencies

Install the required Python libraries:

pip install mysql-connector-python tabulate

Step 3: Set Up the Database
	1.	Open your MySQL client and create a new database:

CREATE DATABASE GMS;


	2.	Tables (game and subscriber) are automatically created when the program is run for the first time.

Step 4: Run the Application

Run the script to start the system:

python gms.py

🚀 Usage
	1.	Start the program and navigate the intuitive menu options:
	•	Game Menu: Manage all game-related tasks like adding, modifying, deleting, or searching for games.
	•	Subscriber Menu: Perform subscriber-related operations, including registration, updates, and record removal.
	•	Generate Reports: Access insightful reports to analyze subscriber activities and status.
	2.	Follow prompts to input data or view results.

📝 Highlights
	•	Simplified data entry and management for games and subscribers.
	•	Automatic creation of necessary tables for a seamless setup experience.
	•	Organized and detailed reports for better decision-making.
	•	Error-handling for invalid inputs to maintain data integrity.

📊 Example Report

Active Subscribers Report

Subscriber Number	Subscriber Name	Subscriber Email	Subscriber Status	Newsletter Status
101	John Doe	john.doe@example.com	Active	Sent
102	Jane Smith	jane.smith@example.com	Active	Sent

🤝 Contributions

We welcome contributions to make GMS even better! Feel free to:
	•	Fork the repository.
	•	Submit pull requests.
	•	Report issues or suggest enhancements.

🌟 Closing Notes

The Gaming Management System is your ultimate assistant for organizing and managing gaming and subscriber data. Whether you’re tracking game inventories or monitoring subscriber engagement, GMS offers a reliable and efficient solution. Dive into the world of simplified management—because managing your games and subscribers should be as fun as playing them! 🎮
