# Транслит для URL (ЧПУ)
Программа решает проблему клиента и генерирует транслит названий городов по следующим правилам:
- Создаёт транслит городов в скобках рядом с кириллическим названием городов.
- Должен сохраняться исходный порядок названий и строк.

Принимает файл TXT с названиями городов, разделёнными запятой:
```
Майкоп
Астрахань
Волгоград, Волжский, Камышин, Михайловка
Элиста
```
Выдает новй файл TXT с транслитом городов:
```
Майкоп (maykop)
Астрахань (astrahan)
Волгоград (volgograd), Волжский (volzhskiy), Камышин (kamyshin), Михайловка (mihaylovka)
Элиста (elista)
```

