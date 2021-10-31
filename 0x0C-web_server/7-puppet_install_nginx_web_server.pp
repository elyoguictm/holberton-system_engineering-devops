# install and configure an Nginx server

package { 'nginx':
    ensure => present,
}

file { '/var/www/html/index.html':
    ensure  => present,
    path    => '/var/www/html/index.html',
    content => 'Hellow World',
}

file_line {'Adding_redirect':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _;',
    line   =>  '        rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['Adding_redirect'],
}
