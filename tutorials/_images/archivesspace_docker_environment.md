# Archivesspace Environment via Docker
Last updated on 10/04/2024 by Kylene Hutchinson.  

Running your own instance of ArchivesSpace can be very helpful for testing, however ArchivesSpace does not currently support Windows operating systems due to issues building gems with C extensions (such as sassc). 
The following documents how to run your own developer instance of ArchivesSpace on a Windows operating System using a Windows subsystem for Linux to install Ubuntu.

## Installation
1. Download the Docker Desktop program (this will include Compose automatically). https://www.docker.com/
	- install and restart the computer
2. Install WSL https://learn.microsoft.com/en-us/windows/wsl/install
	- Open Powershell as an Administrator
	- `wsl -- install -d Ubuntu`
	- create a username and password
3. Open the ubuntu app to access the ubuntu terminal. Everything from now on will be done in the ubuntu terminal.
4. Install jabba in ubuntu https://github.com/shyiko/jabba
	- `export JABBA_VERSION=0.11.2` (you may need to update the version number if a newer one is available.)
	- `curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash`
	- `. ~/.jabba/jabba.sh`
5. Install java using jabba
	- `jabba install openjdk@1.11.0-2`
	- `jabba use openjdk@1.11.0-2`
6. Do the following installations and updates:
	- `sudo apt update`
	- `sudo apt install build-essential libssl-dev libreadline-dev zlib1g-dev`
	- `sudo apt install ant`
	- `sudo apt install nodejs`
	- `sudo apt install supervisor`

## Building a Yale version of ArchivesSpace
7. Fork ArchivesSpace repository.
	- Fork the https://github.com/archivesspace/archivesspace repo
	- `mkdir archivesspace`
	- `cd archivesspace`
	- `git init`
	- `git remote add origin your-fork-url`
	- `git pull origin main` (main might be master depending on your fork repo settings)
8. Add Yale's plugins and reports
	- Download the repos from:
	- Copy each into Archivesspace/plugins as its own folder (yale-archivesspace-reports, yale-archivesspace-plugins)
	- Edit Archivesspace/common/config/config-defaults.rb so: `AppConfig[:plugins] = ['local', 'lcnaf']` is replaced by: `AppConfig[:plugins] = ['local', 'lcnaf', 'yale-archivesspace-reports', 'yale-archiesspace-plugins']`
9. Gather Yale Production records
  - TBA

## Creating a Docker Build
10. Follow the ArchivesSpace tech-docs https://archivesspace.github.io/tech-docs/development/dev.html
	- `docker-compose -f docker-compose-dev.yml build`
	- `docker-compose -f docker-compose-dev.yml up --detach`
	- `cd ./common/lib`
	- `wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar`
	- `cd -`
	- .`/build/run bootstrap`
	
	OPTIONAL: load dev database
	- `gzip -dc ./build/mysql_db_fixtures/accessibility.sql.gz | mysql --host=127.0.0.1 --port=3306  -u root -p123456 archivesspace`

	- `./build/run db:migrate`
  - `./build/run solr:reset`

## Accessing the Developer Environment
10. Run the Dev Environment
	- `supervisord -c supervisord/archivesspace.conf` (ctrl+c if you need to stop this from running)
	- if that doesn't work, try restarting your computer
	- Otherwise, try running the frontend separately. Open two ubuntu terminals and enter each line in a separate terminal:
		- `supvervisord -c supervisord/api.conf`
		- `./build/run frontend:devserver`
11. In a webbrowser enter: `localhost:3000`
	- if everything went correctly you should see an Archivesspace environment
	- log in with username: admin password: admin
12. Open the ubuntu environment in windows explorer or Visual Studio by entering the following path:
	- `\\wsl.localhost\Ubuntu\home\username` in which username is the username you created for ubuntu
 - Edit or add files to test new reports and plugins

## Troubleshooting
- Rebooting Windows after installation can solve isues with Build Failures
- Make sure Docker is open and the engine is running. Make sure your archivesspace container is running.
- Read the terminal logs to determine if any specific files are causing issues.
- If you are getting port errors but no mentions of bad files, check to make sure only docker is using the port
  - `docker ps` in ubuntu can be used to see what containers are in operation and what ports they are using
  - `sudo lsof -i -P -n` in ubuntu can be used to see what processes are using which ports. 127.0.0.1:53 would be port 53, and the PID can be used to identify the process in Task Manager. If a port appears without a (LISTEN) condition, then it is likely in use by the process.
- Make sure everything is up to date and the correct version.
  - `ant -v`
  - `nodejs -v`
  - `jabba use openjdk@1.11.0-2`
- Try each part of the environment individually to better see errors
  - `./build/run backend:devserver`
  - `./build/run public:devserver`
  - `./build/run indexer`
  - `./build/run frontend:devserver`
- Rerun bootstap `./build/run bootstrap`
- Reset solr `./build/run solr:reset`
