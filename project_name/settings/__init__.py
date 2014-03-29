# -*- coding: utf-8 -*-

import os, sys, logging

try:
	if os.environ.get('HOST_ROLE'):
		host_role = os.environ['HOST_ROLE']
		if host_role == 'production':
			from .production import *
		elif host_role == 'staging':
			from .staging import *
		else:
			from .localhost import *
	else:
		from .localhost import *
except ImportError:
	logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
