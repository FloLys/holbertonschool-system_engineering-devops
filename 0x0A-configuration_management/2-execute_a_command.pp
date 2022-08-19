# Delete a process using exec
exec { '/killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
