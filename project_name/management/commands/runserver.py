# -*- coding: utf-8 -*-

from optparse import make_option
from django.conf import settings
from django.core.management.commands.runserver import Command as RunserverCommand
import atexit, signal, subprocess, os

class Command(RunserverCommand):
	option_list = RunserverCommand.option_list + (
		make_option(
			  '--gulp'
			, help='Specifies the project file for a Gulpfile.js in settings.py, and, runs gulp watch at the same time as runserver'
			, dest='gulpfile'
			, action='store_false'
			, default=settings.GULPFILE
		),
	)

	def run(self, *args, **options):
		"""Runs the server and the gulp watch process"""
		use_reloader = options.get('use_reloader')
		if settings.DEBUG and use_reloader and os.environ.get('RUN_MAIN') != 'true':
			"""RUN_MAIN Environment variable is set to None the first time the
			runserver command is start, on every reload after a code change if the
			option 'use_reloader' is set (by default it's) RUN_MAIN is set on 'true'.
			"""
			self.gulpfile = options.get('gulpfile')
			if not os.path.exists(self.gulpfile):
				self.stdout.write('>>> Didn\'t found a %r project' % self.gulpfile)
			else:
				self.start_gulp_watch()
		super(Command, self).run(*args, **options)

	def start_gulp_watch(self):
		self.stdout.write(self.style.NOTICE('>>> Starting the gulp watch command for %r') % self.gulpfile + '\n')
		self.gulp_process = subprocess.Popen(
			  ['gulp watch --gulpfile %s --base=.' % self.gulpfile]
			, shell=True
			, stdin=subprocess.PIPE
			, stdout=self.stdout
			, stderr=self.stderr
		)
		self.stdout.write(self.style.NOTICE('>>> Gulp watch process on pid %r' % self.gulp_process.pid) + '\n')
		def kill_gulp_project(pid):
			self.stdout.write(self.style.NOTICE('>>> Closing gulp watch process') + '\n')
			os.kill(pid, signal.SIGTERM)
		atexit.register(kill_gulp_project, self.gulp_process.pid)
