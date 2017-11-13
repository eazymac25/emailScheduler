
-- psql commands

CREATE DATABASE email_proj;

CREATE USER email_user WITH PASSWORD 'password';


ALTER ROLE email_user SET client_encoding TO 'utf8';
ALTER ROLE email_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE email_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE email_proj TO email_user;