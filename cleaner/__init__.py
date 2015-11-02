from app import untag, images, scrub, validate

commands = {'untag': untag,
            'images': images,
            'scrub': scrub,
            'validate': validate}

def run(command):
    if not command in commands:
        raise ValueError()
    return commands[command]()
