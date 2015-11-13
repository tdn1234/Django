module.exports = function(grunt) {
'use strict';

    if (grunt.option('help')) {
        // Load all tasks so they can be viewed in the help: grunt -h or --help.
        require('load-grunt-tasks')(grunt);
    } else {
        // Use jit-grunt to only load necessary tasks for each invocation of grunt.
        require('jit-grunt')(grunt);
    }

    require('time-grunt')(grunt);
	grunt.initConfig({
		config: {
            baseDir: 'userprofile/',
            staticDir: '<%= config.baseDir %>/static/',
            libDir: '<%= config.staticDir %>/lib/',
            cssDir: '<%= config.staticDir %>/styles/',
            sassDir: '<%= config.baseDir %>/sass/',
            imagesDir: '<%= config.staticDir %>/images',
            generatedImagesDir: '<%= config.imagesDir %>/generated',
            scriptsDir: '<%= config.staticDir %>/scripts',
            fontsDir: '<%= config.staticDir %>/fonts/',
            iconFiles: '<%= config.imagesDir %>/svg/icons/*.svg',
            webfontTemplate: 'webfont/icon-template.css'
        },

        compass: {
            options: {
                sassDir: '<%= config.sassDir %>',
                cssDir: 'static/css',
                fontsDir: '<%= config.fontsDir %>',
                imagesDir: '<%= config.imagesDir %>',
                javascriptsDir: '<%= config.scriptsDir %>',
                httpGeneratedImagesPath: '../images',
                generatedImagesDir: '<%= config.generatedImagesDir %>',
                relativeAssets: true,
                outputStyle: 'expanded',
                debugInfo: false,
                importPath: [
                    '<%= config.libDir %>/sass/'
                ]
            },
            dev: {
                // Options object is required.
                options: {}
            },
            force: {
                options: {
                    force: true
                }
            },
            watch: {
                options: {
                    watch: true
                }
            },
            dist: {
                options: {
                    // Force to be certain the compile is correct.
                    force: true,
                    outputStyle: 'compressed',
                    noLineComments: true
                }
            }
        },

        watch: {
            icons: {
                files: [
                    '<%= config.iconFiles %>',
                    '<%= config.webfontTemplate %>'
                ],
                tasks: ['webfont:icons']
            }
        },
        concurrent: {
            options: {
                logConcurrentOutput: true
            },
            dev: [
                'watch',
                'compass:watch'
            ],
            dist: [
                'compass:dist'
            ]
        },
        webfont: {
            icons: {
                src: '<%= config.iconFiles %>',
                dest: '<%= config.fontsDir %>/icons',
                destCss: '<%= config.sassDir %>/globals',
                options: {
                    hashes: false,
                    htmlDemo: false,
                    relativeFontPath: '../fonts',
                    stylesheet: 'sass',
                    ligatures: true,
                    template: '<%= config.webfontTemplate %>',
                    templateOptions: {
                        baseClass: '',
                        classPrefix: 'icon-',
                        mixinPrefix: ''
                    }
                }
            }
        }
	});
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.registerTask('default', ['dev']);

	grunt.registerTask(
        'dev',
        'Compile Sass and watch for changes',
        // First compile so styles are available, then watch.
        ['webfont', 'compass:dev', 'concurrent:dev']
    );

    grunt.registerTask(
        'dist',
        'Build for deploy',
        ['webfont', 'concurrent:dist']
    );
}