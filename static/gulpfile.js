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
	//| variables and constants - (gulpLoadPlugins)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	var _ = { app: './app', dist: './dist', tmpl: '../templates' },
	    $ = gulpLoadPlugins({ pattern: '*', lazy: true });

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| lint - (plumber, jshint, jscs)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('lint', function() {
		return gulp.src([
			'gulpfile.js',
			_.app + '/scripts/**/*.js',
			'!' + _.app + '/scripts/vendor/**/*.js'
		])
		.pipe($.plumber())
		.pipe($.jshint('.jshintrc'))
		.pipe($.jshint.reporter('default'))
		.pipe($.jscs());
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| test - (mocha)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('mocha', function () {
		gulp.src('test/*.js').pipe($.mocha({ reporter: 'list' }));
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| scripts - (plumber, size, notify)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('scripts', ['lint'], function() {
		return gulp.src([
			_.app + '/scripts/**/*.js',
			'!' + _.app + '/scripts/vendor/**/*.js'
		])
		.pipe($.plumber())
		.pipe($.concat('boot.min.js')).pipe($.uglify())
		.pipe(gulp.dest(_.dist + '/scripts'))
		.pipe($.size()).pipe($.notify({
			message: '<%= options.date %> ✓ script: <%= file.relative %>',
			templateOptions: {
				date: new Date()
			}
		}));
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| images - (cache, imagemin, svgmin, size, notify)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('images', [], function() {
		return gulp.src([
			_.app + '/*.{png,jpg,jpeg,gif,ico}',
			_.app + '/images/**/*.{png,jpg,jpeg,gif,ico}'
		]).pipe($.cache($.imagemin({
			optimizationLevel: 3,
			progressive: true,
			interlaced: true
		}))).pipe(gulp.dest(_.dist)).pipe($.size()).pipe($.notify({
			message: '<%= options.date %> ✓ image: <%= file.relative %>',
			templateOptions: {
				date: new Date()
			}
		}));
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| theme - (plumber, rubySass, util, autoprefixer, size, notify)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('theme', function() {
		return gulp.src([
			_.app + '/*.scss',
			_.app + '/theme/**/*.{sass,scss}'
		])
		.pipe($.plumber())
		.pipe($.rubySass({
			loadPath: [_.app + '/scripts/vendor'],
			require: ['sass-css-importer'],
			style: 'compressed',
			lineNumbers: true,
			sourcemap: true,
			compass: false,
			trace: true
		}).on('error', $.util.log))
		.pipe($.autoprefixer('last 1 version', '> 1%', 'ie 8'))
		.pipe(gulp.dest(_.dist))
		.pipe($.size())
		.pipe($.notify({
			message: '<%= options.date %> ✓ style: <%= file.relative %>',
			templateOptions: {
				date: new Date()
			}
		}));
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| Inject bower components - (htmlmin, useref)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('bower', [], function () {
		return gulp.src(_.tmpl + '/*.html')
		.pipe($.useref())
		.pipe(gulp.dest(_.dist));
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| watch - (watch)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('watch', function() {
		// Watch for changes in `app` dir
		gulp.src([
			_.app + '/*.css',
			_.app + '/fonts/**/*',
			_.app + '/scripts/**/*.js',
			_.app + '/**/*.{png,jpg,jpeg,gif,ico}'
		], { read: false }).pipe($.watch({}, function(files) {
			return files;
		})).pipe($.plumber());

		// Watch .{scss,sass} files
		$.watch({ glob: [_.app + '/**/*.{scss,sass}'] }, function() {
			gulp.start('theme');
		});

		// Watch .js files
		$.watch({ glob: [_.app + '/scripts/**/*.js'] }, function() {
			gulp.start('scripts');
		});

		// Watch image files
		$.watch({ glob: [_.app + '/**/*.{png,jpg,jpeg,gif,ico}'] }, function() {
			gulp.start('images');
		});

		// Watch bower files
		$.watch({ glob: [_.app + '/scripts/vendor/*'] }, function() {
			gulp.start('bower');
		});

		// Launch localhost
		gulp.start('localhost');
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| build
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('build', ['lint', 'mocha', 'scripts', 'theme', 'images'], function() {
		// N/A yet.
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| clean - (clean)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('clean', [], function() {
		var stream = gulp.src([
			_.dist + '/scripts',
			_.dist + '/images',
			_.dist + '/theme',
			_.dist + '/fonts'
		], { read: false });
		return stream.pipe($.clean());
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| environ - (shelljs)
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('localhost', [], function() {
		$.shelljs.exec('open http://localhost:8000');
	});
	gulp.task('development', function() {
		$.shelljs.exec('open https://github.com/adriancmiranda/django-template/tree/dev');
	});
	gulp.task('staging', function() {
		$.shelljs.exec('open https://github.com/adriancmiranda/django-template/');
	});

	//|**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	//| alias
	//'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	gulp.task('default', ['clean'], function() {
		gulp.start('build');
	});

}(require('gulp'), require('gulp-load-plugins')));
