from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    product_type = models.CharField(max_length=8, verbose_name='상품유형',
        choices=(
            ('단품', '단품'),
            ('세트', '세트'),
        )
    )
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'

class Comment(models.Model):
    member = models.ForeignKey("member.Member", on_delete=models.CASCADE, verbose_name='사용자')
    # django는 import로 참조할 수도 있고 문자열로 객체를 참조할 수도 있다(문자열 방법을 더 선호)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name='상품')
    content = models.TextField(verbose_name="댓글내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글'

class Like(models.Model):
    member = models.ForeignKey("member.Member", on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name='상품')

    class Meta:
        db_table = 'shinhan_product_like'
        verbose_name = '상품 좋아요'
        verbose_name_plural = '상품 좋아요'
