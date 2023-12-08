# Install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',  # Specify the desired version
  provider => 'pip3',   # Use the pip3 provider for Python 3
}
