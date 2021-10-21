# JBD Python  :snake:

Aşağıdakı tapşırıqları həll etməyinizi tələb edirik. Əvvəlcə tələbləri oxumağı unutmayın.
#### Tapşırıqları həll etmək üçün bilməli olduğunuz mövzular :brain:

* Generators
* Iterators
* Zip, Filter, Map, Reduce methods


**Qeydlər**: :pushpin:
* Tapşırıqları vaxtında həll etməyi və göndərməyi unutmayın :hourglass_flowing_sand:
### Tapşırıqlar :dart:

* Arqument kimi rəqəm qəbul edən funksiya yazın. Funksiya hər müraciətdə daxil edilmiş rəqəmin bölünənlərini qaytarmalıdır.

    **Nümunə** :bookmark_tabs:

            gen_multiple_of_two = get_next_multiple(2)
            next(gen_multiple_of_two) # 2
            next(gen_multiple_of_two) # 4
            next(gen_multiple_of_two) # 6
            next(gen_multiple_of_two) # 8
            
            gen_multiple_of_thirteen = get_next_multiple(13)

            next(gen_multiple_of_thirteen) # 13
            next(gen_multiple_of_thirteen) # 26
            next(gen_multiple_of_thirteen) # 39
            next(gen_multiple_of_thirteen) # 52

* `[3, 4, 5, 7, 8, 9]` list-i verilmişdir. `Map` method-undan istifadə edərək listin bütün elementlərini kvadrata yüksəldin.
* `[3, 32, 56, 45, 22, 60, 99]` list-i verilmişdir. `Filter` methodundan istifadə edərək list-in 3-ə və 5-ə bölünən elementlərini qaytarın
* `ad=['Babək', 'Ali', 'Koroğlu']` `soyad=['Veliyev', 'Ahmedov', 'Recebov']` `yaş=[23, 54, 98]`

* `Zip` method-u adları, soyaqları və yaşları bir list-də qruplaşdırın.

    **Nəticə** :label:

        >> [('Babək', 'Veliyev', 23), ('Ali', 'Ahmedov', 54), ('Koroğlu', 'Recebov', 98)]

* `Reduce` method-u vasitəsiylə `[3, 5, 6, 7, 8]` list-nin bütün elementlərin cəmini hesablayın

**Powered by [TechAcademy](https://www.tech.edu.az/)**
