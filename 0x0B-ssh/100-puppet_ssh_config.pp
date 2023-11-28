#using puppet to make changes to the default ssh config file

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/your_username/.ssh/config',  # Update 'your_username' with your actual username
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
  before => 'Host *',
}
