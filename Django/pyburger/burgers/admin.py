from django.contrib import admin
# migration을 통해 DB에 테이블을 만든 모델을 불러오기
from burgers.models import Burger

# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
    
