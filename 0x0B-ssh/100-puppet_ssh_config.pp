# Client configuration file with puppet

file_line { 'IdentityFile':
  path    => '/etc/ssh/ssh_config',
  match   => 'IdentityFile ~/.ssh/id_rsa',
  replace => 'true',
  line    => 'IdentityFile ~/.ssh/school'
}
file_line { 'PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  match   => 'PasswordAuthentication yes',
  replace => 'true',
  line    => 'PasswordAuthentication no'
}
