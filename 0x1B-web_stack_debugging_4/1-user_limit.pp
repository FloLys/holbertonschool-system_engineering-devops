# increase ULIMIT traffic bottleneck

# Change defaults file
exec { 'fix-file':
  command => 'sed -i "s/holberton//" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
