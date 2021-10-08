# Sky is the limit, let's bring that limit higher
exec { 'fileli':
  command  => 'sed -i "5s/15/10000/g" /etc/default/nginx; service nginx restart',
  provider => 'shell'
}
