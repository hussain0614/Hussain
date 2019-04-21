#!/usr/bin/python
 
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump and tar utility.
#
# Written by : Hussain Sodawala
# Created date: April 21, 2019
# Last modified: 
# Tested with : Python 2.7.15 & Python 3.5
# Script Revision: 1.0
#
##########################################################
 
# Import required python libraries
import os
import time
import datetime
import pipes

# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databases names one on each line and assigned to DB_NAME variable.

DB_HOST = 'localhost' 
DB_USER = 'root'
DB_USER_PASSWORD = '_mysql_user_password_'
DB_NAME = '/backup/dbnameslist.txt'
