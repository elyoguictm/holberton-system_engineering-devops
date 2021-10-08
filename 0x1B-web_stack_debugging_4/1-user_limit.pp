# User limit task
exec { 'withlim':
  command  => 'echo "" > /etc/security/limits.conf',
  provider => 'shell'
}
