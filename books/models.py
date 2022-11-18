from django.db import models


class BookReview(models.Model):
    book_id = models.IntegerField(blank=False)
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    review = models.TextField(blank=False, default='')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Book ID {self.book_id} received a review and rating {self.rating}'
