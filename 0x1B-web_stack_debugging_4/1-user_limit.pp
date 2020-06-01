# Change the OS configuration with the holberton user.
exec {'Config-User':
  provider => 'shell',
  command  => "sed -i 's/nofile 5/nofile 1000/g' /etc/security/limits.conf;\
              sed -i 's/nofile 4/nofile 1000/g' /etc/security/limits.conf",
}