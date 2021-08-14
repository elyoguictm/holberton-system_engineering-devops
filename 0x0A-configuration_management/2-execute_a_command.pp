#kill a process using pkil
exec { 'killmenow':
    command  => 'pkill -f "killmenow"',
    provider => 'shell',
}