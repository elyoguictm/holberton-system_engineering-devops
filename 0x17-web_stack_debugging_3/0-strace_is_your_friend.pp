# Puppet program that fix the code
exec { 'debug':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/bin',
}
