# JBD Python  :snake:

Aşağıdakı tapşırıqları həll etməyinizi tələb edirik. Əvvəlcə tələbləri oxumağı unutmayın.
#### Tapşırıqları həll etmək üçün bilməli olduğunuz mövzular :brain:

* Python testing (PyTest)

**Qeydlər**: :pushpin:
* Tapşırıqları vaxtında həll etməyi və göndərməyi unutmayın :hourglass_flowing_sand:
### Tapşırıqlar :dart:

* Arqument kimi qəbul etdiyi sətri ilk hərfini böyük hərifə çevirən (capitalize) funksiya yaradın. 

    **Nümunə** :bookmark_tabs:
    
        >>> func('tech') 
        >>> 'Tech'

    Yaradılmış funksiya aşağıdakı `test case`-ləri ödəyən testlərdən keçməlidir.

    - `Giriş verilənləri ==> "proqramlaşdırma". Gözlənilən nəticə ==> "Proqramlaşdırma"`

    - `Giriş verilənləri ==> 33. Gözlənilən nəticə ==> TypeError`

* `Wallet()` class-ı yaradın. Bu class-ın `balance` field-i olmalıdır. `balance`-ın ilkin dəyəri 0 olmalıdır. `spend_cash(amount)` methodu yaradın, bu method arqument kimi qəbul etdiyi dəyər qədər `balance` azaltmalıdır. `add_cash(amount)` methodu yaradın, bu method arqument kimi qəbul etdiyi dəyər qədər `balance` artırmalıdır. 

    Yaradılmış funksiya aşağıdakı `test case`-ləri ödəyən testlərdən keçməlidir.

    - `Wallet()` class-ından obyekt yaradın. `balance`-ın 0-a bərabər olduğunu yoxlayan test yazın.
    - `Wallet()` class-ından obyekt yaradın. İlkin olaraq `balance` 120 olmalıdır. `spend_cash(30)` methodu çağırıldıqda `balance`-ın 90 olduğunu yoxlayan test yazın.
    - `Wallet()` class-ından obyekt yaradın. İlkin olaraq `balance` 10 olmalıdır. `add_cash(70)` methodu çağırıldıqda `balance`-ın 80 olduğunu yoxlayan test yazın.
    - `Wallet()` class-ından obyekt yaradın. İlkin olaraq `balance` 60 olmalıdır. `spend_cash(90)` methodu çağırıldıqda `InsufficientAmount` type-da error raise etməlidir. Bunu yoxlayan test yazın. 
        - ***Hint*** :lollipop: [Creating Custom Exceptions](https://www.programiz.com/python-programming/user-defined-exception) mövzusu istifadə olunacaq. 

**Powered by [TechAcademy](https://www.tech.edu.az/)**
