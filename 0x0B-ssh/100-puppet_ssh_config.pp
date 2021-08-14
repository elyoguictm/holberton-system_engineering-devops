# Connect to a server
file_line {'Pass Auth':
    path  => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
    match  => 'IdentityFile ~/.ssh/id_rsa',
}
file_line { 'no pass':
  path   => '/etc/ssh/ssh_config',
  match  => 'PasswordAuthentication yes',
  line   => 'PasswordAuthentication no',
}