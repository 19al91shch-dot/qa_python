from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest
    @pytest.mark.parametrize(
        'book_name, expected_count',
        [
            ('', False),
            ('A', True),
            ('Любое название', True),
            ('x' * 39, True),
            ('Книга из 40 символов, ровно 40 символов', True),
            ('Книга из 41 символов, ровно 41 символов!', False),
            ('Гордость и предубеждение' * 2, False)
        ],
    )
    def test_add_new_book_validation(self, book_name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == expected_count

    def test_add_duplicate_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')   

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_has_no_genre_by_default(self):
        collector = BooksCollector()
        collector.add_new_book('Герой нашего времени')
                
        assert collector.get_book_genre('Герой нашего времени') == ''  

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_books_without_age_rating_in_children_list(self, genre):
        collector = BooksCollector()
        book_name = f'Детская книга {genre}'
        
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
             
        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_books_with_age_rating_not_in_children_list(self, genre):
        collector = BooksCollector()
        book_name = f'Книга жанра {genre}'
        
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        
        assert book_name not in collector.get_books_for_children()   


    def test_set_book_genre_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        
        assert collector.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'


    def test_set_book_genre_non_existing_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Киберпанк') 
        
        assert collector.get_book_genre('Дюна') == ''


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        
        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 2
        assert 'Книга 1' in books and 'Книга 2' in books  

    def test_get_book_genre_get_genre_for_non_existent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Человек Паук') is None 

    def test_get_books_with_specific_genre_get_books_with_non_existent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []   

    def test_get_books_genre_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_for_children_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Колобок']       

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Танец драконов')
        collector.add_book_in_favorites('Танец драконов')
        
        assert 'Танец драконов' in collector.get_list_of_favorites_books()

    def test_add_non_existing_book_in_favorites_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Танец драконов')
        collector.add_book_in_favorites('Танец драконов')
        collector.delete_book_from_favorites('Танец драконов')
        
        assert 'Танец драконов' not in collector.get_list_of_favorites_books()    

