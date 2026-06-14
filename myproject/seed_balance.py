import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from product.models import AppUser, Balance, Transaction, CoinLog

# User banao
user, _ = AppUser.objects.get_or_create(
    email='sara@vibe.com',
    defaults={'username': 'Sara', 'user_img': 'https://i.pravatar.cc/150?img=1'}
)
print(f"User ✅: {user.username}")

# Balance banao
balance, _ = Balance.objects.get_or_create(
    user=user,
    defaults={'amount_usd': 125.50, 'total_coins': 420}
)
print(f"Balance ✅: ${balance.amount_usd}")

# Transactions
Transaction.objects.get_or_create(
    user=user, type='credit', amount=50.00,
    description='Referral Bonus Received', status='completed'
)
Transaction.objects.get_or_create(
    user=user, type='debit', amount=12.00,
    description='AI Image Prompt Generation', status='completed'
)
print("Transactions ✅")

# Coin Logs
CoinLog.objects.get_or_create(
    user=user, type='earned', coins=100, description='Recharge Bonus'
)
CoinLog.objects.get_or_create(
    user=user, type='spent', coins=30, description='AI Video Upscale'
)
print("Coin Logs ✅")

print("\n🎉 Balance seed complete!")