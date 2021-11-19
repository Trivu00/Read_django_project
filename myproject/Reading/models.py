from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Thể loại của bài đọc')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categores'



class ReadingBook(models.Model):
    name = models.CharField(max_length=200, help_text='Tên bài đọc')
    content_reading = models.TextField(help_text='Nội dung bài đọc')
    reading_translate = models.TextField(help_text='Nội dung bài đọc', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __int__(self):
        return self.name


class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    name_read = models.ForeignKey(ReadingBook, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = 'Questions'
