# kill a process using pkil
exec { 'killmenow':
  command => 'pkill killmenow',
  provider => 'shell',
}