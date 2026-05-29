from portal.models import *

#Создать двух пользователей.
User.objects.create_user('Sam_Isakov')
User.objects.create_user('s1mka')

#Создать два объекта модели Author, связанные с пользователями.
user1 = User.objects.first()
Author.objects.create(user_id=user1)
user2 = User.objects.last()
Author.objects.create(user_id=user2)

#Добавить 4 категории в модель Category.
Category.objects.create(name='Спорт')
Category.objects.create(name='Политика')
Category.objects.create(name='Финансы')
Category.objects.create(name='Наука')

#Добавить 2 статьи и 1 новость. #Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
author1 = Author.objects.first()
author2 = Author.objects.last()
category1 = Category.objects.get(pk=1)
category2 = Category.objects.get(pk=2)
category3 = Category.objects.get(pk=3)
category4 = Category.objects.get(pk=4)

Post.objects.create(author_id=author1, category='N', header='Итоги заседания МОК', text='Сегодня прошло заседание МОК, \
главной повесткой которого являлось возвращение России на международную спортивную арену. По итогам заседания было \
принято вернуть Олимпийский комитет России в состав МОК, также российские спортсмены теперь смогут выступать под флагом \
свой страны')
post = Post.objects.first()
post.categories.add(category1, category2)
Post.objects.create(author_id=author2, category='A', header='Конфликт в Иране - влияние на экономику', text='После \
начала операции США в Иране, стало понятно, что это очередная попытка Дональда Трампа расшатать мировую экономику для \
извлечения из этого выгоды. После "захвата" США Венесуэлы и взятием контроля над ее нефтью, Трампу очень выгодно \
поднять цены на нефть в мире')
post = Post.objects.last()
post.categories.add(category2, category3)
Post.objects.create(author_id=author1, category='A', header='3I-Atlas', text='Комитет ученых-астрономов во главе с \
Владимиром Сурдиным проанализировали поведение небесного тела под названием "3I-Atlas". Итогом анализа стал \
вывод - "3I-Atlas" - это "обычная", по меркам космоса, комета. Она не похожа ни на одну из известных в Солнечной \
системе комет, по размерам, составу и тд. По наблюдениям, у кометы появилась "реактивная тяга", из этого можно сделать \
вывод, что она, в ходе своего путешествия, не пролетала вблизи свезд, так как ее поверхность начала \
испаряться в процессе нагрева от Солнца, из-за этого и появилась реактивная тяга. Данная статья направлена на то, \
чтобы попытаться опровергнуть суждение о том, что "3I-Atlas" - космический искусственный аппарат.')
post = Post.objects.last()
post.categories.add(category2, category4)

#Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
post1 = Post.objects.first()
post2 = Post.objects.get(pk=2)
post3 = Post.objects.last()

user1 = User.objects.first()
user2 = User.objects.last()

Comment.objects.create(post_id=post1, user_id=user1, text='Наконец-то! А то мы все уже устали смотреть на этот \
беспредел! Все страны в мире творят что хотят, а все ограничения накалдывают только на Россию! И вообще, спорт \
должен быть вне политики!')
Comment.objects.create(post_id=post2, user_id=user2, text='У Трампа не просто так кликуха "Бульдозер". Этот чел \
буквально сносит все, что видит на своем пути')
Comment.objects.create(post_id=post2, user_id=user1, text='Кто-нибудь понял, Трамп все таки наш слоняра или нет?')
Comment.objects.create(post_id=post3, user_id=user2, text='Еще одно суждение в пользу того, что это не инопланетный \
корабль. Если они прилетели сюда с исследовательской миссией, то почему они тогда проигнорировали Землю? Комета \
буквально пролетела рядом почти со всеми планетами, кроме Земли. Да, может они как-то засекли наши радиоволны и \
вернутся к нам еще, но конечно, есть сомнения')

#Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.dislike()
post2.like()
post2.like()
post2.like()
post2.dislike()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.dislike()
post3.dislike()
post3.dislike()

com1 = Comment.objects.first()
com2 = Comment.objects.get(pk=2)
com3 = Comment.objects.get(pk=3)
com4 = Comment.objects.last()
com1.like()
com1.like()
com1.like()
com2.dislike()
com2.like()
com2.like()
com2.like()
com3.dislike()
com3.dislike()
com3.dislike()
com4.like()
com4.like()
com4.like()

#Обновить рейтинги пользователей.
author1 = Author.objects.first()
author1.update_rating()
author2 = Author.objects.last()
author2.update_rating()

#Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.order_by('-rating').values('user_id__username', 'rating').first()

#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
post = Post.objects.order_by('-rating').first()
post.preview()
Post.objects.order_by('-rating').values('date', 'author_id__user_id__username', 'header').first()


#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post_id=post).values('date','user_id' ,'user_id__username', 'rating', 'text')