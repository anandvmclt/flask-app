
## Steps to create a new flask project with CI/CD Pipelines

# 1 - Create a new Flask application

# 2 - Add it to a new GitHUb Repository
 - git@github.com:anandvmclt/flask-app.git
 - List all  -> docker images
 - Run it  - > docker run -d -p 5000:5000 python-app:latest
 - List Running Container -> docker ps
 - Docker stop -> docker stop 8d7660436de9 (Image ID)
 - Remove a Container -> docker rm  8d7660436de9 (Image ID)




# 3 - Add a docker file and add it to docker repository.
*  Replace "python-app" with your desired image name
- docker build -t python-app .  