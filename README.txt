1. "/api/v1/books/", metoda GET - zaczytuje plik json z książkami
                     metoda POST - dodaje nową książkę
2. "/api/v1/books/<int:book_id>", metoda GET - zwraca książkę o wybranym book_id
                                  metoda DELETE - kasuje wybraną książkę
                                  metdoa PUT - zapisuje nową książkę w bazie