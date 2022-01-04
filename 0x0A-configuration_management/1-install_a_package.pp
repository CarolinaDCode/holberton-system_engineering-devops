# install puppet-lint 2.5.0
package { 'puppet-lint':
  ensure   => '2.5.0',
  name     => 'puppet-lint',
  provider => 'gem',
}