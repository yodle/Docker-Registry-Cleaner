import argparse
import sys
import pprint

from repository import Repository
pp = pprint.PrettyPrinter(indent=4)
    
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", help="the repository path")
    parser.add_argument("command", help="untag, validate, report, scrub, revert")
    parser.add_argument("--hostname", dest='hostname', nargs='*', help="the registry hostname. Required for untag")

    parser.add_argument("--path", dest='path', help="path to tmp directory to restore")
    args = parser.parse_args()
    return args #{'hostname': args.hostname, 'command': args.command, 'repository': args.repository}


def untag():
    # Not implemented yet
    return True

def scrub(repo):
    to_scrub = repo.unused_images()
    for img in to_scrub:
        repo.remove(img)
    return True

def revert(repo, path):
    print(repo, path)
    repo.revert(path)
    return True

def validate(repo):
    v = repo.validate()
    if v == set():
        print("The registry is in a valid state")
    else:
        print("The registry is in an invalid state. The following images are referenced but not present", v)
    return v

def report(repo):
    r = repo.report()
    print("The following images are unreferenced <image id: size on disk>:")
    pp.pprint(r)
    return r


def main():
    args = parse_args()
    print(args)
    repo = Repository(args.repository)
    
    if args.command == 'report':
        return report(repo)
    if args.command == 'validate':
        return validate(repo)
    if args.command == 'untag':
        return untag()
    if args.command == 'images':
        return images()
    if args.command == 'revert':
        path = args.path
        return revert(repo, path)
    if args.command == 'scrub':
        return scrub(repo)
    if args.command == 'purge':
        return purge()
    else:
        print("Invalid command %s" % command)
        sys.exit(1)
            
