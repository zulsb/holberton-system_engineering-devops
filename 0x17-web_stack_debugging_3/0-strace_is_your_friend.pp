# Apache returns 500 and use this script to correct the configuration error.
exec { 'fixing wp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
