# fixing an extension inside wp-settings.php file

file { '/var/www/html/wp-includes/class-wp-locale.phpp':
    ensure => file,
    source => '/var/www/html/wp-includes/class-wp-locale.php'
}
