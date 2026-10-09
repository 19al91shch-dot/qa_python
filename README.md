# qa_python
test_add_new_book_add_two_books
# Проверяет, что новые книги успешно добавляются в коллекцию.

test_add_new_book_validation
# Проверяет валидацию названия книги (пустое, слишком длинное, корректное, граничные значения).

test_add_duplicate_book_not_added
# Проверяет, что нельзя добавить две одинаковые книги

test_add_new_book_has_no_genre_by_default
# Проверяет успешное добавление книги без жанра

test_books_without_age_rating_in_children_list
# Проверка оприсутствия Книг без возрастного рейтинга в списке книг для детей

test_books_with_age_rating_not_in_children_list
# Проверка отсутствия Книг с возрастным рейтингом в списке книг для детей

test_set_book_genre_existing_genre
# Проверка успешной установки жанра для существующей книги.

test_set_book_genre_non_existing_genre_not_set
# Проверяет, что некорректный жанр не устанавливается книге.

test_get_books_with_specific_genre
# Проверяет получение списка книг по указанному жанру.

test_get_book_genre_get_genre_for_non_existent_book
# Проверяет установку жанра для несуществующей книги.

test_get_books_with_specific_genre_get_books_with_non_existent_genre
# Проверяет поведение при запросе несуществующего жанра.

test_get_books_genre_get_books_genre
# Проверяет получение полного словаря книг и жанров.

test_get_books_for_children_get_books_for_children
# Проверяет получение списка книг, подходящих детям.

test_add_book_in_favorites
# Проверяет добавление книги в избранное.

test_add_non_existing_book_in_favorites_not_added
# Проверяет, что несуществующая книга не добавляется в избранное.

test_delete_book_from_favorites
# Проверяет удаление книги из избранного.

