from config.stages import get_stage

class Endpoints:

    STAGE = get_stage()

    create_user = f"{STAGE}/users"