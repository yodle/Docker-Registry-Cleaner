from app import untag, images, scrub

commands = {'untag': untag,
            'images': images,
            'scrub': scrub}

def run(command):
    if not command in commands:
        raise ValueError()
    return commands[command]()
