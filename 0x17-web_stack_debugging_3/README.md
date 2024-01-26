# 0x17-web_stack_debugging_3

In this task we will use a useful tool `strace` to debug this task,
the target is a Wordpress website running on a LAMP stack

## task

find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet 

Hint:

- `strace` can attach to a current running process
- You can use `tmux` to run `strace` in one window and curl in another one

Requirements:

- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix
