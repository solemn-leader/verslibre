import collections


user_seeds = collections.defaultdict(set)


a_m = ['зеленый', 'тусклый', 'шустрый', 'обворожительный', 'неожиданный', 'молодой', 'снисходительный',
     'мудрый', 'безрассудный', 'застенчивый', 'вальяжный', 'сообразительный', 'воодушевленный',
     'веселый', 'семейный', 'одинокий', 'незадачливый', 'агрессивный', 'настойчивый', 'толерантный',
     'февральский', 'сентябрьский', 'ежедневный', 'пятничный', 'доброкачественный', 'кожаный',
     'заунывный', 'занудный', 'звёздный', 'лунный', 'добрососедский', 'породистый', 'лютый',
     'болтливый', 'бессмертный', 'задумчивый', 'воображаемый', 'вкрадчивый', 'симфонический']

n_m = ['дом', 'аванс', 'ковид', 'друг', 'идиот', 'ребенок', 'воробей',
'лист', 'сон', 'день', 'идиот', 'дуб', 'тополь', 'зуб', 'дьявол', 'бог',
'кашель', 'кошелек', 'путь', 'тупик', 'бродяга', 'интеллект', 'совет', 'тупик', 'ктулху',
'зачёс', 'маникюр', 'понедельник', 'вторник', 'четверг', 'январь', 'февраль',
'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
'декабрь', 'микроб', 'кузнечик', 'вурдалак', 'ухряб', 'кабанчик', 'стон', 'вскрик',
'самурай', 'сабантуй', 'апофеоз']


a_f = ['престарелая', 'угрюмая', 'очаровательная', 'снисходительная', 'воодушевленная', 'щастенчивая', 'привлекательная',
     'мрачная', 'волнительная', 'оранжевая', 'доверительная', 'родная', 'замерзшая', 'уставшая',
     'коренная', 'кокетливая', 'игривая', 'полуночное', 'апрельская', 'октябрьская', 'вечерняя', 'субботняя',
     'зловредная', 'силиконовая', 'солнечная', 'вечнозелёная', 'сапфировая', 'храбрая', 'колченогая', 'суровая',
     'зимняя', 'космическая', 'лживая', 'послеобеденная', 'голубоглазая', 'хромая', 'беспородная', 'лютая',
     'вдумчивая', 'измождённая', 'кудрявая', 'джазовая']

n_f = ['вакцина', 'прививка', 'девушка', 'женщина', 'идея', 'ночь', 'голова',
'дурочка', 'рябина', 'ива', 'чайка', 'смерть', 'жизнь', 'судьба', 'рифма',
'кровь', 'дорога', 'могила', 'еда', 'гроза', 'осень', 'зима', 'весна',
'прическа', 'беседа', 'рекомендация', 'коза', 'подружка', 'совесть',
'ресничка', 'расческа', 'пятница', 'суббота', 'кракозябра', 'оттепель', 'капель',
'депрессия', 'инфляция', 'опухоль', 'эпитафия', 'импровизация']


a_n = ['обезвоженное', 'счастливое', 'последнее', 'новое', 'фиолетовое', 'мерцающее', 'снисходительное',
       'кредитное', 'культурное', 'иностранное', 'ночное', 'утреннее', 'злорадное', 'игривое', 'обеденное',
       'синеглазое', 'июльское', 'декабрьское', 'утреннее', 'воскресное', 'полноводное', 'застенчивое',
       'райское', 'чистосердечное', 'любовное', 'косматое']
n_n = ['утро', 'похмелье', 'зелье', 'лекарство', 'окно', 'чудо',
'явление', 'марево', 'зарево', 'счастье', 'лето', 'очарование', 'вдохновение', 'воскресенье',
'зазеркалье', 'харакири', 'анимэ', 'послевкусие', 'пробуждение', 'смятение', 'сердцебиение'
]


a_p = ['железные', 'острые', 'последние', 'верные', 'ржавые', 'кургузые', 'простые', 'забытые', 'семейные', 'вечные',
     'сладострастные', 'опухшие', 'январские', 'мартовские', 'алюминиевые', 'запредельные', 'сумасбродные',
     'непокорные', 'первородные', 'запредельные', 'ошалевшие']
n_p = ['пассатижи', 'ножницы', 'дожди', 'деньги', 'друзья', 'долги', 'слезы',
'мысли', 'люди', 'листья', 'березы', 'волосы', 'воробьи', 'чайки', 'клочки',
'птицы', 'заморозки', 'замыслы']


n_gen = ['судьбы', 'страданий', 'любви', 'срасти', 'раздумий', 'одиночества', 'ночи', 'дьявола',
         'лета', 'осени', 'мечтаний']


def generate_seeds(user_id):
    seeds = set()
    for _ in range(100):
        template = random.choice('an_m an_f an_n an_p n_n'.split())
        seed = None
        if template == 'an_m':
            a = random.choice(a_m)
            n = random.choice(n_m)
            seed = a + ' ' + n
        elif template == 'an_f':
            a = random.choice(a_f)
            n = random.choice(n_f)
            seed = a + ' ' + n
        elif template == 'an_n':
            a = random.choice(a_n)
            n = random.choice(n_n)
            seed = a + ' ' + n
        elif template == 'an_p':
            a = random.choice(a_p)
            n = random.choice(n_p)
            seed = a + ' ' + n
        elif template == 'n_n':
            n = random.choice(list(itertools.chain(n_m, n_f, n_n, n_p)))
            n2 = random.choice(n_gen)
            seed = n + ' ' + n2

        if seed and seed not in user_seeds[user_id]:
            seeds.add(seed)
            user_seeds[user_id].add(seed)
            if len(seeds) >= 3:
                break

    return list(seeds)
