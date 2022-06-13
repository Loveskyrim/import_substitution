# ANTIZAVOZ
Сервис по сбору и анализу информации о продукции производителей Москвы для развития импортозамещения, направленный на упрощение:
1. Регистрации компаний и добавления информации о произведенной продукции.
2. Поиска импортозамещающей продукции.

## Стек технологий
Python
- Django
- Celery

jQuery 

## Состав программы: 
### APPS
- ANTIZAVOZ - общие файлы настроек сервера.
- authorization - приложение авторизации пользователей/компаний.
- mainPage - приложение стартовой страницы с блогом и поисковой строкой.
- moderatorPage - раздел профиля модератора данных.
- organizations - приложение для отображения всех основных ифноврамионных страниц (информация о компании, о продукте, страницы профиля пользователей, отдельные страницы с таблицами по компаниям/продуктам).
- moderatorPage - раздел профиля компании/компании.


### Функционал
1. [x] Компонент автоматического обхода сайтов компаний-производителей и сбора
информации об их продукции: moderatorPage
2. [x] Компонент хранения данных, который отвечает за правильное хранение/кластеризацию информации о продукции в реестре: ANTIZAVOZ, moderatorPage
3. [x] Компонент рабочее место - графический интерфейс пользователя для просмотра настроек и информации о работе парсера, просмотра реестра продукции с
возможностью гибкой фильтрации: mainPage, organisations

