from main import Shop, Store, Request

print("Привет!")

storage_1 =Store()
storage_2 =Store()
shop_1 =Shop(items={"Телефон":3, "Компютер":3, "Приставка": 3})

test_text = "Привезти 3 Телефон ан shop_1"
req = Request(test_text)
req.move()

#Видео 54:55