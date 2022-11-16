# Refreshing Your Local ArchivesSpace Database

This tutorial provides an overview of refreshing a local ArchivesSpace database with new data. It also includes information about how to update plugins if necessary.

## Step 1: Export Target Database

First, create an SQL dump of the database that you want to use as the basis of the refresh. This can be done via the `mysqldump` command, or within an SQL client. Users with hosted databases or limited permissions may need to request a database copy of their data from their hosting provider.

## Step 2: Import database

Open a Terminal window and enter `mysql -u root -p`. Follow the prompt to enter your password, after which the MySQL interface will open in the terminal.

Next, enter `show databases;` to see a list of your local database. Pick the one you want to update and enter `use [database name]`

Then, locate your exported database dump, and enter `source /path/to/your/database/dump.sql`. The import should begin. It may take several minutes to complete.

## Step 3: Review Plugin List

If the database is a more recent copy than the current local database (as opposed to a rollback), it might be necessary to install new plugins in order to get the database to properly import into your existing local instance, as the table structures may have changed.

A list of active plugins can be found in the ArchivesSpace `config.rb` file of the ArchivesSpace instance from which you exported your SQL dump.

Install all plugins which modify the ArchivesSpace schema, and add these to your local `config.rb` file

## Step 4: Run Database Setup

If any of your plugins made changes to the database structure, you will eed to run the `setup-database` script in your local ArchivesSpace instance in order to make the changes. You should do this after you import the new database, as it will need to modify the old table structures.

## Step 5: Start Application

All done! Now you can start your local ArchivesSpace instance by entering `archivesspace.sh` into your Terminal. If there are any issues with the installation you will most likely find out during startup. However, it's also possible that ArchivesSpace will start successfully but then run into other issues, so be sure to test your local instance thoroughly!