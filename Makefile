RUBY := /usr/local/opt/ruby/bin
export PATH := $(RUBY):$(PATH)

run-server:
	bundle exec jekyll serve --livereload --watch

build:
	bundle exec jekyll build
