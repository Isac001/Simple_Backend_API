class ValidationError(Exception):
    
    def __init__(self, error_list: list):

        self.errors = error_list

        super().__init__(f"Ocorreram {len(error_list)} erros de validação.")
    