# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, localhost):
        self.localhost = localhost
        self.user_name = None
        self.password = None
        
    
    def set_user(self, user_name):
        self.user_name = user_name
        
    def set_password(self, password):
        self.password = password
        
    
    @classmethod
    def create_with_auth(cls, user_name, password):
        connection = cls('EUA')
        connection.user_name = user_name
        connection.password = password
        return connection
    
    
    
    def connection_log(msg):
        return 'LOG:', msg
    
    
c1 = Connection('local')
c1.set_user('Arthur') 
c1.set_password('1234') 
print(f'c1 Host: {c1.localhost}')
print(f'c1 username: {c1.user_name}')
print(f'c1 password: {c1.password}')

print()
print('=' * 20) 
print() 

c2 = Connection.create_with_auth('Peter', '5757')
print(f'c2 Host: {c2.localhost}')
print(f'c2 username: {c2.user_name}')
print(f'c2 password: {c2.password}')

print()
print('=' * 20) 
print() 

log_message = Connection.connection_log('Está é uma mensagem de log')
print(*log_message)