ANTIZAVOZ - Сервис по сбору и анализу информации о продукции производителей Москвы для развития импортозамещения, направленный на упрощение:
1. Регистрации импортозамещающих компаний и добавления информации о произведенной импортозамещающей продукции.
2. Поиска импортозамещающей продукции для замены иностранной.

pip install -r requirements.txt
sudo apt install redis-server
sudo systemctl start redis
Запуск Celery: celery -A ANTIZAVOZ worker --loglevel=INFO --pool=solo --concurrency=4 -n worker@1