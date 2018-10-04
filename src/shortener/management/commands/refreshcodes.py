from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrUrls 



class Command(BaseCommand):
	help = 'Refreshes all KirrUrl shortcodes'

	def handle(self, *args, **options):
		return KirrUrls.objects.refresh_shortcodes()