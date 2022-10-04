# payment
1) Создать виртуальную машину

2) Скопировать код на неё

3) Прописать команды 
sudo apt update
sudo apt upgrade

4) Установить python pip
sudo apt install python3-pip

5) Установка библиотек
sudo pip install django
sudo pip install stripe

6) Перейти в директорию к файлу manage.py
7) выполнить команду 
sudo python3 manage.py runsever 0:80
8) Перейти на сайт по адресу виртуальной машины

___

## Использование собственного магазина

1) При желании можно изменить stripe.api_key на свой ключ, который можно получить на сайте stripe. Ключ stripe.api_key на данный момент хранится в файле /payment/payapp/views.py

2) В этом же файле в функции index используется id товара. Этот id используется для теста, при желании, его можно заменить на id товара из своего

___

*) В общем случае файлы .env не стоит хранить на github,  Для сторонних пользователей можно сделать файл .env.dist вместо файла .env, в котором не хранить ключи. В таком случае при запуске проекта, пользователь должен будет заполнить поля из этого файла своими значениями и переименовать его из .env.dist -> .env
Файлы с расширением .env обычно добавляются в gitignore, такие файлы система контроля версий не сохраняет.
