from django.db import models


class Shoe(models.Model):
    DISCOUNT_PERCENTAGE = (
        ("10%", "10%"),
        ("20%", "20%"),
        ("50%", "50%"),
        ("75%", "75%"),

    )

    name = models.CharField(max_length=1000, verbose_name="Напишите понравившийся кроссовки")
    description = models.TextField(verbose_name="Напишите описание кроссовка")
    image_1 = models.URLField(verbose_name='Сюда вставлять ссылку на картинку')
    image_2 = models.URLField(verbose_name='Сюда вставлять ссылку на картинку')
    image_3 = models.URLField(verbose_name='Сюда вставлять ссылку на картинку')
    brand = models.CharField(max_length=100, verbose_name="Напишите сюда бренд")
    model = models.CharField(max_length=1000, verbose_name="Напишите какая модель кроссовка")
    category = models.CharField(max_length=1000, verbose_name="Напишите для какой задачи сделаны кроссовки")
    color = models.CharField(max_length=100, verbose_name="Напишите цвет кроссовка")
    size = models.CharField(max_length=100, verbose_name="Напишите какие размеры доступны")
    price = models.PositiveIntegerField(verbose_name="Цена")
    discount = models.CharField(max_length=100, choices=DISCOUNT_PERCENTAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}"


class CommentShoe(models.Model):
    shoe_comment = models.ForeignKey(Shoe, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name="comments")
    text = models.TextField(verbose_name="Напиши свое мнение о товаре")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shoe_comment} - {self.text}"
