class Agent:
    
    def __init__(self, agent_id, start_position: tuple, target_posistion: tuple):
        
        self.agent_id = agent_id

        self.start_position = start_position
        self.target_posistion = target_posistion
        self.current_posistion = start_position

        self.path = []
        self.agent_status = "ACTIVE" 

    def move_to(self, next_position: tuple):
        self.current_posistion = next_position
        
        if self.current_posistion == self.target_posistion:
            self.agent_status = "REACHED"

    def __repr__(self):
        return f"Agent(id={self.agent_id}, position={self.current_posistion}, status={self.agent_status})"