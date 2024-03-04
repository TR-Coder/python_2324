# Dates

## Tipus disponibles
* __datetime.date__
    * Atributs: _year_, _month_, _day_

* __datetime.time__
    * Atributs: _hour_, _minute_, _second_, _microsecond_, _tzinfo_

* __datetime.datetime__
    * Atributs: _year_, _month_, _day_, _hour_, _minute_, _second_, _microsecond_, _tzinfo_

* __datetime.timedelta__
    *  Atributs: _date_, _time o datetime_, a una resolución de microsegundos.

## date
```python
class date(year, month, day)
classmethod date.today()
```

```python
d1 = datetime.date(2002, 12, 31)
h1 = datetime.date.today()
y1 = datetime.date.today().year     #Retorna el dia de la setmana, dilluns és 1 y el diumenge és 7.
sm = datetime.date.isoweekday()
d1.replace(day=26)
```
### Mètodes
* date.replace(year=self.year, month=self.month, day=self.day)
* date.strftime(format): Retorna una cadena amb un format determinat.

    Alguns codis de format (dos dígits):
    * %H (hora 24 hores), %M (minuts), %S (segons)
    * %d (dia), %m (mes), %y(any 2 digits), %Y (any 4 dígits), .

## datetime
```python
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
classmethod datetime.now()   # data i hora d'ara
classmethod datetime.combine(date, time)    # Crea un datetime a partir d'un date i un time
classmethod datetime.strptime(cadena, format)  # Crea un datetime a partir de la cadena que li passen, la qual té el format especificat. Llança ValueError si le format de la cadena no casa amb l'especificat.
```

### Atributs
* datetime.year
* datetime.month
* datetime.day
* datetime.hour
* datetime.minute
* datetime.second
* datetime.microsecond

# Mètodes
* datetime.date()
* datetime.time()
* datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
* datetime.weekday(): Dia de la setmana on 0 és dilluns i 6 és diumenge.
* datetime.isoweekday(): Dia de la setmana on 1 és dilluns i 7 és diumenge.
* datetime.strftime(format): Retorna una cadena amb el format especificat.

## time
```python
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

### atributs
time.hour
time.minute
time.second
time.microsecond

### mètodes
* time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
* time.strftime(format): Retorna una cadena amb el format especificat.



## timedelta
```python
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

Només s'emmagatzemen days, seconds i microseconds. Els milisegons es transformen a microsegons, els minuts a segons, les hores a segons i les setmanes a dies.

Podem operar amb +, -, *, //, % ...

Un objecte timedelta es vertader si no es igual a timedelta(0).

### Mètodes
* timedelta.total_seconds()

Retorna el nombre de segons. Equival a td / timedelta(seconds=1).


Per a unitats que no siguen segons hem de fer la divisió directamente. Per exemple: td / timedelta(microseconds=1)


