# JBD Python  :snake:

Aşağıdakı tapşırıqları həll etməyinizi tələb edirik. Əvvəlcə tələbləri oxumağı unutmayın.
#### Tapşırıqları həll etmək üçün bilməli olduğunuz mövzular :brain:

* Itertools
* Collections
* JSON module


**Qeydlər**: :pushpin:
* Tapşırıqları vaxtında həll etməyi və göndərməyi unutmayın :hourglass_flowing_sand:
### Tapşırıqlar :dart:

* `Car` class-ı yaradın. `Car` class-ında yaradılmış obyekti JSON-a çevirin.

        class Car:
            def __init__(self, name, engine, price):
                self.name = name
                self.engine = engine
                self.price = price

        bmw = Car("M5", "3.5L", 32000)

    **Nəticə** :label:

        {
            "name": "M5",
            "engine": "3.5L",
            "price": 32000
        }

* `{ "name": "Elantra", "engine": "2.2L", "price": 12000 }` şəklində verilmiş JSON obyektini `Car` obyektinə çevirin. Nəticə olaraq alınmış obyektin field-lərinə müraciət edə bilməliyik.

    **Nümunə** :bookmark_tabs:
    
        carObj.name, carObj.engine, carObj.price

* Aşağıdakı JSON obyektindən `name` **key**-nə uyğun məlumatları list-ə yığın

        [ 
            { 
                "id":1,
                "name":"Elon",
                "color":[ 
                    "red",
                    "green"
                ]
            },
            { 
                "id":2,
                "name":"Mark",
                "color":[ 
                    "pink",
                    "yellow"
                ]
            }
        ]

    **Nəticə** :label:

        ["Elon", "Mark"]

**Powered by [TechAcademy](https://www.tech.edu.az/)**
