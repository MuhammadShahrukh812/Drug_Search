# Drug_Search
A Project for creating a database different types of drugs with their description. It is based on python API Frame Flask using mySQL database with Docker.
# How to run the project
1. First clone or fetch the repo in your machine (linux/windows).
2. If its windows then you'll have to install docker desktop and also install WSL 2 and enable virtualization from BIOS of your system.
3. If it's linux thn you just need to install docker with their CLI commands on the official website.
4. After this, go into the project folder and type command: docker-compose build
5. After the build is done, which install all requirements, type command: docker-compose up -d
6. Type command docker-compose ps -a to check if the container are running.
7. Sometimes app container exits() because it is waiting for connection from mysql. In this case repeat step 5 and 6 till they are running.
8. This will run the app and mysql container and you are ready to go.
9. Go to any browser and type http://localhost:5000
10. Search your desired drug from the database through API.
