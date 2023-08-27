# Experiments Insights

Welcome to the world of **Experiment Insights**! 🔍 This Flask application exposes a set of endpoints to simplify your interaction with experiment data:

1) Trigger an ETL Task ✨: Initiate an ETL (Extract, Transform, Load) task to generate valuable insights from user-performed experiments. The results are then uploaded to a PostgreSQL database.

2) Fetch the Insights 📊: Retrieve those hard-earned insights by making use of a dedicated endpoint.

3) Delete the Insights 🗑️: If you ever need to clear the slate, our app provides an endpoint to efficiently delete insights.
## Data Explained  📊


The `/data` folder contains three essential files:

**1. `users.csv`**: This file holds user data, featuring the subsequent columns: `user_id`, `name`, `email`, and `signup_date`.

**2. `user_experiments.csv`**: Within this file, you'll find experiment data. It's structured with these columns: `experiment_id`, `user_id`, `experiment_compound_ids`, and `experiment_run_time`. The `experiment_compound_ids` column conveniently holds a semicolon-separated list of compound IDs.

**3. `compounds.csv`**: This file houses compound data and contains the following columns: `compound_id`, `compound_name`, and `compound_structure`.

## Requirements 🛠️

Make sure you have the following tools and resources ready to work with this project:

- [Python 3.10+](https://www.python.org/downloads/) 🐍
  - The programming language used for development.
  
- [Postman](https://www.postman.com/downloads/) or your preferred API testing platform 🚀
  - Useful for testing and interacting with the endpoints.
  
- [Docker](https://www.docker.com/products/docker-desktop/) 🐳
  - Containerization platform for simplifying deployment and management.
  
- [PostgreSQL](https://www.postgresql.org/download/) 🐘
  - A powerful, open-source relational database management system.

These prerequisites will help you set up and utilize the project efficiently. Keep smiling and enjoy working with these tools! 😊Certainly! Here's the enhanced version of your "API Reference" section:

## API Reference  📚

Explore the available endpoints for interacting with the API:

### Generate Insights

Generate new insights through a POST request.

```http
POST /insights
```

### Get Insights

Retrieve insights using a GET request.

```http
GET /insights
```

### Delete Insights

Remove existing insights via a DELETE request.

```http
DELETE /insights
```
## Deployment 🚀

To deploy this project, follow these steps:

1. Clone this repository to your local machine.

2. Navigate to the directory containing the `docker-compose.yml` file.

3. Run the following command in your terminal:

```bash
docker compose up
```

This command will set up and run Flask and Postgres as two dockerized services. The project will be up and running, and you'll be able to interact with the API using the specified endpoints.

Ensure you have Docker installed and properly configured on your machine before proceeding with the deployment.
## Usage 🧩

Interact with the API using the following `curl` commands:

**GET Request** 🔎:
```bash
curl http://0.0.0.0:5000/insights
```

**POST Request** 📮:
```bash
curl -X POST http://0.0.0.0:5000/insights
```

**DELETE Request** 🗑️:
```bash
curl -X DELETE http://0.0.0.0:5000/insights
```

Use these commands to perform various actions with the API. Replace `http://0.0.0.0:5000` with the appropriate base URL if your API is hosted on a different address.
## Screenshots

![App Screenshot](https://paste.pics/c952bd9b7d6d5f7c654f2416f470b8f7)

