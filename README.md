# Weather App

A simple Flask-based weather application that fetches weather data for a given city using the [wttr.in](https://wttr.in/) API and location details from OpenStreetMap's Nominatim API. The app displays temperature, weather description, humidity, wind speed, and the city’s state and country.

---

## Features

- Search weather by city name
- Displays city, state, and country information
- Responsive UI with Bootstrap 5
- Runs locally using Flask or inside Docker container
- Docker Compose support for easy setup

---

## Demo

![Weather App Screenshot](./screenshot.png)

---

## Getting Started

### Prerequisites

- Python 3.7+
- Docker & Docker Compose (optional, for containerization)
- Git

### Local Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   docker-compose up --build