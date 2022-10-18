from main import Shop, Store, Request

print("Привет!")

storage_1 =Store(items={"Телефон":10, "Компютер":10, "Приставка": 10})
storage_2 =Store(items={"Телефон":10, "Компютер":10, "Приставка": 10})
shop_1 =Shop(items={"Телефон":3, "Компютер":3, "Приставка": 3})

test_text = "Привезти 3 Телефон ан shop_1"
req = Request(test_text)
req.move()

#Видео 54:55