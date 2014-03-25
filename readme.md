django-template (β)
===================

A <cite>Django</cite> project template.

## Prerequisites
* [Python ~ 3.3.3](http://www.python.org/)
* [NPM](https://npmjs.org/)
* [Gulp](http://gulpjs.com/)
* [Compass](http://compass*style.org/)
* [Bower](http://bower.io/)

## Getting started
### Setup project
#### Prepare project
Start with creating a new <cite>Django</cite> project based on this project template:

```bash
git clone git@github.com:adriancmiranda/django-template.git
```

```bash
chmod +x makevenv && . makevenv
```

```bash
django-admin.py startproject --template=https://github.com/adriancmiranda/django-template/zipball/master <project_name>
```

## Learn to use
### Django
* [Aprendendo Django (pt-br)][aprendendo_django]
* [Getting started with Pillow][requirement_pillow]
* [Getting started with South][requirement_south]

### NPM
* [Learn to use npmignore][npm_learn_to_use_npmignore] [_(sample)_][npm_sample_npmignore]
* [Learn to use npmrc][npm_learn_to_use_npmrc]

### Gulp
* [Getting started with gulp-util][gulp_util]
* [Getting started with gulp-component][gulp_component]
* [Getting started with gulp-jsonlint][gulp_jsonlint]
* [Getting started with gulp-coffeelint][gulp_coffeelint]
* [Getting started with gulp-jshint][gulp_jshint]
* [Getting started with gulp-jscs][gulp_jscs]
* [Getting started with gulp-requirejs][gulp_requirejs]
* [Getting started with gulp-coffee][gulp_coffee]
* [Getting started with gulp-compass][gulp_compass]
* [Getting started with gulp-changed][gulp_changed]
* [Getting started with gulp-cached][gulp_cached]
* [Getting started with gulp-concat][gulp_concat]
* [Getting started with gulp-autoprefixer][gulp_autoprefixer]
* [Getting started with gulp-plumber][gulp_plumber]
* [Getting started with gulp-uglify][gulp_uglify]
* [Getting started with gulp-imagemin][gulp_imagemin]
* [Getting started with gulp-htmlmin][gulp_htmlmin]
* [Getting started with gulp-svgmin][gulp_svgmin]
* [Getting started with gulp-webp][gulp_webp]
* [Getting started with gulp-clean][gulp_clean]
* [Getting started with gulp-livereload][gulp_livereload]
* [Getting started with gulp-connect][gulp_connect]
* [Getting started with gulp-watch][gulp_watch]
* [Getting started with gulp-zip][gulp_zip]
* [Getting started with gulp-notify][gulp_notify]

### Compass
* [SASS CSS Importer][sass_css_importer]

### Coffee
* [Coffee Script][coffee_script]

### Heroku
* [Deploying with Git][heroku_deploying_with_git]
* [Managing Multiple Environments for an App][heroku_multiple_environments]
* [Getting started with Django][heroku_getting_started_with_django]
* [Django and Static Assets][heroku_django_assets]
* [Configuration and Config Vars][heroku_config_vars]
* [Slug Compiler][heroku_slug_compiler]
* [Logging][heroku_logging]

## Support
Bugs and issues should be reported via the [issue tracker][issue_tracker].

## Contributing
1. [Fork it][fork_it]
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin my-new-feature`).
5. Create new [Pull request][pull_request].

<!-- project links -->
[fork_it]: https://github.com/adriancmiranda/django-template/fork "Fork it"
[pull_request]: https://github.com/adriancmiranda/django-template/compare/ "Pull request"
[issue_tracker]: http://github.com/adriancmiranda/am.io/issues "Issue tracker"

<!-- django links -->
[aprendendo_django]: http://www.aprendendodjango.com/organizando-as-coisas-com-tags/ "Aprendendo Django"
[requirement_pillow]: http://effbot.org/imagingbook/introduction.htm "Getting started with Pillow"
[requirement_south]: http://south.readthedocs.org/en/latest/tutorial/part1.html "Getting started with South"

<!-- npm links -->
[npm_learn_to_use_npmrc]: https://www.npmjs.org/doc/files/npmrc.html "Getting started with npmrc"
[npm_learn_to_use_npmignore]: https://caurea.org/2012/02/11/learn-to-use-npmignore.html "Learn to use npmignore"
[npm_sample_npmignore]: https://github.com/npm/npm/blob/master/.npmignore "npmignore sample"

<!-- Gulp links -->
[gulp_util]: https://www.npmjs.org/package/gulp-util "Getting started with gulp-util"
[gulp_component]: https://www.npmjs.org/package/gulp-component "Getting started with gulp-component"
[gulp_jsonlint]: https://www.npmjs.org/package/gulp-jsonlint "Getting started with gulp-jsonlint"
[gulp_coffeelint]: https://www.npmjs.org/package/gulp-coffeelint "Getting started with gulp-coffeelint"
[gulp_jshint]: https://www.npmjs.org/package/gulp-jshint "Getting started with gulp-jshint"
[gulp_jscs]: https://www.npmjs.org/package/gulp-jscs "Getting started with gulp-jscs"
[gulp_requirejs]: https://www.npmjs.org/package/gulp-requirejs "Getting started with gulp-requirejs"
[gulp_coffee]: https://www.npmjs.org/package/gulp-coffee "Getting started with gulp-coffee"
[gulp_compass]: https://www.npmjs.org/package/gulp-compass "Getting started with gulp-compass"
[gulp_changed]: https://www.npmjs.org/package/gulp-changed "Getting started with gulp-changed"
[gulp_cached]: https://www.npmjs.org/package/gulp-cached "Getting started with gulp-cached"
[gulp_concat]: https://www.npmjs.org/package/gulp-concat "Getting started with gulp-concat"
[gulp_autoprefixer]: https://www.npmjs.org/package/gulp-autoprefixer "Getting started with gulp-autoprefixer"
[gulp_plumber]: https://www.npmjs.org/package/gulp-plumber "Getting started with gulp-plumber"
[gulp_uglify]: https://www.npmjs.org/package/gulp-uglify "Getting started with gulp-uglify"
[gulp_imagemin]: https://www.npmjs.org/package/gulp-imagemin "Getting started with gulp-imagemin"
[gulp_htmlmin]: https://www.npmjs.org/package/gulp-htmlmin "Getting started with gulp-htmlmin"
[gulp_svgmin]: https://www.npmjs.org/package/gulp-svgmin "Getting started with gulp-svgmin"
[gulp_webp]: https://www.npmjs.org/package/gulp-webp "Getting started with gulp-webp"
[gulp_clean]: https://www.npmjs.org/package/gulp-clean "Getting started with gulp-clean"
[gulp_livereload]: https://www.npmjs.org/package/gulp-livereload "Getting started with gulp-livereload"
[gulp_connect]: https://www.npmjs.org/package/gulp-connect "Getting started with gulp-connect"
[gulp_watch]: https://www.npmjs.org/package/gulp-watch "Getting started with gulp-watch"
[gulp_zip]: https://www.npmjs.org/package/gulp-zip "Getting started with gulp-zip"
[gulp_notify]: https://www.npmjs.org/package/gulp-notify "Getting started with gulp-notify"

<!-- grunt links -->
[grunt_getting_started]: http://gruntjs.com/getting-started "Getting started with Grunt"
[grunt_configuring_tasks]: http://gruntjs.com/configuring-tasks "Configuring tasks with Grunt"
[grunt_shelljs]: https://www.npmjs.org/package/shelljs "Getting started with shelljs"
[grunt_jshint]: http://www.jshint.com/docs/options/ "Getting started with jshint"
[grunt_jsonlint]: https://www.npmjs.org/package/grunt-jsonlint "Getting started with grunt-jsonlint"
[grunt_coffeelint]: https://www.npmjs.org/package/grunt-coffeelint "Getting started with grunt-coffeelint"
[grunt_contrib_jshint]: https://www.npmjs.org/package/grunt-contrib-jshint "Getting started with grunt-contrib-jshint"
[grunt_jscs]: https://www.npmjs.org/package/jscs "Getting started with jscs"
[grunt_jscs_checker]: https://www.npmjs.org/package/grunt-jscs-checker "Getting started with grunt-jscs-checker"
[grunt_contrib_requirejs]: https://www.npmjs.org/package/grunt-contrib-requirejs "Getting started with grunt-contrib-requirejs"
[grunt_contrib_coffee]: https://www.npmjs.org/package/grunt-contrib-coffee "Getting started with grunt-contrib-coffee"
[grunt_contrib_compass]: https://www.npmjs.org/package/grunt-contrib-compass "Getting started with grunt-contrib-compass"
[grunt_contrib_imagemin]: https://www.npmjs.org/package/grunt-contrib-imagemin "Getting started with grunt-contrib-imagemin"
[grunt_svgmin]: https://www.npmjs.org/package/grunt-svgmin "Getting started with grunt-svgmin"
[grunt_contrib_clean]: https://www.npmjs.org/package/grunt-contrib-clean "Getting started with grunt-contrib-clean"
[grunt_contrib_connect]: https://www.npmjs.org/package/grunt-contrib-connect "Getting started with grunt-contrib-connect"
[grunt_contrib_watch]: https://www.npmjs.org/package/grunt-contrib-watch "Getting started with grunt-contrib-watch"

<!-- compass links -->
[sass_css_importer]: https://github.com/chriseppstein/sass-css-importer "SASS CSS Importer"

<!-- coffee links -->
[coffee_script]: http://coffeescript.org "Coffee Script"

<!-- heroku links -->
[heroku_deploying_with_git]: https://devcenter.heroku.com/articles/git "Deploying with Git"
[heroku_multiple_environments]: https://devcenter.heroku.com/articles/multiple-environments "Managing Multiple Environments for an App"
[heroku_getting_started_with_django]: https://devcenter.heroku.com/articles/getting-started-with-django "Getting started with Django"
[heroku_django_assets]: https://devcenter.heroku.com/articles/django-assets "Django and Static Assets"
[heroku_config_vars]: https://devcenter.heroku.com/articles/config-vars "Configuration and Config Vars"
[heroku_slug_compiler]: https://devcenter.heroku.com/articles/slug-compiler "Slug Compiler"
[heroku_logging]: https://devcenter.heroku.com/articles/logging "Logging"

<!-- helpfull links -->
[manifest.in]: http://docs.python.org/2/distutils/sourcedist.html "MANIFEST.in file"
[editorconfig]: http://editorconfig.org "Editor Config"
[travisci]: http://docs.travis-ci.com/pt-BR/user/languages/python/ "Travis CI"
