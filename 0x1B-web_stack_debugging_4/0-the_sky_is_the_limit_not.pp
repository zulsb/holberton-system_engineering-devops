# Fix Nginx
exec { 'fixing nginx':
  provider => 'shell';
  command  => "sed -i 's/-n 15/3000/g' /etc/default/nginx; service nginx restart",
}