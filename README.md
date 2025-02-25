# End-to-End DevOps Project : TO-Do List Application
## 📊 Description 
This project features a Python Flask application designed for CRUD operations on a MySQL database . It includes all necessary scripts and Kubernetes manifests for deploying the application alongside the MySQL database on an AWS EKS cluster and Amazon RDS, with accompanying ECR repositories . Additionally, the deployment setup incorporates monitoring through Prometheus and Grafana, as well as a fully integrated CI/CD pipeline .
## Prerequisites 
Before you begin, ensure you have met the following requirements :

- **Python** : Programming Language
- **Docker** : Installed and configured
- **kubectl** : Installed and configured to interact with your Kubernetes cluster
- **K9s** : For managing and interacting with Kubernetes clusters more efficiently
- **Terraform** : open-source Infrastructure as Code (IaC) tool
- **Helm** : simplifies the deployment and management of applications on Kubernetes clusters
- **GitHub CLI** : For interacting with GitHub repositories and workflows directly from the command line
- **MySQL** : Open-source relational database management system
- **Beekeeper-Studio** : For Database Access
- **AWS CLI** : For managing AWS services from the command line

## Running Project
### Step 1 : Setting Up the Database
 1. Start MySQL server on your machine
 2. Create a new MySQL database for the Application
 3. Update the database configuration to match your local MySQL settings : 
       - DB_HOST : localhost
       - DB_USER : Your MySQL username 
       - DB_PASSWORD : Your MySQL password
       - DB_DATABASE : Your Databse name 
 4. Create a table in the database that will be used by your application :
       CREATE TABLE tasks (
       id SERIAL PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       is_complete BOOLEAN DEFAULT false
       );

### Step 2 : Running the Application
    1. Clone the Repository :
       # git clone https://github.com/ahmedgamalyousef/ToDo-List-Application.git
    2. Create a Virtual Environment and activate it :
       # python3 -m venv env
       # source env/bin/activate   
    3. Install Dependencies :
       # pip install -r requirements.txt
    4. Start the Application :
       # python3 app.py
    5. Access the Application using the following url : 
       http://localhost:5000

## Running Project with Docker
    1. Build the Docker Image :
       # docker build -t todo-application .
    2. Run the docker container 
       # docker run todo-application
    3. Access the application using following url :
       http://localhost:5000
