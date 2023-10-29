from django.test import TestCase, Client
from django.urls import reverse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from main.models import TakugoUser
from books.models import Book, BoughtBook

# Create your tests here.
class BookTest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title="Test Book 1",
            book_type="MGA",
            volumes=5,
            image_url="https://cdn.myanimelist.net/r/100x140/images/manga/5/272237.jpg?s=91027a075fc64be41ed3f44b0186cc64",
            score=7.7
        )

        self.book2 = Book.objects.create(
            title="Test Book 2",
            book_type="NVL",
            volumes=9,
            image_url="https://cdn.myanimelist.net/r/100x140/images/manga/5/272237.jpg?s=91027a075fc64be41ed3f44b0186cc64",
            score=8.9
        )

        self.user1 = TakugoUser(username="Test Takugo User 1", user_type="U")
        self.user1.set_password("testpass123")
        self.user1.save()


    def test_book_fields(self):
        book = Book.objects.create(
            title="Test Book 3",
            book_type="MGA",
            volumes=5,
            image_url="https://cdn.myanimelist.net/r/100x140/images/manga/5/272237.jpg?s=91027a075fc64be41ed3f44b0186cc64",
            score=10000.0
        )

        with self.assertRaises(ValidationError) as ve:
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Maximum score of a book is 10")

        with self.assertRaises(ValidationError) as ve:
            book.score = -1
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Score cannot be lower than 0")
        
        with self.assertRaises(ValidationError) as ve:
            book.volumes = -1
            book.score = 10
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Book has to have at least 1 volume")
        
        with self.assertRaises(ValidationError) as ve:
            book.volumes = None
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "This field cannot be null.")

        with self.assertRaises(ValidationError) as ve:
            book.volumes = 5
            book.book_type = "ABC"
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Value 'ABC' is not a valid choice.")
        
        with self.assertRaises(ValidationError) as ve:
            book.book_type = "MGA"
            book.title = "A"*101
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Ensure this value has at most 100 characters (it has 101).")
        
        with self.assertRaises(ValidationError) as ve:
            book.title = "Test Book 3"
            book.image_url = "file:///../../../etc/passwd"
            book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Enter a valid URL.")

        with self.assertRaises(ValidationError) as ve:
            book.image_url = "https://cdn.myanimelist.net/r/100x140/images/manga/5/272237.jpg?s=91027a075fc64be41ed3f44b0186cc64"
            book.score = "hello world"
            book.full_clean()
        
        with self.assertRaises(ValidationError) as ve:
            book.volumes = "5.5"
            book.score = 10
            book.full_clean()

        book.delete()
    

    def test_bought_book_fields(self):
        takugo_user = TakugoUser(
            username="Test Takugo User 2",
            user_type="U"
        )
        takugo_user.set_password("testpass")
        takugo_user.save()

        user = User(username="Test User")
        user.set_password("testpass")

        bought_book = BoughtBook.objects.create(
            user=takugo_user,
            book=self.book1,
            amount=-1
        )

        with self.assertRaises(ValidationError) as ve:
            bought_book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Amount cannot be lower than 1")

        with self.assertRaises(ValidationError) as ve:
            bought_book.amount = 100
            bought_book.full_clean()
        self.assertEqual(ve.exception.messages[0], "Maximum amount of books to buy is 20")

        with self.assertRaises(ValueError) as ve:
            bought_book.amount = 1
            bought_book.user = user
            bought_book.full_clean()
        self.assertEqual(ve.exception.args[0], 'Cannot assign "<User: Test User>": "BoughtBook.user" must be a "TakugoUser" instance.')

        with self.assertRaises(ValueError) as ve:
            bought_book.user = takugo_user
            bought_book.book = "Book"
            bought_book.full_clean()
        self.assertEqual(ve.exception.args[0], 'Cannot assign "\'Book\'": "BoughtBook.book" must be a "Book" instance.')

        with self.assertRaises(ValidationError) as ve:
            bought_book.amount = "10.10"
            bought_book.full_clean()
        
        bought_book.delete()
    

    def test_buy_book(self):
        c = Client()
        buy_url = reverse("books:buy_book", kwargs={"id": 1})
        
        # Can only use POST
        self.assertEqual(c.get(buy_url).status_code, 405)
        self.assertEqual(c.put(buy_url).status_code, 405)
        self.assertEqual(c.patch(buy_url).status_code, 405)
        self.assertEqual(c.head(buy_url).status_code, 405)

        # Unauthorized
        self.assertEqual(c.post(buy_url, {"amount": 1}).status_code, 401)

        c.login(username="Test Takugo User 1", password="testpass123")

        # Successfully bought
        self.assertEqual(c.post(buy_url, {"amount": 1}).status_code, 201)

        # Can't buy the same book again
        self.assertEqual(c.post(buy_url, {"amount": 1}).status_code, 403)

        # Amount must be between 1-20
        buy_url = buy_url[:-1] + "2"
        self.assertEqual(c.post(buy_url, {"amount": -1}).status_code, 400)
        self.assertEqual(c.post(buy_url, {"amount": 100}).status_code, 400)
        self.assertEqual(c.post(buy_url, {"amount": "hello world"}).status_code, 400)
        self.assertEqual(c.post(buy_url).status_code, 400)
        
        # Book does not exist
        buy_url = buy_url[:-1] + "10000"
        self.assertEqual(c.post(buy_url, {"amount": 1}).status_code, 404)
    

    def test_get_bought_book(self):
        c = Client()
        get_bought_book_url = reverse("books:get_book_bought")

        # Can only use GET
        self.assertEqual(c.post(get_bought_book_url).status_code, 405)
        self.assertEqual(c.put(get_bought_book_url).status_code, 405)
        self.assertEqual(c.patch(get_bought_book_url).status_code, 405)
        self.assertEqual(c.head(get_bought_book_url).status_code, 405)

        # Unauthorized
        self.assertEqual(c.get(get_bought_book_url).status_code, 401)

        c.login(username="Test Takugo User 1", password="testpass123")
        c.post(reverse("books:buy_book", kwargs={"id": 1}), {"amount": 1})

        # Bought Book is correct (id = 1)
        bought_books = BoughtBook.objects.filter(user=self.user1)
        books = Book.objects.filter(pk__in=bought_books.values("book"))
        get_result = c.get(get_bought_book_url).content.decode("utf-8")
        own_result = serializers.serialize("json", books)
        self.assertJSONEqual(get_result, own_result)
    

    def test_get_book_list(self):
        c = Client()
        get_book_list_url = reverse("books:get_book_list")
        books = Book.objects.all()

        # Can only use GET
        self.assertEqual(c.get(get_book_list_url).status_code, 200)
        self.assertEqual(c.post(get_book_list_url).status_code, 405)
        self.assertEqual(c.put(get_book_list_url).status_code, 405)
        self.assertEqual(c.patch(get_book_list_url).status_code, 405)
        self.assertEqual(c.head(get_book_list_url).status_code, 405)

        # No filter
        get_result = c.get(get_book_list_url).content.decode("utf-8")
        own_result = serializers.serialize("json", books)
        self.assertJSONEqual(get_result, own_result)

        # MGA filter
        get_result = c.get(get_book_list_url + "?filter=MGA").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="MGA"))
        self.assertJSONEqual(get_result, own_result)
        
        # LNV filter
        get_result = c.get(get_book_list_url + "?filter=LNV").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="LNV"))
        self.assertJSONEqual(get_result, own_result)
        
        # DJS filter
        get_result = c.get(get_book_list_url + "?filter=DJS").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="DJS"))
        self.assertJSONEqual(get_result, own_result)
        
        # MHW filter
        get_result = c.get(get_book_list_url + "?filter=MHW").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="MHW"))
        self.assertJSONEqual(get_result, own_result)
        
        # MHU filter
        get_result = c.get(get_book_list_url + "?filter=MHU").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="MHU"))
        self.assertJSONEqual(get_result, own_result)
        
        # NVL filter
        get_result = c.get(get_book_list_url + "?filter=NVL").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="NVL"))
        self.assertJSONEqual(get_result, own_result)
        
        # OTH filter
        get_result = c.get(get_book_list_url + "?filter=OTH").content.decode("utf-8")
        own_result = serializers.serialize("json", books.filter(book_type="OTH"))
        self.assertJSONEqual(get_result, own_result)
    

    def test_show_main(self):
        c = Client()
        show_main_url = reverse("books:show_main")
        inst = TakugoUser(username="Test Institution", user_type="I")
        inst.set_password("testpass123")
        inst.save()

        # Can only use GET
        self.assertEqual(c.post(show_main_url).status_code, 405)
        self.assertEqual(c.put(show_main_url).status_code, 405)
        self.assertEqual(c.patch(show_main_url).status_code, 405)
        self.assertEqual(c.head(show_main_url).status_code, 405)

        # Used template "books.html" if user_type != "I"
        self.assertTemplateUsed(c.get(show_main_url), "books.html")

        # name = "Guest" if not logged in
        self.assertEqual(c.get(show_main_url).context["name"], "Guest")

        # name = TakugoUser.username if logged in
        c.login(username="Test Takugo User 1", password="testpass123")
        self.assertEqual(c.get(show_main_url).context["name"], self.user1.username)
        c.logout()

        c.login(username="Test Institution", password="testpass123")
        self.assertEqual(c.get(show_main_url).context["name"], inst.username)

        # Used template "unavailable.html" if user_type == "I"
        self.assertTemplateUsed(c.get(show_main_url), "unavailable.html")
