

def resource(relative_path):
    import demoqa_test
    from pathlib import Path
    return (
        Path(demoqa_test.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )