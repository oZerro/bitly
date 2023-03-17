# Модуль bitly.py
Модуль сокращает ссылки и показывает количество переходов по ним.  
- Если введете ссылку, которую хотите сократить - вернет вам сокращенную ссылку.
- Если укажите готовую ссылку bitly - получите количетво переходов по ней.
- Если при вводе будет ошибка - получите сообщение об этом.

## Установка
Python 3 уже должен быть установлен
1. Вам нужно зарегистрироваться на [сайте](https://bitly.com/) и авторизоваться.

2. Создать ваш личный токен [тык сюда](https://app.bitly.com/settings/api/) и сохраните его.  
Выглядит он так: 4420a9fef71911865d8004568eb642714645f82e  
![](https://github.com/oZerro/bitly/blob/main/img/qwe.jpg?raw=true)

3. Клонируйте репозиторий с github - для этого выполните в консоли:  
`git clone https://github.com/oZerro/bitly.git`

4. Создайте виртуальное окружение.  
Для создания виртуального окружения:  
- Перейдите в директорию своего проекта.  
`cd bitly` 
- Выполните:  
`python -m venv venv`

5. Активируйте виртуальное окружение.  
Для активации виртуального окружения выполните:  
- `venv\Scripts\activate.bat` - для Windows;
- `source venv/bin/activate` - для Linux и MacOS.

6. Установите зависимости:  
 `pip install -r requirements.txt`  

7. Создайте файл **.env** в вашей деректории проекта.  

- `type nul > .env` - для Windows;
- `touch файл.txt` - для Linux и MacOS.

8. Откройте файл **.env** в любом текстовом редакторе и добавьте ваш токен - сохраните.  
Строка будет выглядеть так:  
`BITLY_TOKEN='тут ваш токен'`

## Как запустить
Для запуска перейдите в директорию проекта и выполните команду в консоли:    
`python bitly.py`  

Если все сделали правильно - увидите такое сообщение.
Вводите полную ссылку, с протоколом `http://` или `https://`, иначе программа будет возвращать ошибку!
![](https://github.com/oZerro/bitly/blob/main/img/23.jpg?raw=true)




