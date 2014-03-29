(function (gulp, gulpLoadPlugins) {
	'use strict';
	//|**
	//| {{ project_name }}
	//|
	//| This file is the streaming build system
	//|
	//| .--------------------------------------------------------------.
	//| | NAMING CONVENTIONS:                                          |
	//| |--------------------------------------------------------------|
	//| | Singleton-literals and prototype objects | PascalCase        |
	//| |--------------------------------------------------------------|
	//| | Functions and public variables           | camelCase         |
	//| |--------------------------------------------------------------|
	//| | Global variables and constants           | UPPERCASE         |
	//| |--------------------------------------------------------------|
	//| | Private variables                        | _underscorePrefix |
	//| '--------------------------------------------------------------'
	//|
	//| Comment syntax for the entire project follows JSDoc:
	//| - http://code.google.com/p/jsdoc-toolkit/wiki/TagReference
	//|
	//| For performance reasons we're only matching one level down:
	//| - 'test/spec/{,*/}*.js'
	//|
	//| Use this if you want to recursively match all subfolders:
	//| - 'test/spec/**/*.js'
	//|
	//'*/
	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| variables and constants
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	var $ = gulpLoadPlugins({ pattern: '*', lazy: true });

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| lint
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('lint', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| scripts
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('scripts', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| images
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('images', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| theme
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('theme', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| watch
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('watch', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| build
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('build', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| clean
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('clean', [], function () {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| environ
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('localhost', [], function () {
		$.shelljs.exec('open https://github.com/adriancmiranda/django-template/');
	});
	gulp.task('development', function () {
		$.shelljs.exec('open https://github.com/adriancmiranda/django-template/');
	});
	gulp.task('staging', function () {
		$.shelljs.exec('open https://github.com/adriancmiranda/django-template/');
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| alias
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('default', ['watch']);

}(require('gulp'), require('gulp-load-plugins')));
