 This is a Docker Compose setup for an OwnCloud instance with OpenLDAP, PHP LDAP Admin, MariaDB, Redis, and Nginx. The environment variables are defined in separate .env files, and the setup includes an init.sh script to populate the OpenLDAP directory using LDIF files.

The docker-compose.yml file defines five services: openldap, phpldapadmin, mariadb, redis, and owncloud. Each service has its own network and volume definitions.

The env/mariadb/mariadb.env file contains the MariaDB environment variables, such as the root password and OwnCloud database credentials.

The env/openldap/openldap.env file contains the OpenLDAP environment variables, including the administrator username and password.

The env/owncloud/owncloud.env file contains the OwnCloud environment variables, such as the Redis host, domain, and database credentials.

The env/phpldapadmin/phpldapadmin.env file contains the PHP LDAP Admin environment variables, including the LDAP hosts and HTTPS settings.

The init.sh script copies LDIF files to the OpenLDAP container and executes ldapadd commands to populate the OpenLDAP directory with the desired entries. The script also waits until all services are up and running before executing the LDIF scripts.