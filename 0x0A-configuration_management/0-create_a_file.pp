# create a file
file { 'holberton':
     ensure  => file,
     content => 'I love Puppet',
     owner   => 'www-data',
     group   => 'www-data',
     mode    => '0744',
}