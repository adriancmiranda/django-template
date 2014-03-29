# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import Command as CollectstaticCommand
import os

class Command(CollectstaticCommand):
	def handle_noargs(self, **options):
		"""Make sure the media dir exists before we're running collecstatic."""
		if not os.path.exists(settings.MEDIA_ROOT):
			self.stdout.write('>>> MEDIA_ROOT not found, creating one.')
			os.makedirs(settings.MEDIA_ROOT)
		super(Command, self).handle_noargs(**options)
