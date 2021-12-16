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



## Usage
- `gh ec2 config`
    - Append the instance's information to `~/.instance_list.json` interactively.
    - For exmple:
      ```console
      Instance name (e.g., my_gpu_instance)
      > my_high_memory_instance    <- Anyname is fine
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
    - Log in the instance by SSH
- `gh ec2 nautilus INSTANCE_NAME`
    - Open the nautilus to the instance.
- `gh ec2 ip INSTANCE_NAME`
    - Get the IP of the instance.

