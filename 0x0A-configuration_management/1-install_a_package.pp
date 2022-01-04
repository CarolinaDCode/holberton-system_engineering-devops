# install puppet-lint 2.5.0
package { 'puppet-lint':
  name      => 'puppet-lint',
  ensure    => '2.5.0',
  provider  => 'gem',
}