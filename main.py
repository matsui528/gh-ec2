import argparse
import subprocess
import json
import sys
from pathlib import Path


parser = argparse.ArgumentParser(prog="ec2", description="Simple helper commands to interact with AWS EC2 instances")
parser.add_argument("action",
                    choices=["status", "start", "stop", "ssh", "nautilus", "ip", "config", "list"],
                    help="Operation on instances")
parser.add_argument("instance", nargs='?', default=None, help="Instance name")
parser.add_argument("--config",
                    default="~/.instance_list.json",
                    help="Path to a config json file")


def get_ip(instance_id, profile):
    ip = subprocess.run("aws ec2 describe-instances --instance-ids {} "
                        "--query 'Reservations[0].Instances[0].PublicIpAddress' --profile {}".format(instance_id, profile),
                        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf8")
    return ip.strip().strip('"')  # '"XX.XXX.XX.XXX"\n' -> 'XX.XXX.XX.XXX'


if __name__ == '__main__':
    args = parser.parse_args()
    p = Path(args.config).expanduser()  # expand "~"
    
    # (1) If action is "config" or "list", we don't care an instance argment
    if args.action == "config":
        # Append a new instance data interactively
        print(f"Append a new instance data to the config file: {args.config}")
        print("Instance name (e.g., my_gpu_instance)")
        instance_name = input("> ") or None
        if instance_name is None:
            sys.exit("Error: write an instance name")
        print("Instance ID (e.g., i-07hgaxses4adf097a)")
        instance_id = input("> ") or None
        if instance_id is None:
            sys.exit("Error: write an instance id")
        print('Profile (default: "default")')
        profile = input("> ") or "default"
        print('Path to the key (default: "~/.ssh/id_rsa")')
        path_key = input("> ") or "~/.ssh/id_rsa"
        print(f"instance_name: {instance_name}")
        print(f"instance_id: {instance_id}")
        print(f"profile: {profile}")
        print(f"path_key: {path_key}")

        if p.exists():
            with p.open("rt") as f:
                config = json.load(f)
        else:
            config = []

        config.append({
            "instance_name": instance_name,
            "instance_id": instance_id,
            "profile": profile,
            "path_key": path_key
        })

        with p.open("wt") as f:
            json.dump(config, f, sort_keys=True, indent=4)

        sys.exit()

    elif args.action == "list":
        # Just print out the config file
        if not p.exists():
            print("No instances")
        else:
            with p.open("rt") as f:
                from pprint import pprint
                pprint(json.load(f))
        sys.exit()
        
    # (2) If action is not "config"/"list", we need an instance argment
    if args.instance is None:
        sys.exit(f"Error: instance name is not specified")  

    with p.open("rt") as f:
        config = json.load(f)

    instance_id, instance_name, path_key, profile = None, None, None, None
    for c in config:
        # Find the instance specified by args.instance from the config gile
        if c["instance_name"] == args.instance:
            instance_id, path_key, profile = c["instance_id"], c["path_key"], c["profile"] 

    if instance_id is None:
        sys.exit(f"Error: Cannot find {args.instance} in {args.config}")

    if args.action == "start":
        subprocess.run(f"aws ec2 start-instances --instance-ids {instance_id} --profile {profile}", shell=True)
    elif args.action == "stop":
        subprocess.run(f"aws ec2 stop-instances --instance-ids {instance_id} --profile {profile}", shell=True)
    elif args.action == "status":
        subprocess.run(f"aws ec2 describe-instance-status --instance-ids {instance_id} --profile {profile}", shell=True)
    elif args.action == "ip":
        print(get_ip(instance_id, profile))
    elif args.action == "ssh":
        ip = get_ip(instance_id, profile)
        subprocess.run(f"ssh -i {path_key} ubuntu@{ip}", shell=True)
    elif args.action == "nautilus":
        ip = get_ip(instance_id, profile)
        subprocess.run(f"ssh-add {path_key}", shell=True)
        subprocess.run(f"nautilus sftp://ubuntu@{ip}", shell=True)  



