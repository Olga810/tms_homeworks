Установка PostgreSQL:

sudo apt update  
sudo apt install postgresql  
sudo passwd postgres  
ps aux | gres postgres  
sudo -u postgres psql  
whoami

sudo -u postgres createuser --createdb olga  
psql postgres  
\du  
\q

sudo -u postgres createdb --owmer=olga hexlet  
psql -l  
psgl hexlet  
\g  
