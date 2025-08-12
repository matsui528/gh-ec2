# gh-ec2

Simple helper commands to interact with AWS EC2 instances via GitHub CLI extension


## Prerequisite
Install the followings.
- Python 3+
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [GitHub CLI](https://github.com/cli/cli#installation)

## Installation
```
gh extension install matsui528/gh-ec2
```

## Update
```
gh extension upgrade matsui528/gh-ec2
```




## Usage
- `gh ec2 config`
    - Add the instance's information to `~/.instance_list.json` interactively.
    - For exmple:
      ```console
      Instance name (e.g., my_gpu_instance)
      > my_high_memory_instance    <- Any name is fine
      Instance ID (e.g., i-07hgaxses4adf097a)
      > i-rld9jre423jdfe           <- You can obtain it by AWS EC2 console  
      Profile (default: "default")
      >                            <- Press enter if you use the default option
      Path to the key (default: "~/.ssh/id_rsa")
      >                            <- Press enter if you use the default option
      ```
- `gh ec2 list`
    - Show the information of all instances.
- `gh ec2 status INSTANCE_NAME`
    - See the status of the instance.
- `gh ec2 start INSTANCE_NAME`
    - Start the instance.
- `gh ec2 stop INSTANCE_NAME`
    - Stop the instance.
- `gh ec2 ssh INSTANCE_NAME`
    - Log in the instance by SSH.
- `gh ec2 nautilus INSTANCE_NAME`
    - Open the home directory of the instance remotely by nautilus.
- `gh ec2 ip INSTANCE_NAME`
    - Get the IP of the instance.

## Tips
- How to modify the config file?
    - Edit `~/.instance_list.json` directly.
- How to specify a different config file?
    - Run the command with `--config YOUR_CONFIG_FILE`, e.g., `gh ec2 config --config SOMEWHERE/my_config.json`