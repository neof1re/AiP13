class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0.0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")
    def update_rating(self, new_rating):
        self.rating = new_rating
restaurant1 = Restaurant("Сакура", "Японская")
restaurant2 = Restaurant("Тако Белл", "Мексиканская")
restaurant3 = Restaurant("Грузинский Очаг", "Грузинская")
restaurant1.update_rating(4.8)
restaurant2.update_rating(4.2)
restaurant3.update_rating(4.9)
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()