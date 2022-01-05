# Modifying the ssh_config file, to configure the private key
# in ~ /.ssh /school and for password authentication.
file_line { 'Turn off passwd auth':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}
