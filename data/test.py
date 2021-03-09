from requests import get, post, delete

# Получение всех новостей с базы данных
print(get('http://localhost:5000/api/news').json())


# Получение новости под конкретным id
print(get('http://localhost:5000/api/news/1').json())
# Новости с id = 999 нет в базе
print(get('http://localhost:5000/api/news/999').json())
# Пробуем вместо числа указать букву
print(get('http://localhost:5000/api/news/q').json())

# Проверка пустого запроса передачи только заголовка новости и корректный запрос
print(post('http://localhost:5000/api/news').json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

# Проверка удаления новостей
print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе
print(delete('http://localhost:5000/api/news/1').json())