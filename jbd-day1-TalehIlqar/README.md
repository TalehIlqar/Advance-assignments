# JBD Python  :snake:

Aşağıdakı tapşırıqları həll etməyinizi tələb edirik. Əvvəlcə tələbləri oxumağı unutmayın.
#### Tapşırıqları həll etmək üçün bilməli olduğunuz mövzular :brain:

* Enkapsulasiya
* Varislik
* Polimorfizm
* Abstraksiya
* Setter, Getter methods


**Qeydlər**: :pushpin:
* Tapşırıqları vaxtında həll etməyi və göndərməyi unutmayın :hourglass_flowing_sand:
### Tapşırıqlar :dart:

`Vehicle` adlı class yaradın. Yaradılmış class-ın aşağıdakı field-ləri olmalıdır:
        
        numofWheels;
        color;
        engine;
        positionX;
        positionY;
        speed; 
        isOn = false;

Verilmiş class-ın aşağıda qeyd olunmuş methodları yaradılmalıdır

* `accelerate()` - bu method çağırılarkən maşının sürətini 1 vahid artırmalıdır

* `moveForward(int x, int y)` - bu method çağırılarkən maşının `postionX` və `postionY` dəyərlərini müsbətə doğru dəyişin

* `moveBackwards(int x, int y)` - bu method çağırılarkən maşının `postionX` və `postionY` dəyərlərini mənfiyə doğru dəyişin

* `ignition()` - bu method `isOn` true-dursa false, false-dursa true halına gətirməlidir

* `numOfWheels()` - bu method təkərlərin sayını qaytarmalıdır

* `numOfWheels(int num)` bu method təkərlərin sayını dəyişməlidir

* `color()` - bu method maşının rəngini qaytarmalıdır

* `color(color)` - bu method maşının rəngini dəyişməlidir

`numOfWheels`, `color` methodları **getter** və **setter** kimi təyin olunmalıdır


`Vehicle` class-ından **inherit** olan `Motocycle` class-nı yaradın.

`Motocycle` class-ının aşağıdakı field və mehtod-ları yaradılmalıdır

* `brand`; //instance variable
* `numofSeats`; //instance variables
* `__init__` initialize `Motocycle`(color, engine, int wheels, brand, seats)
* `getBrand()` - bu method brand return etməlidir
* `getnumofSeats()`- bu method `numofSeats` return etməlidir
* `setBrand(brand)` - bu method `brand`-i set etmelidir
* `setnumofSeats(numofSeats)` bu method `numofSeats`-i set etməlidir
* `accelerate()` - bu method sürəti 10 vahid artırmalıdır (Polimorfizmdən istifadə olunmalıdır)
* `decelerate()` - bu method sürəti 10 vahid azaltmalıdır


**Powered by [TechAcademy](https://www.tech.edu.az/)**
