CREATE TABLE aliases (
pkid smallint(3) NOT NULL auto_increment,
mail varchar(120) NOT NULL default '',
destination varchar(120) NOT NULL default '',
enabled tinyint(1) NOT NULL default '1',
PRIMARY KEY  (pkid),
UNIQUE KEY mail (mail)
) ;
CREATE TABLE domains (
pkid smallint(6) NOT NULL auto_increment,
domain varchar(120) NOT NULL default '',
transport varchar(120) NOT NULL default 'virtual:',
enabled tinyint(1) NOT NULL default '1',
PRIMARY KEY  (pkid)
) ;
CREATE TABLE users (
id varchar(128) NOT NULL default '',
name varchar(128) NOT NULL default '',
uid smallint(5) unsigned NOT NULL default '5000',
gid smallint(5) unsigned NOT NULL default '5000',
home varchar(255) NOT NULL default '/mnt/spool/mail/virtual',
maildir varchar(255) NOT NULL default 'blah/',
enabled tinyint(1) NOT NULL default '1',
change_password tinyint(1) NOT NULL default '1',
clear varchar(128) NOT NULL default 'tinaturner',
crypt varchar(128) NOT NULL default 'B436E663C5B7E',
quota varchar(255) NOT NULL default '',
PRIMARY KEY  (id),
UNIQUE KEY id (id)
) ;

INSERT INTO domains (domain) VALUES
	('localhost'),
	('localhost.localdomain'),
	('uturnmail.com');

	INSERT INTO aliases (mail,destination) VALUES
	('postmaster@localhost','root@localhost'),
	('sysadmin@localhost','root@localhost'),
	('webmaster@localhost','root@localhost'),
	('abuse@localhost','root@localhost'),
	('root@localhost','root@localhost'),
	('@localhost','root@localhost'),
	('@localhost.localdomain','@localhost');

		INSERT INTO users (id,name,maildir,crypt) VALUES
	('root@localhost','root','root/',encrypt('@life1991', CONCAT('$5$', MD5(RAND()))) );

			INSERT INTO users (id,name,maildir,crypt) VALUES
	('sept@uturnmail.com','root','root/',encrypt('@life1991', CONCAT('$5$', MD5(RAND()))) );
