import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    total_count = Passcard.objects.all().count()
    active_count = Passcard.objects.filter(is_active=True).count()
    print('Всего пропусков: ', total_count)
    print('Активных пропусков: ', active_count)
