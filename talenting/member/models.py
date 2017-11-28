from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email=email, password=password,
                                first_name=first_name, last_name=last_name)
        user.is_active = True
        user.is_admin = True

        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    is_host = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def write_review_to_guest(self, guest_pk, review, recommend):
        '''
        :param guest_pk: 호스트 권한을 가진 유저가 게스트에게 리뷰를 남기는 메소드.
        :return: 리뷰가 새로 생성되었으면 True, 아니면 False
        '''
        if self.is_host and not self.user_review_about_guest.filter(host=self).exists():
            GuestReview.objects.create(
                host=self,
                guest=User.objects.get(pk=guest_pk),
                review=review,
                recommend=recommend
            )
            return True
        return False

    def get_guest_review_by_hosts(self):
        '''해당 게스트에게 호스트가 등록한 리뷰의 전체 리스트를 반환'''
        return self.user_review_about_guest.filter(guest=self)

    # def get_user_average_rating(self):
    #     '''유저 레이팅의 평균을 소수점으로 반환'''
    #     user_reviews = self.user_review_about_guest.filter(guest=self)
    #     if user_reviews:
    #         user_ratings = [review.rating for review in user_reviews]
    #         return float("{0:.1f}".format(sum(user_ratings) / len(user_reviews)))
    #     return float(0)

    def get_number_of_recommendation_of_guest(self):
        user_reviews = self.get_guest_review_by_hosts()
        recommend_num = 0
        for user_review in user_reviews:
            if user_review.recommend:
                recommend_num += 1
        return recommend_num


class GuestReview(models.Model):
    '''호스트가 숙박한 게스트를 평가할 때 사용하는 모델'''
    host = models.ForeignKey(User, related_name='user_review_by_host')
    guest = models.ForeignKey(User, related_name='user_review_about_guest')
    review = models.TextField()
    recommend = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
