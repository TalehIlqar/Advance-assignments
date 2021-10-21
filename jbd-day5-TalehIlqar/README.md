# JBD Python  :snake:

Aşağıdakı tapşırıqları həll etməyinizi tələb edirik. Əvvəlcə tələbləri oxumağı unutmayın.
#### Tapşırıqları həll etmək üçün bilməli olduğunuz mövzular :brain:

* Unit testing

**Qeydlər**: :pushpin:
* Tapşırıqları vaxtında həll etməyi və göndərməyi unutmayın :hourglass_flowing_sand:
### Tapşırıqlar :dart:

* Daxil edilmiş edədi kuba yüksəldən funksiya yazın. Yaradılmış funksiya aşağıdakı `test case`-ləri ödəyən testlərdən keçməlidir.

    - `Giriş verilənləri ==> 7. Gözlənilən nəticə ==> 343`

    - `Giriş verilənləri ==> 'Tech academy'. Gözlənilən nəticə ==> raise TypeError`

* Arqument kimi sətirlərdən (hər hansı söz) ibarət olan list qəbul edən funksiya yazın. Bu funksiya daxil edilmiş listin içərisində 'a' hərfi olan sətirləri (sözləri) yeni list-də qaytarmalıdır.

    **Nümunə** :bookmark_tabs:
    
        >>> func(['alma', 'su', 'dağ', 'meşə', 'stul', 'proqram'])
        >>> ['alma', 'dağ', 'proqram']

    Yaradılmış funksiya aşağıdakı `test case`-ləri ödəyən testlərdən keçməlidir.

    - `Giriş verilənləri ==> ['komputer', 'klaviatura', 'monitor', 'proqramçı']. Gözlənilən nəticə ==> ['klaviatura', 'proqramçı']`

    - `Giriş verilənləri ==> ['alma', 3, True, 'proqramçı']. Gözlənilən nəticə ==> ['alma', 'proqramçı']`

* `Person` class-ı yaradın. Bu class-ın `name` və `surname` field-ləri olmalıdır. Bu class-ın `get_fullname()` adlı və 'Name Surname' return edən method yaradın.

    **Nümunə** :bookmark_tabs:

        >>> person = Person('anar', 'veliyev')
        >>> person.get_fullname() ==> 'Anar Veliyev'

    Yaradılmış funksiya aşağıdakı `test case`-ləri ödəyən testlərdən keçməlidir.

    - `Giriş verilənləri ==> koroglu, mirzeyev. Gözlənilən nəticə ==> Koroglu Mirzeyev`
    - `Person` class-dan obyekt yaradıb onun `Person` class-nın instance-ı olduğunu yoxlayan test case yazın

**Powered by [TechAcademy](https://www.tech.edu.az/)**
