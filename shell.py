from credit.models import Client, Account, Credit
from random import randint

client1 = Client.objects.create(name='Бердиев Н.Д', birth_year='1994-12-12', work_place='Codify')

client2 = Client.objects.create(name='Абидинов М.Р', birth_year='1997-7-11', work_place='Microsoft')

client3 = Client.objects.create(name='Рустамов Р.Р', birth_year='1999-8-25', work_place='Google')



account_1 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=2, client=client1)
account_2 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=3, client=client1)
account_3 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=4, client=client2)
account_4 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=5, client=client2)
account_5 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=6, client=client3)
account_6 = Account.objects.create(number=randint(1000000000000000, 9999999999999999), account_type=7, client=client3)


account_1.credits.create(sum=50000)
account_2.credits.create(sum=30000)
account_3.credits.create(sum=40000)
account_4.credits.create(sum=60000)
account_5.credits.create(sum=70000)
account_6.credits.create(sum=80000)

